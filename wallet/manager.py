from mnemonic import Mnemonic
import os
from wallet.crypto import EncryptionManager
from wallet.ethereum import EthereumWallet
from wallet.solana import SolanaWallet
from wallet.bitcoin import BitcoinWallet

class WalletManager:
    """Main wallet management class"""
    
    def __init__(self):
        self.encryption = EncryptionManager()
        self.mnemonic = Mnemonic('english')
    
    def create_new_wallet(self, password: str = None):
        """Create a new wallet with seed phrase"""
        # Generate mnemonic (12 or 24 words)
        seed_phrase = self.mnemonic.generate(strength=256)  # 24 words
        
        wallet_data = {
            'seed_phrase': seed_phrase,
            'wallets': {
                'ethereum': self._create_ethereum_wallet(seed_phrase),
                'bsc': self._create_ethereum_wallet(seed_phrase),
                'polygon': self._create_ethereum_wallet(seed_phrase),
                'solana': self._create_solana_wallet(seed_phrase),
                'bitcoin': self._create_bitcoin_wallet(seed_phrase)
            }
        }
        
        return wallet_data
    
    def import_wallet(self, seed_phrase: str):
        """Import wallet from seed phrase"""
        # Validate seed phrase
        if not self.mnemonic.check(seed_phrase):
            raise ValueError("Invalid seed phrase")
        
        wallet_data = {
            'seed_phrase': seed_phrase,
            'wallets': {
                'ethereum': self._create_ethereum_wallet(seed_phrase),
                'bsc': self._create_ethereum_wallet(seed_phrase),
                'polygon': self._create_ethereum_wallet(seed_phrase),
                'solana': self._create_solana_wallet(seed_phrase),
                'bitcoin': self._create_bitcoin_wallet(seed_phrase)
            }
        }
        
        return wallet_data
    
    def _create_ethereum_wallet(self, seed_phrase: str):
        """Create Ethereum/EVM wallet from seed phrase"""
        eth_wallet = EthereumWallet()
        return eth_wallet.create_from_seed(seed_phrase)
    
    def _create_solana_wallet(self, seed_phrase: str):
        """Create Solana wallet from seed phrase"""
        solana_wallet = SolanaWallet()
        return solana_wallet.create_from_seed(seed_phrase)
    
    def _create_bitcoin_wallet(self, seed_phrase: str):
        """Create Bitcoin wallet from seed phrase"""
        btc_wallet = BitcoinWallet()
        return btc_wallet.create_from_seed(seed_phrase)
