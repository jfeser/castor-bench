SHELL:=/bin/bash
COMPILE_PATH=../../castor/bin/compile.exe
COMPILE=dune exec --no-build $(COMPILE_PATH) -- 
CFLAGS=-v
TIME_CMD=/usr/bin/time
TIME_PER_BENCH=1

compile: 1-gold 2-gold 3-no-gold 4-gold 5-no-gold 6-gold 7-gold 8-gold 9-gold 10-no-gold 11-no-gold 12-gold 14-gold 15-gold 16-no-gold 17-gold 18-gold 19-gold
.PHONY: compile


run: 1-gold.csv 2-gold.csv 3-no-gold.csv 4-gold.csv 5-no-gold.csv 6-gold.csv 7-gold.csv 8-gold.csv 9-gold.csv 10-no-gold.csv 11-no-gold.csv 12-gold.csv 14-gold.csv 15-gold.csv 16-no-gold.csv 17-gold.csv 18-gold.csv 19-gold.csv
.PHONY: run


time: 1-gold.time 2-gold.time 3-no-gold.time 4-gold.time 5-no-gold.time 6-gold.time 7-gold.time 8-gold.time 9-gold.time 10-no-gold.time 11-no-gold.time 12-gold.time 14-gold.time 15-gold.time 16-no-gold.time 17-gold.time 18-gold.time 19-gold.time
.PHONY: time


validate: analysis_1-opt.csv.log analysis_2-opt.csv.log analysis_3-no-opt.csv.log analysis_4-opt.csv.log analysis_5-no-opt.csv.log analysis_6-opt.csv.log analysis_7-opt.csv.log analysis_8-opt.csv.log analysis_9-opt.csv.log analysis_10-no-opt.csv.log analysis_11-no-opt.csv.log analysis_12-opt.csv.log analysis_14-opt.csv.log analysis_15-opt.csv.log analysis_16-no-opt.csv.log analysis_17-opt.csv.log analysis_18-opt.csv.log analysis_19-opt.csv.log
.PHONY: validate


1-gold: ../../castor/bench/tpch/1-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param0:int' $< > $@/compile.log 2>&1


1-gold.csv:
	./1-gold/scanner.exe -p 1-gold/data.bin '90' > $@


1-gold.time:
	./1-gold/scanner.exe -t $(TIME_PER_BENCH) 1-gold/data.bin '90' > $@
	$(TIME_CMD) -v ./1-gold/scanner.exe -t $(TIME_PER_BENCH) 1/data.bin '90' 2> 1-gold.mem > /dev/null


analysis_1.log:
	../bin/validate.py 1 True 1.csv
    

2-gold: ../../castor/bench/tpch/2-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param1:int' -p 'param2:string' -p 'param3:string' $< > $@/compile.log 2>&1


2-gold.csv:
	./2-gold/scanner.exe -p 2-gold/data.bin '15' 'BRASS' 'EUROPE' > $@


2-gold.time:
	./2-gold/scanner.exe -t $(TIME_PER_BENCH) 2-gold/data.bin '15' 'BRASS' 'EUROPE' > $@
	$(TIME_CMD) -v ./2-gold/scanner.exe -t $(TIME_PER_BENCH) 2/data.bin '15' 'BRASS' 'EUROPE' 2> 2-gold.mem > /dev/null


analysis_2.log:
	../bin/validate.py 2 True 2.csv
    

3-no-gold: ../../castor/bench/tpch/3-no-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param0:string' -p 'param1:date' $< > $@/compile.log 2>&1


3-no-gold.csv:
	./3-no-gold/scanner.exe -p 3-no-gold/data.bin 'BUILDING' '1995-03-15' > $@


3-no-gold.time:
	./3-no-gold/scanner.exe -t $(TIME_PER_BENCH) 3-no-gold/data.bin 'BUILDING' '1995-03-15' > $@
	$(TIME_CMD) -v ./3-no-gold/scanner.exe -t $(TIME_PER_BENCH) 3-no/data.bin 'BUILDING' '1995-03-15' 2> 3-no-gold.mem > /dev/null


analysis_3-no.log:
	../bin/validate.py 3-no False 3-no.csv
    

4-gold: ../../castor/bench/tpch/4-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param1:date' $< > $@/compile.log 2>&1


4-gold.csv:
	./4-gold/scanner.exe -p 4-gold/data.bin '1993-07-01' > $@


4-gold.time:
	./4-gold/scanner.exe -t $(TIME_PER_BENCH) 4-gold/data.bin '1993-07-01' > $@
	$(TIME_CMD) -v ./4-gold/scanner.exe -t $(TIME_PER_BENCH) 4/data.bin '1993-07-01' 2> 4-gold.mem > /dev/null


analysis_4.log:
	../bin/validate.py 4 True 4.csv
    

5-no-gold: ../../castor/bench/tpch/5-no-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param0:string' -p 'param1:date' $< > $@/compile.log 2>&1


5-no-gold.csv:
	./5-no-gold/scanner.exe -p 5-no-gold/data.bin 'ASIA' '1994-01-01' > $@


5-no-gold.time:
	./5-no-gold/scanner.exe -t $(TIME_PER_BENCH) 5-no-gold/data.bin 'ASIA' '1994-01-01' > $@
	$(TIME_CMD) -v ./5-no-gold/scanner.exe -t $(TIME_PER_BENCH) 5-no/data.bin 'ASIA' '1994-01-01' 2> 5-no-gold.mem > /dev/null


analysis_5-no.log:
	../bin/validate.py 5-no False 5-no.csv
    

6-gold: ../../castor/bench/tpch/6-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param0:date' -p 'param1:fixed' -p 'param2:int' $< > $@/compile.log 2>&1


6-gold.csv:
	./6-gold/scanner.exe -p 6-gold/data.bin '1994-01-01' '0.06' '24' > $@


6-gold.time:
	./6-gold/scanner.exe -t $(TIME_PER_BENCH) 6-gold/data.bin '1994-01-01' '0.06' '24' > $@
	$(TIME_CMD) -v ./6-gold/scanner.exe -t $(TIME_PER_BENCH) 6/data.bin '1994-01-01' '0.06' '24' 2> 6-gold.mem > /dev/null


analysis_6.log:
	../bin/validate.py 6 True 6.csv
    

7-gold: ../../castor/bench/tpch/7-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param0:string' -p 'param1:string' $< > $@/compile.log 2>&1


7-gold.csv:
	./7-gold/scanner.exe -p 7-gold/data.bin 'FRANCE' 'GERMANY' > $@


7-gold.time:
	./7-gold/scanner.exe -t $(TIME_PER_BENCH) 7-gold/data.bin 'FRANCE' 'GERMANY' > $@
	$(TIME_CMD) -v ./7-gold/scanner.exe -t $(TIME_PER_BENCH) 7/data.bin 'FRANCE' 'GERMANY' 2> 7-gold.mem > /dev/null


analysis_7.log:
	../bin/validate.py 7 True 7.csv
    

8-gold: ../../castor/bench/tpch/8-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param1:string' -p 'param2:string' -p 'param3:string' $< > $@/compile.log 2>&1


8-gold.csv:
	./8-gold/scanner.exe -p 8-gold/data.bin 'BRAZIL' 'AMERICA' 'ECONOMY ANODIZED STEEL' > $@


8-gold.time:
	./8-gold/scanner.exe -t $(TIME_PER_BENCH) 8-gold/data.bin 'BRAZIL' 'AMERICA' 'ECONOMY ANODIZED STEEL' > $@
	$(TIME_CMD) -v ./8-gold/scanner.exe -t $(TIME_PER_BENCH) 8/data.bin 'BRAZIL' 'AMERICA' 'ECONOMY ANODIZED STEEL' 2> 8-gold.mem > /dev/null


analysis_8.log:
	../bin/validate.py 8 True 8.csv
    

9-gold: ../../castor/bench/tpch/9-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param1:string' $< > $@/compile.log 2>&1


9-gold.csv:
	./9-gold/scanner.exe -p 9-gold/data.bin 'green' > $@


9-gold.time:
	./9-gold/scanner.exe -t $(TIME_PER_BENCH) 9-gold/data.bin 'green' > $@
	$(TIME_CMD) -v ./9-gold/scanner.exe -t $(TIME_PER_BENCH) 9/data.bin 'green' 2> 9-gold.mem > /dev/null


analysis_9.log:
	../bin/validate.py 9 True 9.csv
    

10-no-gold: ../../castor/bench/tpch/10-no-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param0:date' $< > $@/compile.log 2>&1


10-no-gold.csv:
	./10-no-gold/scanner.exe -p 10-no-gold/data.bin '1993-10-01' > $@


10-no-gold.time:
	./10-no-gold/scanner.exe -t $(TIME_PER_BENCH) 10-no-gold/data.bin '1993-10-01' > $@
	$(TIME_CMD) -v ./10-no-gold/scanner.exe -t $(TIME_PER_BENCH) 10-no/data.bin '1993-10-01' 2> 10-no-gold.mem > /dev/null


analysis_10-no.log:
	../bin/validate.py 10-no False 10-no.csv
    

11-no-gold: ../../castor/bench/tpch/11-no-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param1:string' -p 'param2:fixed' $< > $@/compile.log 2>&1


11-no-gold.csv:
	./11-no-gold/scanner.exe -p 11-no-gold/data.bin 'GERMANY' '0.0001' > $@


11-no-gold.time:
	./11-no-gold/scanner.exe -t $(TIME_PER_BENCH) 11-no-gold/data.bin 'GERMANY' '0.0001' > $@
	$(TIME_CMD) -v ./11-no-gold/scanner.exe -t $(TIME_PER_BENCH) 11-no/data.bin 'GERMANY' '0.0001' 2> 11-no-gold.mem > /dev/null


analysis_11-no.log:
	../bin/validate.py 11-no False 11-no.csv
    

12-gold: ../../castor/bench/tpch/12-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param1:string' -p 'param2:string' -p 'param3:date' $< > $@/compile.log 2>&1


12-gold.csv:
	./12-gold/scanner.exe -p 12-gold/data.bin 'MAIL' 'SHIP' '1994-01-01' > $@


12-gold.time:
	./12-gold/scanner.exe -t $(TIME_PER_BENCH) 12-gold/data.bin 'MAIL' 'SHIP' '1994-01-01' > $@
	$(TIME_CMD) -v ./12-gold/scanner.exe -t $(TIME_PER_BENCH) 12/data.bin 'MAIL' 'SHIP' '1994-01-01' 2> 12-gold.mem > /dev/null


analysis_12.log:
	../bin/validate.py 12 True 12.csv
    

14-gold: ../../castor/bench/tpch/14-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param1:date' $< > $@/compile.log 2>&1


14-gold.csv:
	./14-gold/scanner.exe -p 14-gold/data.bin '1995-09-01' > $@


14-gold.time:
	./14-gold/scanner.exe -t $(TIME_PER_BENCH) 14-gold/data.bin '1995-09-01' > $@
	$(TIME_CMD) -v ./14-gold/scanner.exe -t $(TIME_PER_BENCH) 14/data.bin '1995-09-01' 2> 14-gold.mem > /dev/null


analysis_14.log:
	../bin/validate.py 14 True 14.csv
    

15-gold: ../../castor/bench/tpch/15-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param1:date' $< > $@/compile.log 2>&1


15-gold.csv:
	./15-gold/scanner.exe -p 15-gold/data.bin '1996-01-01' > $@


15-gold.time:
	./15-gold/scanner.exe -t $(TIME_PER_BENCH) 15-gold/data.bin '1996-01-01' > $@
	$(TIME_CMD) -v ./15-gold/scanner.exe -t $(TIME_PER_BENCH) 15/data.bin '1996-01-01' 2> 15-gold.mem > /dev/null


analysis_15.log:
	../bin/validate.py 15 True 15.csv
    

16-no-gold: ../../castor/bench/tpch/16-no-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param1:string' -p 'param2:string' -p 'param3:int' -p 'param4:int' -p 'param5:int' -p 'param6:int' -p 'param7:int' -p 'param8:int' -p 'param9:int' -p 'param10:int' $< > $@/compile.log 2>&1


16-no-gold.csv:
	./16-no-gold/scanner.exe -p 16-no-gold/data.bin 'Brand#45' 'MEDIUM POLISHED' '49' '14' '23' '45' '19' '3' '36' '9' > $@


16-no-gold.time:
	./16-no-gold/scanner.exe -t $(TIME_PER_BENCH) 16-no-gold/data.bin 'Brand#45' 'MEDIUM POLISHED' '49' '14' '23' '45' '19' '3' '36' '9' > $@
	$(TIME_CMD) -v ./16-no-gold/scanner.exe -t $(TIME_PER_BENCH) 16-no/data.bin 'Brand#45' 'MEDIUM POLISHED' '49' '14' '23' '45' '19' '3' '36' '9' 2> 16-no-gold.mem > /dev/null


analysis_16-no.log:
	../bin/validate.py 16-no False 16-no.csv
    

17-gold: ../../castor/bench/tpch/17-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param0:string' -p 'param1:string' $< > $@/compile.log 2>&1


17-gold.csv:
	./17-gold/scanner.exe -p 17-gold/data.bin 'Brand#23' 'MED BOX' > $@


17-gold.time:
	./17-gold/scanner.exe -t $(TIME_PER_BENCH) 17-gold/data.bin 'Brand#23' 'MED BOX' > $@
	$(TIME_CMD) -v ./17-gold/scanner.exe -t $(TIME_PER_BENCH) 17/data.bin 'Brand#23' 'MED BOX' 2> 17-gold.mem > /dev/null


analysis_17.log:
	../bin/validate.py 17 True 17.csv
    

18-gold: ../../castor/bench/tpch/18-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param1:int' $< > $@/compile.log 2>&1


18-gold.csv:
	./18-gold/scanner.exe -p 18-gold/data.bin '300' > $@


18-gold.time:
	./18-gold/scanner.exe -t $(TIME_PER_BENCH) 18-gold/data.bin '300' > $@
	$(TIME_CMD) -v ./18-gold/scanner.exe -t $(TIME_PER_BENCH) 18/data.bin '300' 2> 18-gold.mem > /dev/null


analysis_18.log:
	../bin/validate.py 18 True 18.csv
    

19-gold: ../../castor/bench/tpch/19-gold.txt
	mkdir -p $@
	$(COMPILE) $(CFLAGS) -o $@ -p 'param0:string' -p 'param1:string' -p 'param2:string' -p 'param3:fixed' -p 'param4:fixed' -p 'param5:fixed' $< > $@/compile.log 2>&1


19-gold.csv:
	./19-gold/scanner.exe -p 19-gold/data.bin 'Brand#12' 'Brand#23' 'Brand#34' '1.0' '10.0' '20.0' > $@


19-gold.time:
	./19-gold/scanner.exe -t $(TIME_PER_BENCH) 19-gold/data.bin 'Brand#12' 'Brand#23' 'Brand#34' '1.0' '10.0' '20.0' > $@
	$(TIME_CMD) -v ./19-gold/scanner.exe -t $(TIME_PER_BENCH) 19/data.bin 'Brand#12' 'Brand#23' 'Brand#34' '1.0' '10.0' '20.0' 2> 19-gold.mem > /dev/null


analysis_19.log:
	../bin/validate.py 19 True 19.csv
    

.PHONY: clean
clean:
	rm -rf */ *.csv *.mem *.time analysis*log

