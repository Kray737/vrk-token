"""Payment provider layer (rubles). YooKassa implementation."""
import uuid
import httpx

from config import YOOKASSA_SHOP_ID, YOOKASSA_SECRET_KEY, PAYMENT_BASE_URL

YOOKASSA_URL = "https://api.yookassa.ru/v3/payments"


def create_payment(amount_rub: float, description: str, return_url: str) -> str:
    """Create a YooKassa payment and return the confirmation URL."""
    payload = {
        "amount": {"value": f"{amount_rub:.2f}", "currency": "RUB"},
        "capture": True,
        "confirmation": {"type": "redirect", "return_url": return_url},
        "description": description,
        "metadata": {"order": str(uuid.uuid4())},
    }
    auth = (YOOKASSA_SHOP_ID, YOOKASSA_SECRET_KEY)
    r = httpx.post(YOOKASSA_URL, json=payload, auth=auth, timeout=20)
    r.raise_for_status()
    return r.json()["confirmation"]["redirect_url"]


async def handle_webhook(payload: dict) -> dict:
    """Process YooKassa webhook; returns the order to fulfil."""
    event = payload.get("event")
    if event == "payment.succeeded":
        obj = payload.get("object", {})
        return {
            "event": "paid",
            "amount": float(obj.get("amount", {}).get("value", 0)),
            "order": obj.get("metadata", {}).get("order"),
        }
    return {"event": "ignored"}
