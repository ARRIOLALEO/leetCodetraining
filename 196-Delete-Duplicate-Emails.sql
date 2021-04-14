#What it is  CTE?  = "common table expression" used to create a temporary table , that later you can use to Filter , or
#Delete Data from a DB e.g. remove the Duplicates on a #Database #sqlhelp  #leetcode 196. Delete Duplicate Emails

Write your MySQL query statement below
WITH repeted(Id) as (
    SELECT MIN(ID) FROM Person GROUP BY Email
)
DELETE FROM Person WHERE Id NOT IN(
SELECT * FROM repeted
);
