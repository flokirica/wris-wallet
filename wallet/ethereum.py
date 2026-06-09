from web3 import Web3
from eth_keys import keys
from eth_account import Account
from bip_utils import Bip44, Bip44Coins, Bip39MnemonicGenerator, Bip39SeedGenerator
import os

class EthereumWallet:
    """Ethereum/EVM compatible wallet handler"""
    
    def __init__(self, rpc_url: str = None):
        default_rpc = os.getenv('ETHEREUM_RPC', 'https://eth-rpc.gateway.pokt.network')
        self.w3 = Web3(Web3.HTTPProvider(rpc_url or default_rpc))
    
    def create_from_seed(self, seed_phrase: str, index: int = 0):
        """Create Ethereum account from seed phrase"""
        try:
            # Generate seed from mnemonic
            seed_bytes = Bip39SeedGenerator(seed_phrase).Generate()
            
            # Derive path: m/44'/60'/0'/0/{index}
            bip44_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
            bip44_acc_ctx = bip44_ctx.Purpose().Coin().Account(0).Change(0).AddressIndex(index)
            
            private_key = bip44_acc_ctx.PrivateKey().RawCompressed().ToHex()
            
            # Create account
            account = Account.from_key(private_key)
            
            return {
                'address': account.address,
                'private_key': private_key,
                'public_key': account.key.public_key.to_hex()
            }
        except Exception as e:
            raise Exception(f"Failed to create Ethereum wallet: {str(e)}")
    
    def get_balance(self, address: str) -> dict:
        """Get account balance"""
        try:
            balance_wei = self.w3.eth.get_balance(address)
            balance_eth = self.w3.from_wei(balance_wei, 'ether')
            return {
                'balance': str(balance_eth),
                'balance_wei': str(balance_wei),
                'address': address
            }
        except Exception as e:
            raise Exception(f"Failed to get balance: {str(e)}")
    
    def send_transaction(self, from_address: str, to_address: str, amount: float, private_key: str) -> dict:
        """Send transaction"""
        try:
            account = Account.from_key(private_key)
            
            # Get nonce
            nonce = self.w3.eth.get_transaction_count(from_address)
            
            # Get gas price
            gas_price = self.w3.eth.gas_price
            
            # Build transaction
            tx = {
                'from': from_address,
                'to': to_address,
                'value': self.w3.to_wei(amount, 'ether'),
                'gas': 21000,
                'gasPrice': gas_price,
                'nonce': nonce,
                'chainId': self.w3.eth.chain_id
            }
            
            # Sign transaction
            signed_tx = self.w3.eth.account.sign_transaction(tx, private_key)
            
            # Send transaction
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return {'tx_hash': tx_hash.hex()}
        except Exception as e:
            raise Exception(f"Failed to send transaction: {str(e)}")
