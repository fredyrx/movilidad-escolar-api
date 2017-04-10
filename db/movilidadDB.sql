/* DDL Creacion de tablas */

/* Tablas maestras */
CREATE TABLE IF NOT EXISTS schools(
id serial,
name varchar(100) NOT NULL,
address varchar(100),
latitude POINT,
longitude POINT,
logo varchar(250),
created_at timestamp default CURRENT_TIMESTAMP,
alter_at timestamp default CURRENT_TIMESTAMP,
primary key (id)
);

CREATE TABLE IF NOT EXISTS licenses(
id varchar(5) primary key,
license_class char(1),
license_category varchar(4) 
);

CREATE TABLE IF NOT EXISTS states(
id char(2) primary key,
name varchar(50) NOT NULL,
order_number integer NOT NULL
);
/* tablas */
CREATE TABLE IF NOT EXISTS users(
id serial,
email varchar(50) unique,
password_hash varchar(64) not null,
name varchar(50),
last_name varchar(50),
active boolean default true,
created_at timestamp default CURRENT_TIMESTAMP,
alter_at timestamp default CURRENT_TIMESTAMP,
primary key(id)
);

CREATE TABLE IF NOT EXISTS drivers(
id serial,
user_id integer REFERENCES users(id),
license_id varchar(5) REFERENCES licenses(id),
license_number varchar(9),
license_revalidation date,
active boolean default true,
created_at timestamp default CURRENT_TIMESTAMP,
alter_at timestamp default CURRENT_TIMESTAMP,
primary key(id)
);

CREATE TABLE IF NOT EXISTS clients(
id serial,
user_id integer REFERENCES users(id),
name varchar(50),
last_name varchar(50),
photo varchar(255),
born_date date,
address varchar(50),
latitude POINT,
longitude POINT,
created_at timestamp default CURRENT_TIMESTAMP,
alter_at timestamp default CURRENT_TIMESTAMP,
primary key(id)
);
/*
CREATE TABLE IF NOT EXISTS client_addresses(
id serial,
client_id integer references clients(id)
address varchar(50)
latitude long,
longitude long
main boolean default false,
active boolean default true,
created_at timestamp,
modified_at timestamp,
primary key(id)
);
*/

CREATE TABLE IF NOT EXISTS dependents(
id serial,
client_id integer references clients(id),
name varchar(50),
last_name varchar(50),
born_date date,
address varchar(50),
latitude POINT,
longitude POINT,
created_at timestamp default CURRENT_TIMESTAMP,
alter_at timestamp default CURRENT_TIMESTAMP,
primary key(id)
);

/**/
CREATE TABLE IF NOT EXISTS contracts(
id serial,
driver_id integer REFERENCES drivers(id),
client_id integer REFERENCES clients(id),
dependant_id integer REFERENCES dependents(id),
school_id integer REFERENCES schools(id),
start_date date,
end_date date,
created_at timestamp default CURRENT_TIMESTAMP,
alter_at timestamp default CURRENT_TIMESTAMP,
primary key(id)
);

CREATE TABLE IF NOT EXISTS services(
driver_id integer REFERENCES drivers(id),
service_date date,
state_id char(2) REFERENCES states(id),
active boolean default true,
created_at timestamp default CURRENT_TIMESTAMP,
modified_at timestamp default CURRENT_TIMESTAMP,
primary key(driver_id,service_date)
);

CREATE TABLE IF NOT EXISTS service_header(
driver_id integer REFERENCES drivers(id),
service_date date,
state_id char(2) REFERENCES states(id),
start_time time,
audit_latitude POINT,
audit_longitude POINT,
audit_precision numeric,
created_at timestamp default CURRENT_TIMESTAMP,
modified_at timestamp default CURRENT_TIMESTAMP,
primary key(driver_id, service_date, state_id)
);

CREATE TABLE IF NOT EXISTS service_details(
driver_id integer,
service_date date,
state_id char(2),
depentant_id integer REFERENCES dependents(id),
success boolean,
audit_time time,
audit_latitude POINT,
audit_longitude POINT,
audit_precision numeric,
created_at timestamp default CURRENT_TIMESTAMP,
modified_at timestamp default CURRENT_TIMESTAMP,
primary key(driver_id, service_date, state_id, depentant_id),
foreign key (driver_id, service_date, state_id) REFERENCES service_header(driver_id, service_date, state_id)
);


--select * from users;


select now(), CURRENT_TIMESTAMP, CURRENT_TIME, CURRENT_DATE, 5.656