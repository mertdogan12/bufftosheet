from dotenv import load_dotenv

import buffapi

load_dotenv()

inv = buffapi.getinv()

for i in inv.items:
    print("%s, %g yen" % (i.name, i.price))

print("Total %g yen" % inv.total_ammount)
