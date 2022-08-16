import json
import os
import random

#file count from env var
count = int(os.getenv('FILE_COUNT') or 10)
words = [word.strip() for word in open('/usr/share/dict/words',  'r').readlines()]

for id in range(count):
    amount  = random.uniform(1.0, 1000)
    content =  {'topic': random.choice(words), 'value': "%.2f" % amount}

    with open(f'./files/receipt-{id}.json', 'w') as f:
        json.dump(content, f)