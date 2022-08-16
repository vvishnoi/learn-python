import argparse


parser  = argparse.ArgumentParser(description='Seach snippet in words file')
parser.add_argument('snippet', help='name of search term' )

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dict/words',  'r') as f:
    words = f.readlines()

    #list comprehensiopns
    matches = [word.strip() for word in words if snippet in word.lower()]

    # for word in words:
    #     if snippet in word.lower():
    #         matches.append(word)

print(matches)