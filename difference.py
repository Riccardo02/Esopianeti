import os
import sys


for i in range(1000):
	os.system("compare -compose src " + str(i) + ".png " + str(i+1) + ".png" + str(" difference/diff_" + str(i)))

