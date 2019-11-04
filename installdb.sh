sudo -u postgres dropdb database_backup >> /dev/null
sudo -u postgres createdb database_backup
sudo -u postgres psql << EOF
alter user postgres with encrypted password 'pazverde123';
alter role postgres set client_encoding to 'utf8';
alter role postgres set default_transaction_isolation to 'read committed';
alter role postgres set timezone to 'utc';
alter role postgres createdb;
grant all privileges on database database_backup to postgres ;\q
EOF