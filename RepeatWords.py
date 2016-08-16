# At every instance of space it adds one to the value because if there was a spcae there was a word before it 
def wordNumbers(fin):
	f = open(fin);
	emma = f.read();
	value = 0
	for i in range(0, len(emma)):
		if(emma[i] == ' '):
			value+=1
	# + 1 to account for last word		
	return value + 1

#	while there is a next line loop through value and then return when done
def lineNumbers(fin):
	f = open(fin);
	value = 0
	done = False
	while(not done):
		s = f.readline()
		if(not(s == "")):
			value+=1
		else:
			done = True
	return value
#initializes value list of lenth wordList with all vals equal to 0 and then each time it finds word in list it incrments corresponding val count then writes to file with corresponding word & val
def repeatedWords (fin, word_list):
	f = open(fin)
	emma = f.read();
	vals = [0]*len(word_list)
	for i in range(0 , len(word_list)):
		vals[i] = 0
	w = ""
	for i in range(0, len(emma)):
		if(str(emma[i]).isalpha()):
			w += emma[i]
		else:
			for j in range(0, len(word_list)):
				if(w.lower() == word_list[j].lower()):
					vals[j] += 1
			w = ""
	x = open("Repeated_word.txt", 'w')
	for i in range(0,len(word_list)):
		x.write(str(word_list[i]) + " "+ str(vals[i]) + " times\n")
	x.close()
#finds words and then if word is equal to key words it will set w to replacement word and add to edited file. else increments onto edited everytime	
def editWords(fin):
	f = open(fin)
	emma = f.read();
	w = ""
	edited = ""
	for i in range(0, len(emma)):
		if(str(emma[i]).isalpha()):
			w += emma[i]
		else:
			if(w == "Emma"):
				w = "George"
			if(w == "her" or w == "Her"):
				w = "his"
			if(w == "she" or w == "She"):
				w = "he"
			edited += w +emma[i]
			w = ""
	x = open("Edited.txt",'w')
	x.write(edited)
	x.close
#test case 	
def main():
	print str(wordNumbers("emma.txt"))
	print str(lineNumbers("emma.txt"))
	repeatedWords("emma.txt",  ['Emma', 'Woodhouse', 'father', 'Taylor', 'Miss', 'been', 'she', 'her'])
	editWords("emma.txt")
	#his has one extra count because the orginal story has an extra his
	repeatedWords("Edited.txt",  ['George', 'he','his'])

