import argparse
from diaryMain import Diary

def main():
    diary = Diary()
    parser = argparse.ArgumentParser(description='Diary CLI')
    subparsers = parser.add_subparsers(dest='command')

    create_parser = subparsers.add_parser('create', help='Create the database')
    create_parser.set_defaults(func=diary.createDB)

    add_parser = subparsers.add_parser('add', help='Add a new entry')
    add_parser.add_argument('--entry', type=str, required=True, help='The text of the entry')
    add_parser.add_argument('--mood', type=str, required=True, help='The mood of the entry')
    add_parser.set_defaults(func=lambda args: diary.addEntry(args.entry, args.mood))

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
