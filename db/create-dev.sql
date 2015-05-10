DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS WorkerAttrs;
DROP TABLE IF EXISTS Attrs;
DROP TABLE IF EXISTS Actions;

CREATE TABLE Users (
	id INTEGER PRIMARY KEY,
	name TEXT,
	email TEXT UNIQUE NOT NULL,
	pwdhash TEXT NOT NULL,
	isadmin INTEGER,
	descr TEXT,
	awskey TEXT,
	awssecretkey TEXT
);

CREATE TABLE WorkerAttrs (
	workerid TEXT,
	amtid INTEGER,
	value INT,
	PRIMARY KEY (workerid, amtid)
);

CREATE TABLE Attrs (
	amtid TEXT PRIMARY KEY,
	publicname TEXT,
	privatename TEXT,
	publicdescr TEXT,
	privatedescr TEXT
);

CREATE TABLE Actions (
	id INTEGER PRIMARY KEY,
	userid INTEGER NOT NULL,
	descr TEXT,
	FOREIGN KEY(userid) REFERENCES Users(id)
);
INSERT INTO Users VALUES (0, 'Admin', 'lsrmturkdb@gmail.com', 'pbkdf2:sha1:1000$Wcblxhmo$abefc7a7715ebb01278fc94fee89fb46c2702c43', 1, 'LSR admin', null, null);
