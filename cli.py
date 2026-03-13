import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

validate_side(args.side)
validate_order_type(args.type)

print("Order Request Summary")
print(args)

if args.type == "MARKET":
    response = place_market_order(args.symbol, args.side, args.quantity)

elif args.type == "LIMIT":
    if not args.price:
        raise ValueError("Price required for LIMIT order")
    response = place_limit_order(args.symbol, args.side, args.quantity, args.price)

print("Order Response:")
print(response)