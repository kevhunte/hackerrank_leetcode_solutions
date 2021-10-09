# Write your MySQL query statement below
Select Person.FirstName, Person.Lastname, Address.City, Address.State
From Person
Left join Address
on Person.PersonId = Address.PersonId