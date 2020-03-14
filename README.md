# tutte-polyn
Research on the Tutte polynomials.




# Data Preparation

### (1) Create directories

```
mkdir bin
mkdir -p data/g6 data/decoded data/input data/output
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

