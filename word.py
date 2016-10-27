graph=[];				#LIST FOR STROING EQUAL LENGTH WORDS

def equallen(data):						#getting values equal to the length of fword
	for val in data:
		if (len(fword) == len(val)):		#IF THE WORD LENGTH IS EQUAL TO THE USER INPUT WORD
			graph.append(val)
	return graph
	
def lettermatch(a,b):						#keeping only those that are at one letter difference
	temp=0;
	for letter,lett in zip(a,b):				#GETTING EACH LETTER OF WORDS TO CHECK THE NUMBER OF SAME LETTERS 
			if (letter == lett and a!=b):
				temp+=1
				if ((len(b)-1) == temp):			#IF ONLY ONE LETTER IS NOT EQUAL
					#pdb.set_trace()
					return True;
	return False;

										#taken from stackoverflow
def bfs(find, start, end):
    
	# maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node == end:
            return path
		# enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in find.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

		###########################################################################################################################3
	
import json				#IMPORTING JSON LIBRARY
import pdb				# FOR DEBUGGING PURPOSE
import os 				#USED FOR FINDING FILE IN os
from collections import defaultdict		#IMPORTING DEFAULT DICTIONARY FOR GRAPH LIKE IMPLEMENTATION

fword = input('Enter first word: ')			#INPUT WORD
sword = input('Enter second word: ')

while(len(fword) != len(sword)):		#LENGTH OF THE WORDS EQUAL OR NOT
	print("Length not equal: ")
	fword = input('Enter first word: ')
	sword = input('Enter second word: ')

fword = fword.upper();				#CONVERTING TO UPPER AS DICTIONARY.JSON HAS UPPERCASE WORDS
sword = sword.upper();
	
with open('Dictionary.json') as data_file:			#GETTING WORDS FROM DICTIONARY
	data = json.load(data_file)
data_file.close();

d = defaultdict(list)					#DEFINING DEFAULTDICT NAMED D

graph = equallen(data)			#GETTING ONLY SAME LENGTH WORDS AS FWORD

#pdb.set_trace()								#TO COMPENSATE FOR SPEED WE ARE SAVING IT IN FILE FOR THE FIRST TIME
if (os.path.exists('./chain.json')):			#CHECKING IF CHAIN.JSON IS AVAILABLE
	with open('chain.json') as data_file:    
		d = json.load(data_file)				#LOADING THIS FILE
else:
	print("Making all chains!!!")
	for j,k in enumerate(graph):
		for l,n in enumerate(graph):				#COMPARING EVERY ELEMENT FOR SAME LETTER MATCH
			if (lettermatch(k,n)):
				d[k].append(n);
	with open('chain.json', 'w') as outfile:
		json.dump(d, outfile)
	outfile.close();		

#pdb.set_trace()
print (bfs(d, fword, sword))				#USING BREADTH FIRST SEARCH FOR GETTING THE SHORTEST PATH FOR CONVERTING
#for x, val in enumerate(d):
#	print (x, val ,"->", d[val], "\n")
  