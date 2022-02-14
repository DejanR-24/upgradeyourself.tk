-- CREATE DATABASE upgrade_yourself_db;
-- CREATE USER mydatabaseuser WITH PASSWORD 'EmzZ2DfvhFitsiZ17WjEKONtTloAMkuB7QAPrfoXpVvxvDBfTX';
-- ALTER ROLE mydatabaseuser SET default_transaction_isolation TO 'read committed';
-- ALTER ROLE mydatabaseuser SET timezone TO 'UTC';
-- ALTER ROLE mydatabaseuser SET client_encoding TO 'utf8';
-- GRANT ALL PRIVILEGES ON DATABASE upgrade_yourself_db TO mydatabaseuser;
-- ALTER USER mydatabaseuser CREATEDB; #for creating test datab

-- CREATE DATABASE upgrade_yourself_db;
-- CREATE USER upgrade_yourself_admin WITH PASSWORD 'EmzZ2DfvhFitsiZ17WjEKONtTloAMkuB7QAPrfoXpVvxvDBfTX';
-- ALTER ROLE upgrade_yourself_admin SET default_transaction_isolation TO 'read committed';
-- ALTER ROLE upgrade_yourself_admin SET timezone TO 'UTC';
-- ALTER ROLE upgrade_yourself_admin SET client_encoding TO 'utf8';
-- GRANT ALL PRIVILEGES ON DATABASE upgrade_yourself_db TO upgrade_yourself_admin;
-- ALTER USER upgrade_yourself_admin CREATEDB; #for creating test datab

CREATE DATABASE mydatabase;
CREATE USER mydatabaseuser WITH PASSWORD 'mypassword';
ALTER ROLE mydatabaseuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE mydatabaseuser SET timezone TO 'UTC';
ALTER ROLE mydatabaseuser SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO mydatabaseuser;
ALTER USER mydatabaseuser CREATEDB; #for creating test datab