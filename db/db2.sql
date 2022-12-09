CREATE DATABASE ConnectNU;

-- move into the the database we just created mhm
USE ConnectNU;

CREATE TABLE ClubMember (
    idNumber INTEGER PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    college TEXT,
    year INTEGER
);

INSERT INTO ClubMember 
    (idNumber, firstName, lastName, college, year)
VALUES 
    (002118972, 'Lisetta', 'Daniello', 'Science', 5),
    (002110084, 'Lulita', 'Laddle', 'Business', 1),
    (002110392, 'Regan', 'Robb', 'Humanities', 4),
    (002117096, 'Addie', 'Dingwall', ' Art', 2),
    (002118400, 'Ethelind', 'Polkinghorne', 'Engineering', 4),
    (002119127, 'Torie', 'Neild', 'Health Science', 3);

CREATE TABLE committees (
    committeeID INTEGER PRIMARY KEY,
    committeeName TEXT
);

INSERT INTO committees 
    (committeeID, committeeName)
VALUES 
    (1, 'Internal Affairs'),
    (2, 'Campus Relations'),
    (3, 'Events'),
    (4, 'Marketing'),
    (5, 'Recruitment');

CREATE TABLE committeeMember (
    committeeID INTEGER,
    memberID INTEGER,
    FOREIGN KEY (committeeID) REFERENCES committees(committeeID),
    FOREIGN KEY (memberID) REFERENCES ClubMember(idNumber),
    PRIMARY KEY(committeeID, memberID)
);

INSERT INTO committeeMember 
    (committeeID, memberID)
VALUES 
    (1, 002117096),
    (2, 002118400),
    (3, 002119127);



CREATE TABLE committeeLeader (
    committeeID INTEGER,
    leaderID INTEGER,
    FOREIGN KEY (committeeID) REFERENCES committees(committeeID),
    FOREIGN KEY (leaderID) REFERENCES ClubMember(idNumber),
    PRIMARY KEY(committeeID, leaderID)
);

INSERT INTO committeeLeader 
    (committeeID, leaderID)
VALUES 
    (1, 002118972),
    (2, 002110084),
    (3, 002110392);



CREATE TABLE supervisor (
    staffID INTEGER PRIMARY KEY,
    firstName TEXT,
    lastName TEXT
);

INSERT INTO supervisor 
    (staffID, firstName, lastName)
VALUES 
    (203, 'Cate', 'Iannuzzelli'),
    (393, 'Sidoney', 'Ecob'),
    (291, 'Jemmie', 'Berg'),
    (168, 'Gnni', 'John'),
    (118, 'Susanetta', 'Benedite');                          


CREATE TABLE dues (
    dueID INTEGER PRIMARY KEY,
    dueTypeName TEXT,
    dueAmount FLOAT
);

INSERT INTO dues 
    (dueID, dueTypeName, dueAmount)
VALUES 
    (1, 'Events', 50),
    (2, 'Annual', 75),
    (3, 'Merch', 40);



CREATE TABLE duePayment (
    memberID INTEGER, -- club member ID
    dueID INTEGER, -- due ID
    paymentDate DATE, -- date 
    FOREIGN KEY (memberID) REFERENCES ClubMember(idNumber),
    FOREIGN KEY (dueID) REFERENCES dues(dueID),
    PRIMARY KEY(memberID, dueID)
);

 INSERT INTO duePayment 
    (memberID, dueID, paymentDate)
 VALUES 
    (002118972, 1, '2022-01-02'),
    (002118972, 2, '2022-04-27');



CREATE TABLE Events (
    eventID INTEGER PRIMARY KEY, 
    eventType VARCHAR(20), 
    eventDate DATE,
    eventTitle VARCHAR(20)
);

 INSERT INTO Events 
    (eventID, eventType, eventDate, eventTitle)
 VALUES 
    (1, 'meeting', '2022-01-02', 'Meeting 1'),
    (2, 'internal', '2022-04-02', 'Movie Night'),
    (3, 'external', '2022-04-05', 'Tabling');



CREATE TABLE eventPoints (
    memID INTEGER, 
    eventID INTEGER, 
    FOREIGN KEY (memID) REFERENCES ClubMember(idNumber), 
    FOREIGN KEY (eventID) REFERENCES Events(eventID)
);

 INSERT INTO eventPoints 
    (memID, eventID)
 VALUES 
    (002118972, 1),
    (002118972, 2),
    (002118972, 3),
    (002110084, 2),
    (002110084, 3);

GRANT ALL PRIVILEGES ON ConnectNU.* TO 'webapp'@'%';
FLUSH PRIVILEGES;
