# Binance Futures Testnet Trading Bot

A simple Python command-line trading bot that places **Market** and **Limit** orders on the **Binance USDT-M Futures Testnet**.

## Features

- Place **Market Orders**
- Place **Limit Orders**
- Supports **BUY** and **SELL**
- Command Line Interface (CLI)
- Input Validation
- Logging of API requests, responses, and errors
- Exception Handling
- Modular project structure

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

---

## Requirements

- Python 3.10+
- Binance Futures Testnet Account
- API Key
- Secret Key

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/trading_bot.git
cd trading_bot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Setup

Create a `.env` file in the project root.

```
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
```

Generate your API keys from Binance Futures Testnet:

https://testnet.binancefuture.com

---

## Usage

### Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example Output

```
========== ORDER REQUEST ==========

Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001

Submitting order...

========== ORDER RESPONSE ==========

Order ID      : 18159576467
Status        : NEW
Executed Qty  : 0.0000
Average Price : Not Available

Order placed successfully!
```

---

### Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

---

## Logging

All API requests, responses, and errors are stored in

```
logs/trading.log
```

Example

```
2026-07-01 10:20:33 INFO Order Request | Symbol=BTCUSDT Side=BUY Type=MARKET Quantity=0.001

2026-07-01 10:20:34 INFO Create Order Response {...}

2026-07-01 10:20:34 INFO Order Details {...}
```

---

## Error Handling

The application handles:

- Invalid order side
- Invalid order type
- Invalid quantity
- Missing price for LIMIT orders
- Binance API errors
- Network errors
- Unexpected exceptions

---

## Assumptions

- Uses Binance USDT-M Futures Testnet.
- API credentials are stored in a `.env` file.
- The Binance Testnet account has sufficient demo balance.
- Internet connection is available.

---

## Technologies Used

- Python 3
- python-binance
- argparse
- python-dotenv
- logging

---

## Author

**Anuradha Singh**