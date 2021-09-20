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

        database[uuid] = { #STOCK LOCATOR,ITEM ORDER,DESCRIPTION,SUB DESCRIPTION,PRICE BUY,PRICE SELL,UNIT UPC,PACK UPC,QTY,DEPARTMENT,VENDOR ID
            "STOCK LOCATOR"   : uuid,
            "ITEM ORDER"      : line[1],
            "DESCRIPTION"     : line[2],
            "SUB-DESCRIPTION" : line[3],
            "PRICE BUY"       : line[4],
            "PRICE SELL"      : line[5],
            "UNIT UPC"        : line[6],
            "PACK UPC"        : line[7],
            "QTY"             : line[8],
            "DEPARTMENT"      : line[9],
            "VENDOR ID"       : line[10],
        }

    db    = json.dumps(database, indent=2, sort_keys=True)

    with open('db.json', 'w') as f:
        f.write(db)

