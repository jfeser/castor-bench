SELECT
    n_name,
    sum(agg3) AS revenue
FROM
    q5
WHERE
    o_orderdate >= date '1994-01-01'
    AND o_orderdate < date '1995-01-01'
    AND r_name = 'ASIA'
GROUP BY
    n_name;

