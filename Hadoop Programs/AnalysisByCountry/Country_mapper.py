#!/usr/bin/env python
import sys

for line in sys.stdin:
	line=line.strip()
	entries=line.split('\t')
	country=entries[2].strip()
	if entries[4].strip()=="-":
		entries[4]="0"
	if entries[5].strip()=="-":
		entries[5]="0"
 
	dead_wounded=int(entries[4])+int(entries[5])
   
	if country==sys.argv[1].strip():
		print entries[0].strip()+";"+str(dead_wounded)+"\t"+"1"
       
