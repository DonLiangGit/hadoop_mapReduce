import sys

highestSale = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
		
    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)
	
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", highestSale
        oldKey = thisKey;
        highestSale = 0
		
    oldKey = thisKey
	
    if thisSale > highestSale:# if this one is put above the oldkey it may get wipe the oldkey highestSale.
        highestSale = thisSale
		
if oldKey != None:
    print oldKey, "\t", highestSale
