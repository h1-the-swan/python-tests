import argparse
parser = argparse.ArgumentParser(description="Test argparse")
parser.add_argument('--tru', action='store_true')
parser.add_argument('--test', type=int)
args = parser.parse_args()
if args.tru:
    print("it's true")
testt = args.test
print(testt)
