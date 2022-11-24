# SQL Cheatsheet
## Postgresql
### Login from cml terminal
```sql
# psql -U postgres -h <host-ip> -p <port> <db name>
psql -U postgres -h 10.224.44.127 -p 30050 ev_gis
```

### Create read-only user
```sql
--create a new user, which will turn to a user group
create role tpg_rf
with nologin;

---grant read-only previliege to the database, schema and table
GRANT CONNECT ON DATABASE mydatabase TO tpg_rf;
GRANT USAGE ON SCHEMA myschema TO tpg_rf;
GRANT SELECT ON ALL TABLES IN SCHEMA myschema TO tpg_rf;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA myschema TO tpg_rf;

--create a new user
create role evan
with login password 'Password12345'
in role tpg_rf;


--drop the user
drop owned by evan;
drop role if exists evan;
```

### Backup and Restore
* Backup
```bash
# Backup all contents in a specific schema
pg_dump -U postgres -h 10.224.44.127 -p 30050 tpg_gis -n macro  -Fc -f macro.backup

# Backup specific table(s)
pg_dump -U postgres -h 10.224.44.127 -p 30050 tpg_gis -n macro -t macro.macro_radius500  -Fc -f macro_s.backup

# Backup all contents in a specific schema exclude a collection of tables
pg_dump -U postgres -h 10.224.44.127 -p 30050 tpg_gis -n macro -T macro.macro_radius500  -Fc -f macro_s.backup
```

* Restore
```bash
pg_restore -U postgres -h 10.224.44.254 -p 30050 -d tpg_gis macro.backup

pg_restore -U postgres -h 10.224.44.254 -p 30050 -d tpg_gis  macro_s.backup
```


### Terminate a hung query
```sql
SELECT * FROM pg_stat_activity WHERE state = 'active' and query LIKE '%user_in_weak%' and wait_event_type = 'Lock';

SELECT pg_terminate_backend(1903405);
```

### Performance Tuning
EXPLAIN
```sql
EXPLAIN (Format JSON) SELECT * FROM categories;

EXPLAIN (ANALYZE on, VERBOSE on, Cost on, Timing on, Summary on, Buffer on) SELECT * FROM categories;
```

Inspect the table size and index size
```sql
SELECT pg_size_pretty( pg_relation_size( 'mytable' ) ) AS table_size,
     pg_size_pretty( pg_relation_size( 'imyindex' ) ) AS index_size;
```

Inspect the usage of the indexes
```sql
SELECT indexrelname, idx_scan, idx_tup_read, idx_tup_fetch FROM pg_stat_user_indexes WHERE relname = 'mytable';
```


## Mysql
### Login from cml terminal
```bash
# mysql -u <user-name> -p<password> -h <host-ip> -P <port> <database>
mysql -u evan -ptpg12345 -h 10.224.44.127 -P 30010 demo
```