import os
from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///wris_wallet.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# Import models
from database.models import Wallet, Account, Transaction, DApp

# Import API routes
from api.routes import api_bp
from api.wallet_routes import wallet_bp
from api.account_routes import account_bp
from api.transaction_routes import transaction_bp

# Register blueprints
app.register_blueprint(api_bp)
app.register_blueprint(wallet_bp, url_prefix='/api/wallet')
app.register_blueprint(account_bp, url_prefix='/api/accounts')
app.register_blueprint(transaction_bp, url_prefix='/api/transactions')

# Routes
@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Wallet dashboard"""
    return render_template('dashboard.html')

@app.route('/create')
def create_wallet():
    """Create new wallet page"""
    return render_template('create_wallet.html')

@app.route('/import')
def import_wallet():
    """Import wallet page"""
    return render_template('import_wallet.html')

@app.route('/transactions')
def transactions():
    """Transaction history page"""
    return render_template('transactions.html')

@app.route('/accounts')
def accounts():
    """Accounts management page"""
    return render_template('accounts.html')

@app.route('/dapps')
def dapps():
    """DApps browser page"""
    return render_template('dapps.html')

@app.route('/settings')
def settings():
    """Settings page"""
    return render_template('settings.html')

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return {'error': 'Not found'}, 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return {'error': 'Internal server error'}, 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 5000)),
        debug=os.getenv('FLASK_DEBUG', True)
    )
