
import argparse


def convert(amount: float) -> float:
    exchange_rate = 25.00
    return amount * exchange_rate


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("amount", type=float)
    args = parser.parse_args()

    result = convert(args.amount)
    print(f"{args.amount} BLR в RUB: {result}")
