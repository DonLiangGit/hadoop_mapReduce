import sys

salesTotal = 0
oldKey = None
# all these codes are based on the assumption that the intermediate results from mappers are sorted already.

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	
	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue
	thisKey, thisSale = data_mapped
	
	if oldKey and oldKey != thisKey: # print when it changes to a new product.
		print oldKey, "\t", salesTotal
		oldKey = thisKey;
		salesTotal = 0
		
	oldKey = thisKey
	salesTotal += float(thisSale)
	
if oldKey != None: # print the last record.
	print oldKey, "\t", salesTotal
