# Data Description

`${n}` represents the number of vertices in the graph, between 2 and 10, inclusive.

## 1. Raw graph data: `data/01_g6/graph${n}.g6`

All non-isomorphic simple graphs with 2-10 vertices (including disconnected ones).

Downloaded from http://users.cecs.anu.edu.au/~bdm/data/graphs.html

Example:

```
$ head data/01_g6/graph4.g6
C?
CC
CE
CF
CQ
CT
CU
CV
C]
C^
```


## 2. Decoded graph data: `data/02_decoded/graph${n}.txt`

Decoded graph data by the `showg` program found here http://users.cecs.anu.edu.au/~bdm/data/formats.html

Example:

```
$ head data/02_decoded/graph4.txt

Graph 1, order 4.
  0 : ;
  1 : ;
  2 : ;
  3 : ;

Graph 2, order 4.
  0 : 3;
  1 : ;
```


## 3. Input data for Tutte polynomial computation: `data/03_input/graph${n}.txt`

Formatted edge list data for the tuttepoly program found here https://homepages.ecs.vuw.ac.nz/~djp/tutte/

In this step, the trivial graph (graph with no edges) is removed from the list.

Example:

```
$ head data/03_input/graph4.dat
0--3
0--3,1--3
0--3,1--3,2--3
0--2,1--3
0--2,0--3,2--3
0--2,0--3,1--3
0--2,0--3,1--3,2--3
0--2,0--3,1--2,1--3
0--2,0--3,1--2,1--3,2--3
0--1,0--2,0--3,1--2,1--3,2--3
```


## 4. Tutte polynomial computation result: `data/04_output/graph${n}.out`

Output of the tuttepoly program.

Example:

```
$ head data/04_output/graph4.out
G[1] := {0--1}
TP[1] := 1*x :
G[2] := {0--2,1--2}
TP[2] := 1*x^2 :
G[3] := {0--3,1--3,2--3}
TP[3] := 1*x^3 :
G[4] := {0--2,1--3}
TP[4] := 1*x^2 :
G[5] := {0--1,0--2,1--2}
TP[5] := 1*y + 1*x + 1*x^2 :
```

## 5. Vectorized Tutte polynomial coefficients: `data/05_vector/graph${n}.csv`

t_ij = v_{i+j*n}

where t is the coefficient matrix of the Tutte polynomial (i: x's degree, j: y's degree),
and v is the resulting vector.

The result for the trivial graph for each n has been inserted into the first line.

Example:

```
$ head data/05_vector/vector4.csv
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0
0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0
0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0
0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0
0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0
0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0
0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0
0,1,2,1,1,2,0,0,1,0,0,0,0,0,0,0
```

### 6. Graph invariant data 

Example:

```
$ head data/06_invariant/graph4.cc.csv
4
3
2
1
2
2
1
1
1
1
```

### 7. Filter definition data

Example: Indexes of the connected graphs with n=4

```
$ head data/07_filter/graph4_conn.txt
3
6
7
8
9
10
```
