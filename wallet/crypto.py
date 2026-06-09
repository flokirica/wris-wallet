from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
import os
import base64
from dotenv import load_dotenv

load_dotenv()

class EncryptionManager:
    """Handle encryption and decryption of sensitive data"""
    
    def __init__(self):
        self.encryption_key = os.getenv('ENCRYPTION_KEY', 'default-key').encode()
        
    def derive_key(self, password: str, salt: bytes = None) -> tuple:
        """Derive encryption key from password"""
        if salt is None:
            salt = os.urandom(16)
        
        kdf = PBKDF2(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key, salt
    
    def encrypt(self, data: str, password: str = None) -> str:
        """Encrypt data"""
        if password:
            key, salt = self.derive_key(password)
            cipher = Fernet(key)
            encrypted = cipher.encrypt(data.encode())
            return base64.b64encode(salt + encrypted).decode()
        else:
            cipher = Fernet(self.encryption_key)
            encrypted = cipher.encrypt(data.encode())
            return encrypted.decode()
    
    def decrypt(self, encrypted_data: str, password: str = None) -> str:
        """Decrypt data"""
        try:
            if password:
                data = base64.b64decode(encrypted_data.encode())
                salt = data[:16]
                encrypted = data[16:]
                key, _ = self.derive_key(password, salt)
                cipher = Fernet(key)
                decrypted = cipher.decrypt(encrypted)
                return decrypted.decode()
            else:
                cipher = Fernet(self.encryption_key)
                decrypted = cipher.decrypt(encrypted_data.encode())
                return decrypted.decode()
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")
