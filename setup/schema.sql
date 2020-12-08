DROP TABLE IF EXISTS swornoffice CASCADE;
DROP TABLE IF EXISTS recidivism CASCADE;
DROP TABLE IF EXISTS adultarresta CASCADE;
DROP TABLE IF EXISTS adultarrestb CASCADE;
DROP TABLE IF EXISTS indexcrime CASCADE;
DROP TABLE IF EXISTS income CASCADE;
DROP TABLE IF EXISTS population CASCADE;


CREATE TABLE swornoffice(
    county VARCHAR(255),
	pd VARCHAR(255),
    year INTEGER,
	fulltimetotal INTEGER,
	partimetotal INTEGER
);

CREATE TABLE recidivism(
	year INTEGER,
	county VARCHAR(255),
	gender VARCHAR(10),
	age INTEGER
);

CREATE TABLE adultarresta(
	county VARCHAR(255),
	year INTEGER,
	totalcase INTEGER,
	felonytotal INTEGER,
	misdemeanortotal INTEGER
);

CREATE TABLE adultarrestb(
	county VARCHAR(255),
	year INTEGER,
	drugf INTEGER,
	dwif INTEGER,
	drugm INTEGER,
	dwim INTEGER
);

CREATE TABLE indexcrime(
    county VARCHAR(255),
	agency VARCHAR(255),
	year INTEGER,
	indextotal INTEGER
);

CREATE TABLE income(
	year INTEGER,
    county VARCHAR(255),
	avgagi INTEGER,
	avgtax INTEGER
);

CREATE TABLE population(
	year INTEGER,
	county VARCHAR(255),
	popul INTEGER
);

