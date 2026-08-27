# Write your MySQL query statement below
SELECT firstName,lastName,city,state from Address right join Person ON Person.personId=Address.personId;