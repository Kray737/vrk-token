import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import (ADMIN_ID, BOT_TOKEN, VRK_PRICE_RUB, MIN_BUY_RUB,
                    PAYMENT_BASE_URL, JETTON_MASTER, CASH_ADDRESS)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

WELCOME = (
    "<b>VRK - Вертикальный Рубль</b>\n\n"
    "Цифровой актив, обеспеченный рублём.\n"
    f"Цена: {VRK_PRICE_RUB} ₽ за VRK\n"
    f"Минимальная покупка: {MIN_BUY_RUB:.0f} ₽\n\n"
    "Нажмите «Купить», чтобы оплатить картой и получить токены на свой TON-кошелёк."
)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(WELCOME, parse_mode="HTML")


@dp.callback_query(F.data == "buy")
async def buy(callback):
    await callback.answer()
    await callback.message.answer(
        "Оплата:\n"
        f"1. Перейди на {PAYMENT_BASE_URL}/pay\n"
        "2. Укажи TON-адрес кошелька, куда прислать VRK\n"
        "3. После оплаты токены придут автоматически"
    )


@dp.message(F.text == "/stats")
async def stats(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    await message.answer(
        f"Jetton master: {JETTON_MASTER}\n"
        f"Касса: {CASH_ADDRESS}\n"
        f"Курс TON/₽: {os.getenv('TON_TO_RUB_RATE')}"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
