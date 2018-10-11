#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt




x = [1]
rainPercent = [35,148,187,160,125,82,81,59,44,36,21,9,6,4,2]

lenghtnum = 0
count = 0


while (lenghtnum < 14):
    count = rainPercent[lenghtnum]
    while (count > 1):
        x.append(lenghtnum + 1)
        count = count - 1
    lenghtnum = lenghtnum + 1


num_bins = 14
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, density = 1, align='right', facecolor='blue', alpha=0.5)

# note align='right' puts the number in the center of the bar indicating this is a histagram of indivudal numbers

plt.xlabel('length of words')
plt.ylabel('percent of words')

 
# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)




plt.show()
