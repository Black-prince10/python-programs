'''
Sorting:
Sorting is a process of arrangement. It arranges data systematically in a particular format. 
It follows some algorithm to sort data.
'''
string_txt=input("Enter a string to sort the words:") 
words =string_txt.split()
words.sort()
for word in words:
	print(word)

