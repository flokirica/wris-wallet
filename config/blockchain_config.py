import os
from dotenv import load_dotenv

load_dotenv()

# Blockchain RPC Endpoints
BLOCKCHAIN_CONFIG = {
    'ethereum': {
        'name': 'Ethereum',
        'rpc': os.getenv('ETHEREUM_RPC', 'https://eth-rpc.gateway.pokt.network'),
        'chain_id': 1,
        'symbol': 'ETH',
        'explorer': 'https://etherscan.io'
    },
    'bsc': {
        'name': 'Binance Smart Chain',
        'rpc': os.getenv('BSC_RPC', 'https://bsc-rpc.gateway.pokt.network'),
        'chain_id': 56,
        'symbol': 'BNB',
        'explorer': 'https://bscscan.com'
    },
    'polygon': {
        'name': 'Polygon',
        'rpc': os.getenv('POLYGON_RPC', 'https://polygon-rpc.gateway.pokt.network'),
        'chain_id': 137,
        'symbol': 'MATIC',
        'explorer': 'https://polygonscan.com'
    },
    'solana': {
        'name': 'Solana',
        'rpc': os.getenv('SOLANA_RPC', 'https://api.mainnet-beta.solana.com'),
        'network': 'mainnet',
        'symbol': 'SOL',
        'explorer': 'https://solscan.io'
    },
    'bitcoin': {
        'name': 'Bitcoin',
        'network': os.getenv('BITCOIN_NETWORK', 'mainnet'),
        'symbol': 'BTC',
        'explorer': 'https://blockchain.com'
    }
}

# Supported chains
SUPPORTED_CHAINS = list(BLOCKCHAIN_CONFIG.keys())
