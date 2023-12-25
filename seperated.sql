CREATE TABLE Perpetrator
SELECT ID AS IncidentID, 
    PerpAgeGroup AS AgeGroup,
    PerpSex AS Sex,
    PerpRace AS Race
FROM Incident;

CREATE TABLE Victim 
SELECT ID AS IncidentID,
    VictimAgeGroup AS AgeGroup,
    VictimSex AS Sex, 
    VictimRace AS Race
FROM Incident;

CREATE TABLE Location
SELECT ID AS IncidentID,
    XCoord, 
    YCoord,
    Latitude,
    Longitude,
    LocationPoint
FROM Incident;