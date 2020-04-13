# tutte-polyn
Research on the Tutte polynomials.




# Data Preparation

### (1) Create directories

```
mkdir bin
mkdir -p data/g6 data/decoded data/input data/output data/vector
```

### (2) Download graph data

http://users.cecs.anu.edu.au/~bdm/data/graphs.html

- Download the files for "Simple graphs: 2-10 vertices" to `data/g6`
- Extract `graph10.g6.gz` by `gunzip data/g6/graph.g6.gz`

### (3) Download **showg** program

http://users.cecs.anu.edu.au/~bdm/data/formats.html

- Download an executable for your environment.
- Place the file as `bin/showg`
- Set the execute permission to the file, if needed.

### (4) Decode g6 format

```
for i in 2 3 4 5 6 7 8 9 10; do ./bin/showg ./data/g6/graph${i}.g6 ./data/decoded/graph${i}.txt; done
```

### (5) Download and build **tuttepoly** program

https://homepages.ecs.vuw.ac.nz/~djp/tutte/#download

- Download the latest `tuttepoly-v*.*.*.tgz`.
- Move to `/tmp`
- Extract file by `tar zxf ~/Downloads/tuttepoly-v*.*.*.tgz`

```
cd /tmp/tuttepoly-v*.*.*/
./configure
make
```

- Copy program `/tmp/tuttepoly-v*.*.*/tutte/tutte` to `{this directory}/bin/`

### (6) Create input for **tuttepoly** program

```
for i in 2 3 4 5 6 7 8 9 10; do ./scripts/conv_data.py ./data/decoded/graph${i}.txt > ./data/input/graph${i}.dat; done
```

### (7) Run **tuttepoly** program

```
for i in 2 3 4 5 6 7 8; do ./bin/tutte ./data/input/graph${i}.dat > ./data/output/graph${i}.out; done
./bin/tutte ./data/input/graph9.dat > ./data/output/graph9.out
./bin/tutte -c8G ./data/input/graph9.dat > ./data/output/graph9.out
```

### (8) Create vector data

```
for i in 2 3 4 5 6 7 8; do ./scripts/vectorize.py -n $i ./data/output/graph${i}.out > ./data/vector/vector${i}.txt; done
./scripts/vectorize.py -n 9 ./data/output/graph9.out > ./data/vector/vector9.txt
./scripts/vectorize.py -n 10 ./data/output/graph10.out > ./data/vector/vector10.txt
```

### (9) Convert vector data into CSV

```
for i in {2..10}; do ./scripts/vec_to_csv.py ./data/vector/vector${i}.txt > ./data/vector/vector${i}.csv; done
```

## Compute Graph Invariants

### (1) Number of Edges

```
mkdir data/inv
for i in {2..10}; do ./scripts/invariant.py -n $i -t num-edges ./data/input/graph$i.dat > ./data/inv/graph$i.num-edges.csv; done
```

< 6 min

### (2) Number of Connected Components

```
for i in {2..10}; do ./scripts/invariant.py -n $i -t cc ./data/input/graph$i.dat > ./data/inv/graph$i.cc.csv; done
```

< 7 min



## References

- [Ball mapper: a shape summary for topological data analysis](https://arxiv.org/pdf/1901.07410.pdf)


