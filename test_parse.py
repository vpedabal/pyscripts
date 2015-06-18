import re
from tabulate import tabulate

allsamples = "ctime=2014-10-29 16:50:05-0700,hostname=vpedabal-crownpass-6-4,rank=1,pid=108524,cmd=orcmd,state=S,percent_cpu=0.000000,priority=20,num_threads=3,vsize=185.921875,rss=4.062500,peak_vsize=249.792969,processor=31@"

persample = re.split("@",allsamples)
entries = re.split(",",persample[0])
for y in range(2,len(entries)):
    pair = re.split("=",entries[y])
    value = re.split(":",pair[1])
    num = re.split(".",value[0])
    print(pair)
#    print (pair[0],"\n", end="")
 

print ("\n")
for x in range(0,len(persample)):
    entries = re.split(",",persample[x])
    for y in range(2,len(entries)):
        pair = re.split("=",entries[y])
        value = re.split(":",pair[1])
        num = re.split("\.",value[0])
        print(num[0]," ", end="")
    print("\n")


