# catalyst-count

# Project Setup

## Database Setup Commands:
```bash
CREATE DATABASE catalyst_db;
CREATE USER catalyst_user WITH PASSWORD 'catalyst1234';
ALTER ROLE catalyst_user SET client_encoding TO 'utf8';
ALTER ROLE catalyst_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE catalyst_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE catalyst_db TO catalyst_user;