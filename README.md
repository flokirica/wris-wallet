# WRIS Wallet 🌐

**Multichain Cryptocurrency Wallet** - Browser-based web app with support for Ethereum, BSC, Polygon, Solana, and Bitcoin.

## Features ✨

- ✅ Multi-chain support (Ethereum, BSC, Polygon, Solana, Bitcoin)
- ✅ Create New Wallet
- ✅ Import/Export Seed Phrases
- ✅ Multiple Accounts Management
- ✅ Real-time Balance Tracking
- ✅ Transaction History
- ✅ DApps Browser Integration
- ✅ Beautiful UI (White background, Purple glitter font)
- ✅ Secure local storage with encryption

## Tech Stack 🛠️

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Blockchain**: Web3.py, Solana.py, Bitcoin libraries
- **Database**: SQLite
- **UI**: Custom CSS with Purple Glitter theme

## Installation 📦

### Prerequisites
- Python 3.9+
- pip
- Git

### Setup

1. Clone the repository:
```bash
git clone https://github.com/flokirica/wris-wallet.git
cd wris-wallet
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
```

5. Run the application:
```bash
python app.py
```

6. Open browser:
```
http://localhost:5000
```

## Project Structure 📁

```
wris-wallet/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore file
│
├── config/
│   ├── __init__.py
│   ├── settings.py       # Configuration settings
│   └── blockchain_config.py  # Blockchain RPC endpoints
│
├── wallet/
│   ├── __init__.py
│   ├── manager.py        # Wallet management logic
│   ├── crypto.py         # Encryption/decryption utils
│   ├── ethereum.py       # Ethereum/BSC/Polygon handler
│   ├── solana.py         # Solana handler
│   └── bitcoin.py        # Bitcoin handler
│
├── database/
│   ├── __init__.py
│   ├── models.py         # Database models
│   └── db_manager.py     # Database operations
│
├── api/
│   ├── __init__.py
│   ├── routes.py         # API routes
│   ├── wallet_routes.py  # Wallet endpoints
│   ├── transaction_routes.py  # Transaction endpoints
│   └── account_routes.py  # Account endpoints
│
├── static/
│   ├── css/
│   │   └── style.css     # Purple glitter theme
│   ├── js/
│   │   ├── main.js       # Main JavaScript
│   │   ├── wallet.js     # Wallet logic
│   │   ├── transactions.js  # Transaction logic
│   │   └── dapps.js      # DApps browser
│   └── images/
│       └── logo.png      # WRIS Wallet logo
│
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── dashboard.html    # Wallet dashboard
│   ├── create_wallet.html    # Create new wallet
│   ├── import_wallet.html    # Import wallet
│   ├── transactions.html     # Transaction history
│   ├── accounts.html     # Multiple accounts
│   ├── dapps.html        # DApps browser
│   └── settings.html     # Settings
│
└── tests/
    ├── __init__.py
    ├── test_wallet.py
    └── test_blockchain.py
```

## API Endpoints 🔌

### Wallet Management
- `POST /api/wallet/create` - Create new wallet
- `POST /api/wallet/import` - Import wallet from seed phrase
- `GET /api/wallet/export` - Export seed phrase
- `GET /api/wallet/balance` - Get wallet balance

### Accounts
- `GET /api/accounts` - List all accounts
- `POST /api/accounts/create` - Create new account
- `GET /api/accounts/{id}` - Get account details

### Transactions
- `GET /api/transactions` - Get transaction history
- `POST /api/transactions/send` - Send transaction
- `GET /api/transactions/{hash}` - Get transaction details

### DApps
- `GET /api/dapps` - List available DApps
- `POST /api/dapps/connect` - Connect to DApp

## Security Notes 🔐

- Seed phrases are encrypted before storage
- Private keys never stored in plain text
- Local encryption using cryptography library
- HTTPS recommended for production
- Never expose .env file

## Contributing 🤝

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License 📄

MIT License - see LICENSE file for details

## Support 💬

For issues and questions, please open an issue on GitHub.

---

**Made with ❤️ by flokirica**
