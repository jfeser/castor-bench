create table q20_1 (
  n_name char(25) not null,
  s_suppkey integer not null,
  s_name char(25) not null,
  s_address varchar(40) not null
  );

CREATE INDEX q20_1_idx ON q20_1 (n_name);

create table q20_2 (
  ps_partkey integer not null,
  ps_suppkey integer not null,
  ps_availqty integer not null,
  ps_supplycost decimal(12,2) not null,
  ps_comment varchar(199) not null
);

CREATE INDEX q20_2_idx ON q20_2 (ps_suppkey);

create table q20_3 (
  l_partkey integer not null,
  l_suppkey integer not null,
  l_shipdate date not null,
  tot_quantity decimal(12,2) not null
);

CREATE INDEX q20_3_idx ON q20_3 (l_partkey, l_suppkey, l_shipdate);

create table q20_4 (
  p_partkey integer not null,
  p_name varchar(55) not null,
  p_mfgr char(25) not null,
  p_brand char(10) not null,
  p_type varchar(25) not null,
  p_size integer not null,
  p_container char(10) not null,
  p_retailprice decimal(12,2) not null,
  p_comment varchar(23) not null
);

CREATE INDEX q20_4_idx ON q20_4 (p_partkey);
