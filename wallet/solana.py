from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solana.rpc.api import Client
from bip_utils import Bip44, Bip44Coins, Bip39SeedGenerator
import os

class SolanaWallet:
    """Solana wallet handler"""
    
    def __init__(self, rpc_url: str = None):
        default_rpc = os.getenv('SOLANA_RPC', 'https://api.mainnet-beta.solana.com')
        self.client = Client(rpc_url or default_rpc)
    
    def create_from_seed(self, seed_phrase: str, index: int = 0):
        """Create Solana account from seed phrase"""
        try:
            # Generate seed from mnemonic
            seed_bytes = Bip39SeedGenerator(seed_phrase).Generate()
            
            # Derive path: m/44'/501'/0'/0'{index}'
            bip44_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)
            bip44_acc_ctx = bip44_ctx.Purpose().Coin().Account(0).Change(0).AddressIndex(index)
            
            private_key_bytes = bip44_acc_ctx.PrivateKey().RawCompressed().ToBytes()
            
            # Create keypair
            keypair = Keypair.from_secret_key(private_key_bytes)
            
            return {
                'address': str(keypair.pubkey()),
                'private_key': keypair.secret_key.hex(),
                'public_key': str(keypair.pubkey())
            }
        except Exception as e:
            raise Exception(f"Failed to create Solana wallet: {str(e)}")
    
    def get_balance(self, address: str) -> dict:
        """Get account balance in SOL"""
        try:
            pubkey = Pubkey.from_string(address)
            balance = self.client.get_balance(pubkey)
            
            # Convert lamports to SOL (1 SOL = 1 billion lamports)
            balance_sol = balance.value / 1_000_000_000
            
            return {
                'balance': str(balance_sol),
                'balance_lamports': str(balance.value),
                'address': address
            }
        except Exception as e:
            raise Exception(f"Failed to get balance: {str(e)}")
