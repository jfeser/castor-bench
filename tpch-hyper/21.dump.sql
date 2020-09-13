CREATE temp VIEW q21 AS (
  SELECT
    n_name,
    s_name,
    count(*) as numwait
    FROM
      lineitem as l1,
      supplier,
      nation,
      orders
   WHERE
     o_orderstatus = 'F' and
     l1.l_receiptdate > l1.l_commitdate
     and exists (select * from lineitem
                  where l_orderkey = l1.l_orderkey
                    and not (l_suppkey = l1.l_suppkey))
     and not exists (select * from lineitem
                      where l_orderkey = l1.l_orderkey
                        and not (l_suppkey = l1.l_suppkey)
                        and l_receiptdate > l_commitdate)
     and s_nationkey = n_nationkey
     and s_suppkey = l1.l_suppkey
     and o_orderkey = l1.l_orderkey
   group by n_name, s_name
);

\copy (select * from q21) to 'q21.tbl' delimiter '|';
