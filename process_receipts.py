from glob import glob
import json
import os
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' dir already exist")

paths  = glob(pathname='./files/receipt-[0-9]*.json')

subTotal = 0.0

for path in paths:
    with open(path) as f:
        receipt = json.load(f)
        subTotal += float(receipt['value'])

    name = path.split('/')[-1]
    dest  = f'./processed/{name}'
    print(f"File: {name} processed")

    shutil.move(path, dest)
    print(f"{path} moved to {dest}")

print(f'Total sum {subTotal}')