So this code  is about finding the shortest path between tasks using called the A-star algorithm 

What the code is doing, 
start with a bunch of tasks like ‘Start, Design,  Procure,’ all the way to 'Release'. Each task is a node, and we connect them with edges, which are paths that have costs , like time or effort to move from one task to another. 

Paano ba gumagana ang  A* algorithm , 
To find the best path, we use A-star. It’s smart because it doesn’t just look at how far you’ve gone, it also guesses how far you still need to go. That prediction po is called a heuristic , sa code it’s just the straight-line distance to the goal. 

We say 'g of n' — that means the cost so far to get to a node 'n'." 

Then, 'h of n' — that means the estimated cost from node 'n' to the goal." 

Finally, 'f of n' equals 'g of n' plus 'h of n' — that’s the total estimated cost of the path through node 'n'." 

* The algorithm always picks the path with the smallest 'f of n' value.

 

How it works step by step: 
* We start at Start 
* We check all connected tasks like Design and Procure 

* We calculate g, h, and f for each task 

* We always go to the task with the smallest f of n 

* Once we reach Release, we stop and trace back the best path 

Pagkatapos makita yung best path, ginagamit natin yung matplotlib para iguhit:
* All the task as points  
* arrows  showing connections 
* Yung shortest path naka-highlight sa pula 
* Tapos sa tabi ng bawat task, makikita yung values ng g(n), h(n), at f(n) 

In the end: 
The program tells us the shortest path, like: 
 Start → Design → ImplementB → Integrate → Test → Release 
 and shows the total cost to follow that path. 

 

* Ginamit ko yung A-star kasi mas mabilis siya kaysa sa checking every possible path. Pinag sasama sama niya yung actual cost  and an estimate of the remaining cost to pick the best direction. The code finds the best path and shows it visually with labels for g, h, and f, so we can see exactly how it worked.
