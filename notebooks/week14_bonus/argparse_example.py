import argparse

parser = argparse.ArgumentParser(description="Calculate the square of a number.")
parser.add_argument("number", type=int, help="The number to square")

args = parser.parse_args()
print(f"The square of {args.number} is {args.number ** 2}")
