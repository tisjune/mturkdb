DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Workers;
DROP TABLE IF EXISTS WorkerAttrs;
DROP TABLE IF EXISTS Attrs;

CREATE TABLE Users (
	id INTEGER PRIMARY KEY,
	name TEXT,
	email TEXT UNIQUE,
	pwdhash TEXT,
	isadmin INTEGER,
	descr TEXT,
	awskey TEXT,
	awssecretkey TEXT
);

CREATE TABLE Workers (
	workerid TEXT PRIMARY KEY
);

CREATE TABLE WorkerAttrs (
	workerid TEXT,
	attrid INTEGER,
	value INT,
	granted INT,
	PRIMARY KEY (workerid, attrid),
	FOREIGN KEY(attrid) REFERENCES Attrs(attrid),
	FOREIGN KEY(workerid) REFERENCES Workers(workerid)
);

CREATE TABLE Attrs (
	attrid INTEGER PRIMARY KEY,
	amtid TEXT,
	publicname TEXT,
	privatename TEXT,
	publicdesc TEXT,
	privatedesc TEXT
);

INSERT INTO Users VALUES (0, 'lsr', 'lsrmturkdb@gmail.com', 'pbkdf2:sha1:1000$Wcblxhmo$abefc7a7715ebb01278fc94fee89fb46c2702c43', 1, 'LSR admin', null, null);
