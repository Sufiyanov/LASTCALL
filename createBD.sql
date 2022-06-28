CREATE DATABASE LASTCALL;

\c LASTCALL

CREATE TABLE persons (
    id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
	middle_name varchar(255),
	phone_number varchar(12) NOT NULL,
	city varchar(255) NOT NULL,
    address varchar(255) NOT NULL
);

CREATE TABLE logons (
    id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	person_id bigint REFERENCES persons (id),
    name varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL
);


CREATE TABLE calls (
    id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    person_id bigint REFERENCES persons (id),
    message text NOT NULL,
	date timestamp NOT NULL default CURRENT_TIMESTAMP,
	status varchar(255) default 'actual'
);
