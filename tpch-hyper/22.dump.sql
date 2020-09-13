create temp view q22_1 as (
  select substring(c_phone, 1, 2) as phone, sum(c_acctbal), count(*)
    from customer
   where c_acctbal > 0.0
   group by phone
);

\copy (select * from q22_1) to 'q22_1.tbl' delimiter '|';

create temp view q22_2 as (
  select substring(c_phone, 1, 2) as phone, c_acctbal
    from customer
   where not exists (select * from orders where o_custkey = c_custkey)
);

\copy (select * from q22_2) to 'q22_2.tbl' delimiter '|';
