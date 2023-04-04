-- create a read-only user for Grafana
CREATE USER grafana_user;
ALTER ROLE grafana_user WITH PASSWORD 'nwfnqhzujqfagusdaahrdwlthhlwhwkf';
CREATE DATABASE grafana_user;

-- give grafana_user read access to tables
GRANT SELECT ON ALL TABLES IN SCHEMA public TO grafana_user;