import csv
import json

#  STOCK LOCATOR | ITEM ORDER | DESCRIPTION | PRICE BUY | PRICE SELL | UPC | DEPARTMENT | SUB DESCRIPTION | QTY | VENDOR ID

with open('Karts-Inventory.csv') as file:
    csv_file = csv.reader(file) 
    next(csv_file)

    database = {}
    for line in csv_file:
        uuid = line[0]
        if len(uuid) == 1:uuid = f'000{uuid}'
        elif len(uuid) == 2:uuid = f'00{uuid}'
        elif len(uuid) == 3:uuid = f'0{uuid}'
        else:pass
        database[uuid] = {}

        database[uuid] = {
            "STOCK LOCATOR"   : uuid,
            "ITEM ORDER"      : line[1],
            "DESCRIPTION"     : line[2],
            "PRICE BUY"       : line[3],
            "PRICE SELL"      : line[4],
            "UPC"             : line[5],
            "DEPARTMENT"      : line[6],
            "SUB DESCRIPTION" : line[7],
            "QTY"             : line[8],
            "VENDOR ID"       : line[9],
        }

    db    = json.dumps(database, indent=2, sort_keys=True)

    with open('db.json', 'w') as f:
        f.write(db)

