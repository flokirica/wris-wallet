from bitcoinlib.keys import Key
from bitcoinlib.wallets import Wallet, wallet_delete_if_exists
from bip_utils import Bip44, Bip44Coins, Bip39SeedGenerator
import os

class BitcoinWallet:
    """Bitcoin wallet handler"""
    
    def __init__(self, network: str = None):
        self.network = network or os.getenv('BITCOIN_NETWORK', 'mainnet')
    
    def create_from_seed(self, seed_phrase: str, index: int = 0):
        """Create Bitcoin account from seed phrase"""
        try:
            # Generate seed from mnemonic
            seed_bytes = Bip39SeedGenerator(seed_phrase).Generate()
            
            # Derive path: m/44'/0'/0'/0/{index}
            bip44_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
            bip44_acc_ctx = bip44_ctx.Purpose().Coin().Account(0).Change(0).AddressIndex(index)
            
            private_key_hex = bip44_acc_ctx.PrivateKey().RawCompressed().ToHex()
            
            # Create key
            key = Key.from_text(private_key_hex, network=self.network)
            
            return {
                'address': key.address(),
                'private_key': private_key_hex,
                'public_key': key.public_hex,
                'wif': key.wif()  # Wallet Import Format
            }
        except Exception as e:
            raise Exception(f"Failed to create Bitcoin wallet: {str(e)}")
