import diaryMain as dm
from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument('searchEntry', help='Search entries through db')

args: Namespace = parser.parse_args()

print(args.searchEntry)
