from flask import Blueprint, request, jsonify
from wallet.manager import WalletManager
from wallet.crypto import EncryptionManager
from database.models import Wallet, Account
from app import db

wallet_bp = Blueprint('wallet', __name__)
wallet_manager = WalletManager()
encryption = EncryptionManager()

@wallet_bp.route('/create', methods=['POST'])
def create_wallet():
    """Create new wallet"""
    try:
        data = request.get_json()
        wallet_name = data.get('wallet_name', 'My Wallet')
        password = data.get('password', '')
        
        # Create wallet
        wallet_data = wallet_manager.create_new_wallet(password)
        seed_phrase = wallet_data['seed_phrase']
        
        # Encrypt and store
        encrypted_seed = encryption.encrypt(seed_phrase, password)
        new_wallet = Wallet(wallet_name=wallet_name, encrypted_seed_phrase=encrypted_seed)
        db.session.add(new_wallet)
        db.session.commit()
        
        # Create accounts for each blockchain
        for blockchain, account_data in wallet_data['wallets'].items():
            encrypted_private_key = encryption.encrypt(account_data['private_key'], password)
            account = Account(
                wallet_id=new_wallet.id,
                account_name=f"{blockchain.capitalize()} Account",
                blockchain=blockchain,
                address=account_data['address'],
                encrypted_private_key=encrypted_private_key,
                public_key=account_data.get('public_key', '')
            )
            db.session.add(account)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'wallet_id': new_wallet.id,
            'wallet_name': wallet_name,
            'seed_phrase': seed_phrase,
            'message': 'Wallet created successfully. Save your seed phrase!'
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@wallet_bp.route('/import', methods=['POST'])
def import_wallet():
    """Import wallet from seed phrase"""
    try:
        data = request.get_json()
        seed_phrase = data.get('seed_phrase', '').strip()
        wallet_name = data.get('wallet_name', 'Imported Wallet')
        password = data.get('password', '')
        
        # Import wallet
        wallet_data = wallet_manager.import_wallet(seed_phrase)
        
        # Store encrypted
        encrypted_seed = encryption.encrypt(seed_phrase, password)
        new_wallet = Wallet(wallet_name=wallet_name, encrypted_seed_phrase=encrypted_seed)
        db.session.add(new_wallet)
        db.session.commit()
        
        # Create accounts
        for blockchain, account_data in wallet_data['wallets'].items():
            encrypted_private_key = encryption.encrypt(account_data['private_key'], password)
            account = Account(
                wallet_id=new_wallet.id,
                account_name=f"{blockchain.capitalize()} Account",
                blockchain=blockchain,
                address=account_data['address'],
                encrypted_private_key=encrypted_private_key,
                public_key=account_data.get('public_key', '')
            )
            db.session.add(account)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'wallet_id': new_wallet.id,
            'wallet_name': wallet_name,
            'message': 'Wallet imported successfully'
        }), 201
    except ValueError as e:
        return jsonify({'error': 'Invalid seed phrase'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@wallet_bp.route('/export/<int:wallet_id>', methods=['POST'])
def export_wallet(wallet_id):
    """Export seed phrase from wallet"""
    try:
        data = request.get_json()
        password = data.get('password', '')
        
        wallet = Wallet.query.get_or_404(wallet_id)
        seed_phrase = encryption.decrypt(wallet.encrypted_seed_phrase, password)
        
        return jsonify({
            'seed_phrase': seed_phrase,
            'warning': 'Never share your seed phrase with anyone!'
        }), 200
    except Exception as e:
        return jsonify({'error': 'Failed to export wallet'}), 400

@wallet_bp.route('/list', methods=['GET'])
def list_wallets():
    """List all wallets"""
    wallets = Wallet.query.all()
    return jsonify([w.to_dict() for w in wallets])
