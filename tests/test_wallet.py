import pytest
from wallet.manager import WalletManager
from wallet.crypto import EncryptionManager

class TestWalletManager:
    def setup_method(self):
        self.wallet_manager = WalletManager()
    
    def test_create_new_wallet(self):
        wallet_data = self.wallet_manager.create_new_wallet()
        assert 'seed_phrase' in wallet_data
        assert 'wallets' in wallet_data
        assert 'ethereum' in wallet_data['wallets']
        assert 'solana' in wallet_data['wallets']
        assert 'bitcoin' in wallet_data['wallets']
    
    def test_import_valid_wallet(self):
        # Create a wallet first
        original = self.wallet_manager.create_new_wallet()
        seed_phrase = original['seed_phrase']
        
        # Import the same wallet
        imported = self.wallet_manager.import_wallet(seed_phrase)
        
        assert imported is not None
        assert 'wallets' in imported

class TestEncryptionManager:
    def setup_method(self):
        self.encryption = EncryptionManager()
    
    def test_encrypt_decrypt(self):
        data = "secret seed phrase"
        password = "test-password"
        
        encrypted = self.encryption.encrypt(data, password)
        decrypted = self.encryption.decrypt(encrypted, password)
        
        assert decrypted == data
    
    def test_decrypt_wrong_password(self):
        data = "secret data"
        password = "correct-password"
        
        encrypted = self.encryption.encrypt(data, password)
        
        with pytest.raises(ValueError):
            self.encryption.decrypt(encrypted, "wrong-password")
