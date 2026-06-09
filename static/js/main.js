// WRIS Wallet - Main JavaScript

const API_BASE = '/api';

// Wallet Manager
class WalletApp {
  constructor() {
    this.wallet = null;
    this.currentAccount = null;
    this.init();
  }

  async init() {
    console.log('WRIS Wallet initialized');
    await this.loadWallets();
  }

  async loadWallets() {
    try {
      const response = await fetch(`${API_BASE}/wallet/list`);
      const wallets = await response.json();
      console.log('Loaded wallets:', wallets);
      return wallets;
    } catch (error) {
      console.error('Error loading wallets:', error);
    }
  }

  async createWallet(walletName, password) {
    try {
      const response = await fetch(`${API_BASE}/wallet/create`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          wallet_name: walletName,
          password: password
        })
      });
      const data = await response.json();
      if (response.ok) {
        this.showAlert('Wallet created successfully! Save your seed phrase!', 'success');
        return data;
      } else {
        this.showAlert(data.error || 'Error creating wallet', 'danger');
        return null;
      }
    } catch (error) {
      console.error('Error creating wallet:', error);
      this.showAlert('Error creating wallet', 'danger');
    }
  }

  async importWallet(seedPhrase, walletName, password) {
    try {
      const response = await fetch(`${API_BASE}/wallet/import`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          seed_phrase: seedPhrase,
          wallet_name: walletName,
          password: password
        })
      });
      const data = await response.json();
      if (response.ok) {
        this.showAlert('Wallet imported successfully!', 'success');
        return data;
      } else {
        this.showAlert(data.error || 'Error importing wallet', 'danger');
        return null;
      }
    } catch (error) {
      console.error('Error importing wallet:', error);
      this.showAlert('Error importing wallet', 'danger');
    }
  }

  async exportWallet(walletId, password) {
    try {
      const response = await fetch(`${API_BASE}/wallet/export/${walletId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ password: password })
      });
      const data = await response.json();
      if (response.ok) {
        return data.seed_phrase;
      } else {
        this.showAlert('Failed to export wallet', 'danger');
        return null;
      }
    } catch (error) {
      console.error('Error exporting wallet:', error);
      this.showAlert('Error exporting wallet', 'danger');
    }
  }

  showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;
    
    const container = document.querySelector('.container') || document.body;
    container.insertBefore(alertDiv, container.firstChild);
    
    setTimeout(() => alertDiv.remove(), 4000);
  }
}

// Initialize app
const app = new WalletApp();
