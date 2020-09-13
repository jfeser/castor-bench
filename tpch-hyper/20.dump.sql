CREATE temp VIEW q20_1 AS (
  SELECT
    n_name,
    s_suppkey,
    s_name,
    s_address
    FROM
      supplier,
      nation
   WHERE
     s_nationkey = n_nationkey
);

\copy (select * from q20_1) to 'q20_1.tbl' delimiter '|';

CREATE temp VIEW q20_2 AS (
  SELECT
    ps_partkey,
    ps_suppkey,
    ps_availqty,
    ps_supplycost,
    ps_comment
    FROM
      partsupp
);

\copy (select * from q20_2) to 'q20_2.tbl' delimiter '|';

CREATE temp VIEW q20_3 AS (
  SELECT
    l_partkey,
    l_suppkey,
    l_shipdate,
    sum(l_quantity)
    FROM
        lineitem
   group by l_partkey, l_suppkey, l_shipdate
);

\copy (select * from q20_3) to 'q20_3.tbl' delimiter '|';

CREATE temp VIEW q20_4 AS (
  SELECT
    p_partkey,
    p_name,
    p_mfgr,
    p_brand,
    p_type,
    p_size,
    p_container,
    p_retailprice,
    p_comment
    FROM
        part
);

\copy (select * from q20_4) to 'q20_4.tbl' delimiter '|';
