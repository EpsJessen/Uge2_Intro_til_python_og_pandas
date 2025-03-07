select * from products order by UnitPrice DESC;
select * from Customers where Country='Spain' OR Country='UK';
select * from products where  UnitsInStock > 100 AND UnitPrice >= 25;
select distinct ShipCountry from orders;
select * from orders where OrderDate between '1996-10-01' and '1996-10-31';
select * from orders where shipCountry = 'Germany' and ShipRegion is null and orderDate between '1996-01-01' and '1996-12-31' and freight >= 100 and employeeID = 1;
select * from orders where RequiredDate < ShippedDate;
select * from orders where OrderDate between '1997-01-01' and '1997-04-30' and shipcountry='Canada';
select * from orders where employeeID in (2, 5, 8) and shipRegion is not null and shipVia in (1, 3) order by employeeID, shipvia;
select * from employees where (region is null -- or reportsto is null <--commented out since there is no column of that name in the table
	) and birthdate < '1961-01-01';
