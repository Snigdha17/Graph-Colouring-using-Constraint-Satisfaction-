# Graph-Colouring-using-Constraint-Satisfaction-

This code solves the Graph Colouring problem using three algorithms:
1. Depth-First Search
2. Depth-First Search with Backtracking
3. Min-conflicts algorithm

### The aim of this project is to understand contraint satisfaction and understand how this algorithm is applied to solve problems.


The program can be compiled and run as follows:

1. dfsb.py runs in two modes: 
> * Plain DFS-B 
> * DFS-B with variable, value ordering and AC3 for contraint propogation. 

> To run the program on the command line:
> 
>	python dfsb.py input_file output_file mode_flag
> 
>	where mode_flag can be either 0 or 1
> 
> example: dfsb.py backtrack_easy.txt output.txt 0

2. minconflicts.py runs the MinConflicts local search algorithm, and effectively avoids getting stuck in local minima using random restarts. To run the program on the command line:

> python minconflicts.py input_file output_file
> 
> example: python minconflicts.py minconflicts_easy output.txt

The format of the input is as follows:

There are N variables numbered 0 to N-1 and M constraints connecting them. There are K possible colors for each of the variables, so the domain for all variables is the same. In the input, N,M,K are entered first. Then on each separate line variables U and V are provided. There will be M lines following the first line

> N  M  K 
> 
> v0 u0  *variables v0 and u0 should not have the same color*
> 
> v1 u1
> 
> ... 
> 
> ...
> 
> vM-1   uM-1



