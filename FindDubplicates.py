#--------------------------------
# Name:         FindDuplicates.py
# Purpose:      Flags duplicates as "1" including the first occurrence
# Author:       Vern Wolfley
# Created       03/02/2012
# Copyright:    MIT
# ArcGIS Version:   10.x
# Python Version:   2.6
# INFO:         Information found at http://forums.arcgis.com/threads/4021-arcgis-10
#--------------------------------

import arcpy
from collections import defaultdict

#ArcMap File name variable.
inft = "G:\GISData\DysartGIS\SY2011_2012\DysartScratch2011_12.gdb\OpenEnrollment_2012_2013"
#Field Name
inField = "Name"
cnt=0

value_list =[]
rows = arcpy.SearchCursor(inft)
for row in rows:
    value = row.getValue(inField)
    value_list.append(value)
duplicate_list = []
dict1 = defaultdict(int)
for value in value_list:
    dict1(value)+1
for key, val in dict1.iteritems():
    if val > 1:
        dup_list.append(key)
print "duplicate list length = ", len(duplicate_list)

del row
del rows

dict1()