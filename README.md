## Create data schema
After putting your parquet file into `datalake` bucket, please execute `trino` container by the following command:
```shell
docker exec -ti datalake-trino bash
```

When you are already inside the container, running:
```shell
psql -U k6 -d k6 -W 
# Enter the password: k6
```

After that, run the following command to register a new schema for our data:

```sql
CREATE SCHEMA IF NOT EXISTS datalake.iot_time_series
WITH (location = 's3://datalake/');

CREATE TABLE IF NOT EXISTS datalake.iot_time_series.data (
  pressure DOUBLE,
  velocity  DOUBLE,
  speed DOUBLE
) WITH (
  external_location = 's3://datalake/iot_time_series/',
  format = 'PARQUET'
);
```