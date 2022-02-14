CREATE DATABASE upgrade_yourself_db;
CREATE USER root WITH PASSWORD 'EmzZ2DfvhFitsiZ17WjEKONtTloAMkuB7QAPrfoXpVvxvDBfTX';
ALTER ROLE root SET default_transaction_isolation TO 'read committed';
ALTER ROLE root SET timezone TO 'UTC';
ALTER ROLE root SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE upgrade_yourself_db TO root;

ALTER USER root CREATEDB; #for creating test datab



-- CREATE USER root;
-- ALTER USER root WITH SUPERUSER;
-- ALTER USER root WITH PASSWORD 'EmzZ2DfvhFitsiZ17WjEKONtTloAMkuB7QAPrfoXpVvxvDBfTX';
-- ALTER ROLE root SET default_transaction_isolation TO 'read committed';
-- ALTER ROLE root SET timezone TO 'UTC';
-- ALTER ROLE root SET client_encoding TO 'utf8';
-- GRANT ALL PRIVILEGES ON DATABASE upgrade_yourself_db TO root;
-- ALTER USER root CREATEDB;

-- CREATE DATABASE upgrade_yourself_db;
-- CREATE USER upgrade_yourself_admin WITH PASSWORD 'EmzZ2DfvhFitsiZ17WjEKONtTloAMkuB7QAPrfoXpVvxvDBfTX';
-- ALTER ROLE upgrade_yourself_admin SET default_transaction_isolation TO 'read committed';
-- ALTER ROLE upgrade_yourself_admin SET timezone TO 'UTC';
-- ALTER ROLE upgrade_yourself_admin SET client_encoding TO 'utf8';
-- GRANT ALL PRIVILEGES ON DATABASE upgrade_yourself_db TO upgrade_yourself_admin;

-- ALTER USER upgrade_yourself_admin CREATEDB; #for creating test datab