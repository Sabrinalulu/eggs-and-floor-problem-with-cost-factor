# eggs-and-floor-problem-with-cost-factor
The solution of eggs and floors problem may be a way to test the quality of a mobile phone (e.g., bump-resistance). After adding the cost factor, we can also compute the minimum cost of the testing. If the final cost is affordable, this throwing method is feasible. If not, we had better change another way to test. 

## Problem Outline
You are given n eggs and a m floor building.  You need to figure out the highest floor an egg can be dropped without breaking, assuming that (i) all eggs are identical, (ii) if an egg breaks after being dropped from one floor, then the egg will also break if dropped from all higher floors, (iii) if an egg does not break after being thrown from a certain floor, it retains all of its strength and you can continue to use that egg, and (iiii) if an egg break, it costs 5 extra dollars, otherwise it cost 10 dollars. Your goal is to minimize the cost of throws. From which floor do you drop the first egg? 

## Solution
Use dynamic programming method to solve this problem. With the base case (minimum cost of given one egg or one floor) and recurrence relation, we derive the final outcome to avoid the overlapping.

### Notation
C[y][x] means the minimum cost when y floors and x eggs are given. Basically, if y=1, C[1][x]=15(as only one test is needed,and the worst situation is that egg is broken). if x=1, C[y][1]=y*10+5(to consider the worst situation: we throw the egg from the bottom level, and the egg is broken at the top level) .

### Optimality
The operation starts from bottom to top of the building to find the optimal of each floor. So, adding an argument to get the minimum cost from the top level shuold be optiaml.

### Recurrence relation
We can suppose z to represent the floor we judge, and gain minimum cost of worst situation by 
C[y][x]= min( C[y][x], 10 + max(C[z-1][x-1]+5,C[y-z][x]) ).
(if(z=1): C[y][x]= 10+ max( C[z-1][x-1]+5, C[y-z][x]) ).
