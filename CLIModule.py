from diaryMain import Diary
import argparse

#create the top-level parser and create class-insance
diary = Diary()
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(required=True)

#create the parser for the "add" command
parser_add = subparsers.add_parser('add')
parser_add.set_defaults(func=diary.append)