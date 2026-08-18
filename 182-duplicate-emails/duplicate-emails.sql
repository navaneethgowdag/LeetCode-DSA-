select  e.email as Email from Person e
join Person i on e.email = i.email
where e.email is not null
group by e.email 
having count(e.email) > 1;