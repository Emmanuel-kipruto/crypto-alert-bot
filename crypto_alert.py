import requests
import smtplib
from email.mime.text import MIMEText
from time import sleep
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# --- Config ---
CRYPTO_ID = "bitcoin"  # e.g., "bitcoin", "ethereum", "dogecoin"
VS_CURRENCY = "usd"
THRESHOLD = 74870  # set your target price
CHECK_INTERVAL = 60  # seconds

# Gmail credentials loaded from .env
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")  # can be the same as sender

# --- Get current price from CoinGecko ---
def get_price():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={CRYPTO_ID}&vs_currencies={VS_CURRENCY}"
    response = requests.get(url)
    data = response.json()
    return data[CRYPTO_ID][VS_CURRENCY]

# --- Send email notification ---
def send_email(current_price):
    subject = f"{CRYPTO_ID.capitalize()} Price Alert!"
    body = f"The price of {CRYPTO_ID.upper()} is now ${current_price:,} USD.\nCheck CoinGecko for more info."
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

# --- Main Loop ---
print("🟢 Crypto price alert bot is running...")
while True:
    try:
        current_price = get_price()  # renamed variable to avoid shadowing
        print(f"[INFO] Current {CRYPTO_ID.upper()} price: ${current_price}")
        if current_price < THRESHOLD:
            print(f"🔔 Price dropped below ${THRESHOLD}! Sending email...")
            send_email(current_price)
            sleep(300)  # Wait for 5 minutes before checking again
        else:
            sleep(CHECK_INTERVAL)
    except Exception as e:
        print(f"[ERROR] {e}")
        sleep(60)
