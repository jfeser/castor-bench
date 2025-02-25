create temp view q19_1 as (select l_quantity, l_extendedprice, l_discount, p_brand from lineitem, part where l_shipinstruct = 'DELIVER IN PERSON' and (l_shipmode = 'AIR' or l_shipmode = 'AIR REG') and p_size >= 1 and p_size <= 5 and (p_container = 'SM CASE' or p_container = 'SM BOX' or p_container = 'SM PACK' or p_container = 'SM PKG') and p_partkey = l_partkey);

\copy (select * from q19_1) to 'q19_1.tbl' delimiter '|';

create temp view q19_2 as (select l_quantity, l_extendedprice, l_discount, p_brand from lineitem, part where l_shipinstruct = 'DELIVER IN PERSON' and (l_shipmode = 'AIR' or l_shipmode = 'AIR REG') and p_size >= 1 and p_size <= 10 and (p_container = 'MED BAG' or p_container = 'MED BOX' or p_container = 'MED PKG' or p_container = 'MED PACK') and p_partkey = l_partkey);

\copy (select * from q19_2) to 'q19_2.tbl' delimiter '|';

create temp view q19_3 as (select l_quantity, l_extendedprice, l_discount, p_brand from lineitem, part where l_shipinstruct = 'DELIVER IN PERSON' and (l_shipmode = 'AIR' or l_shipmode = 'AIR REG') and p_size >= 1 and p_size <= 15 and (p_container = 'LG CASE' or p_container = 'LG BOX' or p_container = 'LG PACK' or p_container = 'LG PKG') and p_partkey = l_partkey);

\copy (select * from q19_3) to 'q19_3.tbl' delimiter '|';
