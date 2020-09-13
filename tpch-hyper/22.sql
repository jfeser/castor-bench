select phone_2,
       count(*),
       sum(acctbal_2)
  from q22_2
 where acctbal_2 > (select sum(acctbal_1)/sum(custcount_1)
                      from q22_1
                     where phone_1 in ('13', '31', '23', '29', '30', '18', '17'))
   and phone_2 in ('13', '31', '23', '29', '30', '18', '17')
group by phone_2
