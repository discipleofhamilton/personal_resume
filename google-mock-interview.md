mQuestion 1

Suppose you have a graph of Google's organizational structure where:
Each node N corresponds to a person
If N reports to M (i.e. M is N's boss), M is the parent of N
If P reports to N (i.e. N is P's boss), P is the child of N

At Google, someone's "employee score" is the total number of reports (including themselves).

Write a function to compute anyone's employee score.

Example:

```
alice (4)
|               
bob (3)       
/            \ 
charlie (1) dave (1)
```
Class Node:
	Name
	Score
	Children:list[node]
	Parent: nod

Nodes: Dict[str, Node]
	
Def getScore(target: str) -> int:
	Target_node = nodes.get(target) 
	
           score = 0

	For n in target_node.child:
	   Score += getScore(n.name)
    Return score+1

Space: O(N), worst case when linked list
Time: O(N), worst case input is the root




Followup #1

Suppose the graph has already been precomputed with everyone's employee score. Write a function to recompute these employee scores should someone move teams.

Assume that if an individual moves teams, their reports do not move with them, and simply start directly reporting to an individual's former boss. Assume that a function to perform the actual team movement already exists, and the new children / parent of this node have been updated accordingly.

```
…
alice (4 -> 3)
|               
bob (3)       
/            \ 
charlie (1) dave (1)
Old_team : tree
…
|
David(1 -> 2)
|
bob(1)
```
New_team : tree

Nodes: Dict[str, Node]

Def updateScore(target:str, new_boss:str):
	
	Target_nodes = nodes.get(target)

	L = targetnodes.parent
	While l:
		l.score -=1
		L = l.parent

	New_bossnode = nodes.get(new_boss)
	L  = new_bossnode
	While l:
		l.score+=1
		L = l.parent

Time: O(Depth), worst case O(N) when linked list
Space: O(1), no recursive call


Followup #2

Same as follow up #1, but instead of an individual moving teams write a function to recompute employee scores in the event of a reorganization: that is, have an employee and everyone underneath them move teams.

```
alice (4 -> 1)
|               
bob (3)       
/            \ 
charlie (1) dave (1)

David(1 -> 4)
|
bob(3)
|        \
charlie (1) dave (1)
```

Def updatescore(target:str, new_boss:str):
	
	Targetnodes = nodes.get(target)

	L = targetnodes.parent
	While l:
		l.score -=Targetnodes.score
		L = l.parent

	New_bossnode = nodes.get(new_boss)
	L  = new_bossnode
	While l:
		l.score+=Targetnodes.score
		L = l.parent