from flask import Blueprint, jsonify
from config.blockchain_config import BLOCKCHAIN_CONFIG

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'WRIS Wallet API'
    })

@api_bp.route('/chains', methods=['GET'])
def get_chains():
    """Get list of supported chains"""
    return jsonify(BLOCKCHAIN_CONFIG)
