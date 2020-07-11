#!/usr/bin/env python3
import argparse
import sys
from utils.crypto.classical import caesar_all
parser = argparse.ArgumentParser(description="Try all caesar shifts on a string.")
parser.add_argument("string", nargs="?", help="string to shift")
parser.add_argument("-a", "--all", help="try all ascii values as shift", action="store_true")
args = parser.parse_args()
alphabet_only = not args.all
s = args.string
if s is None:
	s = sys.stdin.read().strip()
print("\n".join(c[0] for c in caesar_all(s, alphabet_only)))
