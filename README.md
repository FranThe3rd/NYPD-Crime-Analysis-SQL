
# NYPD Crime Analysis Project

## Purpose

The purpose of this project is to include crime analysis, statistical reporting, and understanding patterns related to criminal incidents in different locations. The database, called NYPD, contains tables for Incidents, Perpetrators, Victims, and Locations. 

## Description of Fields

The Incident table contains details about each incident such as:

- ID - A unique identifier 
- Date and Time - When the incident occurred
- Borough - The neighborhood where it happened
- LocationDesc - Description of the location
- Precinct - The connected police station  
- Other fields including jurisdiction, classification, murder flag, perpetrator and victim details, and location coordinates.

The other tables (Perpetrator, Victim, Location) link to the Incident table and contain specific details about those entities.

## Database Schema

The Incident table uses ID as its primary key. Foreign keys in the other tables reference the ID field to connect the data.

## Questions Explored

Some sample informational questions explored with SQL queries:

1. Average perpetrator age group for incidents in Brooklyn
2. Most common victim sex/race combination in Manhattan 
3. Number of incidents at bodegas in Queens
4. Precincts with most Hispanic perpetrator incidents  
5. Age/sex breakdown for Bronx apartment victims
6. Most common perpetrator race/sex against senior victims
7. Number of incidents with 18-24 perpetrator and victim
8. Homicide victims by gender

The separation into multiple linked tables enables these detailed analyses. Joins across the tables connect the relevant information.
