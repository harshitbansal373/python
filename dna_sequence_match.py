# Written by: MuseHD - https://github.com/musehd
# Purpose: Obtaining matching bases sequence in a DNA

print("How this works:")
print("Input a sequence of nucleotides that form alleles in a DNA using the letters G A C and T without spaces.")
print("This program will output the matching base to form a pair")
print()
DNA = input("INPUT DNA CODE: ").lower()

outlist = []

for letter in DNA:
	if letter == 'g':
		outlist.append("C")
	elif letter =='c' :
		outlist.append("G")
	elif letter =='a':
		outlist.append("T")
	elif letter == 't':
		outlist.append("A")
	else:
		print("You had invalid characters!")
		exit()
		break

print("Matching bases sequence is: ")
for x in outlist:
	print(x,end='')