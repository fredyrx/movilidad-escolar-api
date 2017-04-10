/* DDL Creacion de tablas */

CREATE TABLE IF NOT EXISTS users(
id serial,
email varchar(50) unique,
password_hash varchar(64) not null,
active boolean default true,
actived_at timestamp,
created_at timestamp,
alter_at timestamp,
primary key(id)
);

CREATE TABLE IF NOT EXISTS hashes(
 id serial,
 user_id integer REFERENCES users(id),
 hash_string varchar(64),
 active boolean default true,
 used boolean default false,
 created_at timestamp,
 altered_at timestamp,
 primary key(id)
)

select * from users;