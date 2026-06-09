from flask import Blueprint, request, jsonify
from database.models import Account, Wallet
from app import db

account_bp = Blueprint('accounts', __name__)

@account_bp.route('/', methods=['GET'])
def list_accounts():
    """List all accounts"""
    wallet_id = request.args.get('wallet_id')
    if wallet_id:
        accounts = Account.query.filter_by(wallet_id=wallet_id).all()
    else:
        accounts = Account.query.all()
    return jsonify([a.to_dict() for a in accounts])

@account_bp.route('/<int:account_id>', methods=['GET'])
def get_account(account_id):
    """Get account details"""
    account = Account.query.get_or_404(account_id)
    return jsonify(account.to_dict())

@account_bp.route('/', methods=['POST'])
def create_account():
    """Create new account in wallet"""
    try:
        data = request.get_json()
        # Implementation for creating additional accounts
        return jsonify({'message': 'Account creation not yet implemented'}), 501
    except Exception as e:
        return jsonify({'error': str(e)}), 400
