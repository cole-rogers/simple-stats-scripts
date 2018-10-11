# Converts a set of numbers into a python list with those numbers occurring multiple times
# IE: by setting the step size to one, and replacing the percentNum list with [40,60], you
# would get an output of 40 1s followed by 60 2s
# almost exclusively useful for generating histograms and some other graph types when only percentages are avalible
# even then, it should still be avoided when possible.




outputNumbers = []

#replace data here with correct percentages, with each percent being for the number of the (index + 1) * the size of each step.
#Use whole numbers only.
#multiply percents by powers of 10 to make them whole numbers if needed
#should probably add up to a power of 10, unless your real percents do not
percentNum = [35,148,187,160,125,82,81,59,44,36,21,9,6,4,2]

## Largest x value
total = 14
## step size.  For whole numbers should be one
step = 1

indexNum = 0
count = 0


while (indexNum < total):
    count = percentNum[indexNum]
    while (count > 1):
        outputNumbers.append(indexNum + 1) # use + 1
        count = count - 1
    indexNum = indexNum + step

print(outputNumbers)
