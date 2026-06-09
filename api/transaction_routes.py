from flask import Blueprint, request, jsonify
from database.models import Transaction, Account
from app import db

transaction_bp = Blueprint('transactions', __name__)

@transaction_bp.route('/', methods=['GET'])
def list_transactions():
    """List transactions"""
    account_id = request.args.get('account_id')
    if account_id:
        transactions = Transaction.query.filter_by(account_id=account_id).all()
    else:
        transactions = Transaction.query.all()
    return jsonify([t.to_dict() for t in transactions])

@transaction_bp.route('/<int:tx_id>', methods=['GET'])
def get_transaction(tx_id):
    """Get transaction details"""
    transaction = Transaction.query.get_or_404(tx_id)
    return jsonify(transaction.to_dict())

@transaction_bp.route('/send', methods=['POST'])
def send_transaction():
    """Send transaction"""
    try:
        data = request.get_json()
        # Implementation for sending transactions
        return jsonify({'message': 'Transaction sending not yet implemented'}), 501
    except Exception as e:
        return jsonify({'error': str(e)}), 400
