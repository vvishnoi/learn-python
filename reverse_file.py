import argparse
from ast import arg;
import sys

parser  = argparse.ArgumentParser(description='Read file and reverse')
parser.add_argument('file_name', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='number of lines ot read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')


args  = parser.parse_args()

print(f"argus: {args}")

try:
    f = open(args.file_name)
    limit  = args.limit
except FileNotFoundError as err:
    print (f"Error: {err}")
    sys.exit(2)
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]
    for line in lines:
        print(line.strip()[::-1])
finally:
    print('program is complete')