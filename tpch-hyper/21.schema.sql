create table q21 (
  n_name char(25) not null,
  s_name char(25) not null,
  numwait integer not null);

CREATE INDEX q21_idx ON q21 (n_name);

