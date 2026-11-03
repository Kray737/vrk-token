import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
OWNER_MNEMONIC = os.getenv("OWNER_MNEMONIC", "")
CASH_MNEMONIC = os.getenv("CASH_MNEMONIC", "")
OWNER_ADDRESS = os.getenv("OWNER_ADDRESS", "")
CASH_ADDRESS = os.getenv("CASH_ADDRESS", "")
JETTON_MASTER = os.getenv("JETTON_MASTER", "")
JETTON_WALLET = os.getenv("JETTON_WALLET", "")
PAYMENT_BASE_URL = os.getenv("PAYMENT_BASE_URL", "")
YOOKASSA_SHOP_ID = os.getenv("YOOKASSA_SHOP_ID", "")
YOOKASSA_SECRET_KEY = os.getenv("YOOKASSA_SECRET_KEY", "")
TON_TO_RUB_RATE = float(os.getenv("TON_TO_RUB_RATE", "100.0"))
VRK_PRICE_RUB = float(os.getenv("VRK_PRICE_RUB", "1.0"))
MIN_BUY_RUB = float(os.getenv("MIN_BUY_RUB", "100"))
