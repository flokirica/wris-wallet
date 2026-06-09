from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

class Wallet(db.Model):
    """Wallet model"""
    __tablename__ = 'wallets'
    
    id = db.Column(db.Integer, primary_key=True)
    wallet_name = db.Column(db.String(255), nullable=False)
    encrypted_seed_phrase = db.Column(db.Text, nullable=False)
    accounts = db.relationship('Account', backref='wallet', lazy=True, cascade='all, delete-orphan')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'wallet_name': self.wallet_name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Account(db.Model):
    """Account model (for multiple accounts per wallet)"""
    __tablename__ = 'accounts'
    
    id = db.Column(db.Integer, primary_key=True)
    wallet_id = db.Column(db.Integer, db.ForeignKey('wallets.id'), nullable=False)
    account_name = db.Column(db.String(255), nullable=False)
    blockchain = db.Column(db.String(50), nullable=False)  # ethereum, bsc, polygon, solana, bitcoin
    address = db.Column(db.String(255), nullable=False, unique=True)
    encrypted_private_key = db.Column(db.Text, nullable=False)
    public_key = db.Column(db.String(255))
    transactions = db.relationship('Transaction', backref='account', lazy=True, cascade='all, delete-orphan')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'wallet_id': self.wallet_id,
            'account_name': self.account_name,
            'blockchain': self.blockchain,
            'address': self.address,
            'public_key': self.public_key,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Transaction(db.Model):
    """Transaction model"""
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    tx_hash = db.Column(db.String(255), unique=True, nullable=False)
    from_address = db.Column(db.String(255), nullable=False)
    to_address = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.String(255), nullable=False)
    fee = db.Column(db.String(255))
    status = db.Column(db.String(50))  # pending, confirmed, failed
    blockchain = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'tx_hash': self.tx_hash,
            'from_address': self.from_address,
            'to_address': self.to_address,
            'amount': self.amount,
            'fee': self.fee,
            'status': self.status,
            'blockchain': self.blockchain,
            'timestamp': self.timestamp.isoformat(),
            'created_at': self.created_at.isoformat()
        }

class DApp(db.Model):
    """DApp model for browser integration"""
    __tablename__ = 'dapps'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    url = db.Column(db.String(255), nullable=False)
    icon = db.Column(db.String(255))
    category = db.Column(db.String(100))  # defi, nft, gaming, etc
    blockchain = db.Column(db.String(50))  # ethereum, bsc, polygon, solana, bitcoin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'url': self.url,
            'icon': self.icon,
            'category': self.category,
            'blockchain': self.blockchain
        }
