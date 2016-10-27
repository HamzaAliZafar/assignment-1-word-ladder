graph=[];

def equallen(data):						#getting values equal to the length of fword
	for val in data:
		if (len(fword) == len(val)):
			graph.append(val)
	return graph
	
def lettermatch(a,b):						#keeping only those that are at one letter difference
	temp=0;
	for letter,lett in zip(a,b):
			if (letter == lett and a!=b):
				temp+=1
				if ((len(b)-1) == temp):
					#pdb.set_trace()
					return True;
	return False;

										#taken from stackoverflow
def bfs(graph, start, end):
    
	# maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
		# enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

	
import json
import pdb
from collections import defaultdict

fword = input('Enter first word: ')
sword = input('Enter second word: ')

while(len(fword) != len(sword)):
	print("Length not equal: ")
	fword = input('Enter first word: ')
	sword = input('Enter second word: ')

fword = fword.upper();
sword = sword.upper();
	
with open('Dictionary.json') as data_file:	
	data = json.load(data_file)
data_file.close();

d = defaultdict(list)

graph = equallen(data)

for j,k in enumerate(graph):
	for l,n in enumerate(graph):
		if (lettermatch(k,n)):
			d[k].append(n);

#pdb.set_trace()
print (bfs(d, fword, sword))
#for x, val in enumerate(d):
#	print (x, val ,"->", d[val], "\n")
  