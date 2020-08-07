# Getting Started

The artifact is packaged as a Docker container. Follow the instructions here
(https://docs.docker.com/get-started/) to get Docker set up on your machine.

The default username/password is ubuntu/ubuntu.

## Importing the image

To import the container image, run
```
docker import castor-docker.tar.gz castor
```

## Starting a shell

Start the container with `docker run -it -v $(pwd):/castor castor:latest bash
-l`. Start PostgreSQL with `sudo service postgresql start` (password `ubuntu`).

## Compiling

In `/castor/`, run `dune build @install`.

## Configuring

Castor is configured through environment variables. Run `source
castor/config-docker-redshift.sh` to configure Castor to use Redshift as its
backing database. Running `source castor/config-docker-postgres.sh` will select
Postgres instead. Redshift is much faster and is suggested for running the
benchmarks.

## Running the test suite

In `/castor/`, run `dune runtest`. There should be no output. It's important to
source one of the configuration scripts before running the tests.

# Evaluation

The artifact contains the scripts for reproducing Tables 1 and 2 in the paper,
which contain the main performance claims. 

Table 1 contains two benchmark configurations:

1. Hyper with manually combined and specialized datasets
2. Castor with combined optimized queries

Table 2 contains four different benchmark configurations:

1. Vanilla Hyper
2. Hyper with manually specialized datasets
3. Expert generated Castor queries
4. Optimizer generated Castor queries
    
## Structure of the artifact

 - `castor/`: the Castor compiler and helper programs
 - `castor-opt/`: the Castor optimizer
 - `castor-bench/`: benchmarks and supporting scripts
 - `castor-bench/tpch/`: TPC-H queries, translations of these queries into the
   relational fragment of the layout algebra, scripts for generating the
   expected TPC-H output
 - `combinat/`, `genhash/`, `sqlgg/`, `ocaml-cmph/`: helper libraries
 
## Table 1

The steps for reproducing the Castor numbers in Table 1 are:
1. `cd /castor/castor-bench/tpch-multi`
2. Generate the makefile with `./mk_make.py queries.json > Makefile`.
2. Generate the combined queries with `make queries`.
3. Compile the queries with `make compile`.
4. Run the queries with `make run`.
5. Time the queries with `make time`.
6. Generate CSV containing the results with `../bin/results.py .`.

The scripts and queries for Hyper are in `castor-bench/tpch-hyper-paper-version`.

## Table 2

### Hyper default

The numbers we report in the paper come from our run of the Hyper benchmark
suite, which we can't distribute.

### Hyper specialized queries

The scripts for running Hyper on manually specialized TPC-H queries are in
`castor-bench/tpch-hyper-paper-version`. We can't distribute the Hyper binaries,
but we have provided the log output from the run of Hyper that we reported in
the paper.

### Castor expert queries

The steps for benchmarking the expert queries are:

1. Generate the makefile with `./mk_make.py > Makefile`
1. Generate the queries from their specifications by running `make gen`.
2. Compile the queries by running `make compile`.
3. Run the compiled queries with `make run`.
5. Time the queries with `make time`.
4. Ensure the TPC-H expected outputs are generated by running `./mk_make >
   Makefile; make` in `castor-bench/tpch`.
4. Validate the query outputs with `make validate`.
5. Generate CSV containing the results with `../bin/results.py .`

### Castor optimizer queries

The steps for benchmarking the optimizer generated queries are:

1. Generate the makefile with `./mk_make.py > Makefile`
2. Run the optimizer with `make opt`. This step is slow. Consider using the `-j`
   flag for parallelism. The optimizer runs for a fixed time, saving the best
   query that it has found. The runtime of the optimizer can be configured by
   modifying the argument to `-timeout` in `OPT_FLAGS` (the argument is in
   seconds).
2. Compile the queries by running `make compile`.
3. Run the compiled queries with `make run`.
4. Ensure the TPC-H expected outputs are generated by running `./mk_make >
   Makefile; make` in `castor-bench/tpch`.
4. Validate the query outputs with `make validate`.
5. Generate CSV containing the results with `../bin/results.py .`

#### Optimizer non-determinism
    
The optimizer uses MCMC, so different runs of the optimizer may return queries
that perform differently. We've provided the logs and results from the optimizer
run that we reported in the paper in
`castor-bench/tpch-optimizer-paper-version`.
