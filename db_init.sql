CREATE SCHEMA master;

CREATE TABLE master.operation (
id SERIAL NOT NULL PRIMARY KEY,
name VARCHAR(100) NOT NULL
);

CREATE TABLE master.team (
id SERIAL NOT NULL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
id_operation INT REFERENCES master.operation(id)
);

CREATE TABLE master.user (
id SERIAL NOT NULL PRIMARY KEY,
user_name VARCHAR(100) NOT NULL,
name_first VARCHAR(100) NOT NULL,
name_last VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL,
password VARCHAR(100) NOT NULL,
authenticated BOOLEAN DEFAULT False
);

CREATE TABLE master.user_operation (
id SERIAL NOT NULL,
id_user INT NOT NULL REFERENCES master.user(id),
id_operation INT NOT NULL REFERENCES master.operation(id),
PRIMARY KEY(id, id_user, id_operation)
);

CREATE TABLE master.user_team (
id SERIAL NOT NULL,
id_user INT NOT NULL REFERENCES master.user(id),
id_team INT NOT NULL REFERENCES master.team(id),
PRIMARY KEY(id, id_user, id_team)
);

CREATE SCHEMA growing;

CREATE TABLE growing.plant (
id SERIAL NOT NULL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
id_user INT NOT NULL REFERENCES master.user(id),
ts_start TIMESTAMP NOT NULL,
ts_end TIMESTAMP
);

CREATE SCHEMA notebook;



CREATE TABLE notebook.read_type_category (
id SERIAL NOT NULL PRIMARY KEY,
name VARCHAR(100) NOT NULL,	
description VARCHAR(100),
color VARCHAR(100)
);

CREATE TABLE notebook.read_type (
id SERIAL NOT NULL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
description VARCHAR(100) NOT NULL,
id_read_type_category INT REFERENCES notebook.read_type_category(id),
target_value VARCHAR(100),
frequency VARCHAR(100)
);

CREATE SCHEMA toolshed;

CREATE TABLE toolshed.tool (
id SERIAL NOT NULL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
id_read_type INT NOT NULL REFERENCES notebook.read_type(id)
);

CREATE TABLE toolshed.toolshed (
id SERIAL NOT NULL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
id_operation INT REFERENCES master.operation(id)
);

CREATE TABLE notebook.reading (
id SERIAL NOT NULL PRIMARY KEY,
id_plant INT NOT NULL REFERENCES growing.plant(id),
ts_reading_taken TIMESTAMP NOT NULL,
id_read_type INT NOT NULL REFERENCES notebook.read_type(id),
value VARCHAR(100) NOT NULL,
id_taker INT NOT NULL REFERENCES master.user(id),
id_tool INT REFERENCES toolshed.tool(id)
);

CREATE TABLE toolshed.team_toolshed (
id SERIAL NOT NULL,
id_team INT NOT NULL REFERENCES master.team(id),
id_toolshed INT NOT NULL REFERENCES toolshed.toolshed(id),
PRIMARY KEY(id, id_team, id_toolshed)
);

CREATE TABLE toolshed.toolshed_tool (
id_toolshed INT NOT NULL REFERENCES toolshed.toolshed(id),
id_tool INT NOT NULL REFERENCES toolshed.tool(id),
PRIMARY KEY(id_toolshed, id_tool)
);

CREATE SCHEMA appendix;

CREATE TABLE appendix.lighting (
id SERIAL NOT NULL PRIMARY KEY
);

INSERT INTO master.user
VALUES(DEFAULT, 'test_user', 'test', 'user', 'email@email.com', 'password', DEFAULT);

INSERT INTO notebook.read_type_category
VALUES(DEFAULT, 'lighting', 'describes lighting stuff', 'yellow');

INSERT INTO notebook.read_type
VALUES(DEFAULT, 'test_name', 'test_description', 1);

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA growing TO hero;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA notebook TO hero;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA appendix TO hero;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA master TO hero;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA toolshed TO hero;

GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA growing TO hero;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA notebook TO hero;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA appendix TO hero;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA master TO hero;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA toolshed TO hero;

-- INSERT INTO growing.plant
-- VALUES(DEFAULT, '1', 'plant name 1', '2018-01-01 01:01:01');
-- INSERT INTO growing.plant(
-- 	id, name, id_user, ts_start, ts_end)
-- 	VALUES (1, 'plant name 1', ?, ?, ?);

-- INSERT INTO growing.plant
-- VALUES(DEFAULT, 'plant name 2', '2018-02-02 01:01:01');