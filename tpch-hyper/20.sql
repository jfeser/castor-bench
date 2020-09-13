select s_name, s_address
  from q20_1
 where n_name = 'CANADA'
   and exists (select *
                 from q20_2
                where ps_suppkey = s_suppkey
                  and exists (select null
                                from q20_3
                               where l_shipdate >= date '1994-01-01'
                                 and l_shipdate < date '1995-01-01'
                                 and l_partkey = ps_partkey
                                 and l_suppkey = ps_suppkey
                              having ps_availqty > (0.5 * sum(tot_quantity)))
                  and exists (select *
                                from q20_4
                               where p_name like 'forest%'
                                 and p_partkey = ps_partkey))
       order by s_name;
