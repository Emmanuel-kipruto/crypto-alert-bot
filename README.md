✅ Step 1: Create a README.md
In your Crypto Bot folder, create a new file called README.md and paste the following:

# 🪙 Crypto Alert Bot

A simple Python bot that monitors cryptocurrency prices using the CoinGecko API and sends an email alert when the price drops below a specified threshold.

## 🚀 Features
- Tracks live prices of any coin listed on CoinGecko
- Sends email notifications when price goes below your target
- Easy to configure and run

## 📦 Requirements
- Python 3.x
- `requests` library

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Emmanuel-kipruto/crypto-alert-bot.git
   cd crypto-alert-bot

2. Install dependencies:

pip install requests

3. Edit the script to set:

Your coin of choice (dogecoin, bitcoin, etc.)

The alert price

Your email and app password

4. Run the bot:

python crypto_alert.py

🛡️ Security
Email sending uses a Gmail app password (never hardcode your real Gmail password).

Keep your credentials safe — you can use environment variables for production use.

📄 License
This project is licensed under the MIT License.

Built with ❤️ by Emmanuel Kipruto
