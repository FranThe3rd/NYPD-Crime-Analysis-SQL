-- 1. What is the average age group of perpetrators for incidents that occurred in Brooklyn?
SELECT AVG(PerpAgeGroup)
FROM Incident i JOIN Location l ON i.ID = l.IncidentID
WHERE Borough = 'BROOKLYN';

-- 2. What is the most common sex and race combination for victims in Manhattan?
SELECT VictimSex, VictimRace, COUNT(*) AS num
FROM Incident i 
JOIN Location l ON i.ID = l.IncidentID
WHERE Borough = 'MANHATTAN'
GROUP BY VictimSex, VictimRace
ORDER BY num DESC
LIMIT 1;

-- 3. How many incidents took place at bodegas in Queens?

SELECT COUNT(*) 
FROM Incident
WHERE Borough = 'QUEENS'AND LocDescription 
LIKE '%BODEGA%';

-- 4. What are the top 5 precincts with the most incidents involving a Hispanic perpetrator?
SELECT Precinct, COUNT(*) AS num
FROM Incident 
WHERE PerpRace LIKE '%HISPANIC%'
GROUP BY Precinct
ORDER BY num DESC
LIMIT 5;

-- 5. What is the age group and sex breakdown for victims in apartment buildings in the Bronx?
SELECT VictimAgeGroup, VictimSex, COUNT(*) AS num
FROM Incident i 
JOIN Location l ON i.ID = l.IncidentID
WHERE Borough = 'BRONX'
AND LocDescription LIKE '%APT BUILD%' 
GROUP BY VictimAgeGroup, VictimSex;

-- 6. What is the most common (race/sex)  of perpetrators who committed crimes against senior (65+) victims?
SELECT p.Race, p.Sex, COUNT(*) AS num
FROM Perpetrator p 
JOIN Victim v ON p.IncidentID = v.IncidentID
WHERE v.AgeGroup = '65+'
GROUP BY p.Race, p.Sex  
ORDER BY num DESC
LIMIT 1;

-- 7. How many incidents involve both perpetrator and victim in the 18-24 age group at public housing?

SELECT COUNT(*)
FROM Incident 
WHERE LocDescription LIKE '%PUBLIC HOUS%'
AND PerpAgeGroup = '18-24'
AND VictimAgeGroup = '18-24';

-- 8. How many homicide victims are female compared to male?
SELECT VictimSex, SUM(CASE WHEN MurderFlag = 'true' THEN 1 ELSE 0 END) AS homicides
FROM Incident
GROUP BY VictimSex



