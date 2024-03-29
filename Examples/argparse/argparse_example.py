
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("pos1", help="positional argument 1")
parser.add_argument("-o", "--optional-arg", help="optional argument", dest="opt", default="default")

args = parser.parse_args()
print("positional arg:", args.pos1)
print("optional arg:", args.opt)
