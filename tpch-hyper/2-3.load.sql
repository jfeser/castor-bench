COPY q2
FROM
'q2.tbl' DELIMITER '|';
COPY q2_supplier
FROM
'q2_supplier.tbl' DELIMITER '|';
COPY q3
FROM
'q3.tbl' DELIMITER '|';
