SELECT
    s_suppkey,
    s_name,
    s_address,
    s_phone,
    total_revenue
FROM
    q15
WHERE
    l_shipdate = date '1996-01-01'
ORDER BY
    s_suppkey;

