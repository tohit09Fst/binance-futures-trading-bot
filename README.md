# Binance Futures Testnet Trading Bot

A simple Python CLI application that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features

- MARKET order
- LIMIT order
- BUY / SELL support
- CLI input using argparse
- Logging of API responses
- Error handling

## Setup

Install dependencies:

pip install -r requirements.txt

Add API credentials in `bot/client.py`.

## Run Examples

Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 90000

## Logs

All API responses and errors are logged in:

trading_bot.log
