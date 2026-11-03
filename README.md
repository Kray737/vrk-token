# VRK - Вертикальный Рубль

Цифровой актив на TON (стандарт TEP-74 Jetton).

## Структура

```
contracts/
  jetton-minter.fc     - мастер-контракт (mint, burn, метаданные)
  jetton-wallet.fc     - кошелёк держателя токена
  imports/             - вспомогательные библиотеки
bot/
  main.py              - Telegram-бот (aiogram 3)
  ton.py               - работа с TON/джетоном
  payments.py          - приём оплаты в рублях (ЮKassa)
  config.py            - конфиг из .env
metadata/
  VRK_metadata.json    - оффчейн-метаданные токена
```

## Деплой

1. Положить реальный `stdlib.fc` из `ton-blockchain/ton` в `contracts/imports/`.
2. Скомпилировать:

```bash
docker run --rm -v "$PWD":/work ton-blockchain/ton/compiler:0.5.0 \
  func -SPA contracts/jetton-minter.fc contracts/jetton-wallet.fc -o build/
```

3. Задеплоить мастер-контракт (`jetton-minter`), передав в init:
   - owner address
   - jetton wallet code cell
   - metadata cell
   - content cell (ссылка на VRK_metadata.json)
4. Задеплоить кошелёк-джетон владельца, зачеканить 1 000 000 000 VRK.

## Лендинг

https://vrk-token-wz5w130x.agent.mira.tg

## Важно

Приём рублёвой оплаты требует договора с платёжным агрегатором и статуса ИП/самозанятого.
