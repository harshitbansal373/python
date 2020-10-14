# A simple program to count and display the most used word on a file

name = input("Enter file:")
if len(name) < 1:
    name = "README.md"

try:
    handle = open(name)
except:
    print("Could not open the file ")
    exit()
parsedsenders = list()
counts = dict()
for line in handle:
    parsedline = line.split()
    for iterator in parsedline:
        counts[iterator] = counts.get(iterator, 0) + 1

bigword = None
bigcount = None

for iterword, itercount in counts.items():
    if bigcount is None or int(itercount) > bigcount:
        bigcount = int(itercount)
        bigword = iterword

print(bigword, bigcount)