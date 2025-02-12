
-- Ejercicio  1: Encuentra el nombre de las pistas y los títulos de los álbumes a los que pertenecen.
select t."Name" as "Nomber de la Pista", a."Title" as "Album"
from "Track" t 
inner join "Album" a 
on t."AlbumId" = a."AlbumId" 

-- Ejercicio 2: Lista los nombres de los artistas y los títulos de sus álbumes. Ordena los resultados por artista.
select a."Name" as "Artistas", a2."Title" as "Album"
from "Artist" a 
inner join "Album" a2 
on a."ArtistId" = a2."ArtistId" 
order by "Artistas"

-- Ejercicio 3: Encuentra los nombres de los clientes y los totales de sus facturas. Extrae solo los 5 clientes con mayor total. 
select concat(c."FirstName", ' ',c."LastName") as "Nombre_Clientes", sum(i."Total") as "Total"
from "Customer" c 
inner join "Invoice" i 	
on c."CustomerId" = i."CustomerId" 
group by concat(c."FirstName", ' ',c."LastName")
order by "Total" desc 
limit 5

-- Ejercicio 4: Lista los nombres de los empleados y los nombres de los clientes que les han sido asignados.
select  concat(e."FirstName", ' ', e."LastName") as "Nombre _Empleado",
		concat(c."FirstName", ' ', c."LastName") as "Nombre_Cliente" 
from "Employee" e 
inner join "Customer" c 
on e."EmployeeId" = c."SupportRepId" 
group by concat(e."FirstName", ' ', e."LastName"), concat(c."FirstName", ' ', c."LastName")


-- Ejercicio 5: Muestra los ID de las facturas y los nombres de las pistas incluidas en esas facturas.
select "InvoiceId" as "ID_Factura", t."Name" as "Nombre_Pista"
from "InvoiceLine" il 
inner join "Track" t 
on il."TrackId" = t."TrackId" 

-- Ejercicio 6: Encuentra los nombres de los artistas y los géneros de sus pistas.
SELECT ar."Name" AS "Nombre_Artista", g."Name" AS "Genero"
FROM "Artist" ar
INNER JOIN "Album" al ON ar."ArtistId" = al."ArtistId"
INNER JOIN "Track" t ON al."AlbumId" = t."AlbumId"
INNER JOIN "Genre" g ON t."GenreId" = g."GenreId";

--  Ejercicio 7: Muestra los nombres de las pistas y el tipo de medio en el que están disponibles.
select t."Name" as Nombre_Pistas, mt."Name" as Tipo_Medio
from "Track" t 
inner join "MediaType" mt on t."MediaTypeId" = mt."MediaTypeId" 

-- Ejercicio 8: Encuentra todas las pistas y, si existen, muestra los nombres de los géneros a los que pertenecen. Incluye también las pistas que no tienen un género asignado.**
select t."Name" "Pista", g."Name" "Genero"
from "Track" t 
left join "Genre" g on t."GenreId" = g."GenreId" 

-- Ejercicio 9: Muestra todos los clientes y, si existen, muestra las facturas que han realizado. Incluye también los clientes que no tienen ninguna factura.
select concat(c."FirstName",' ',c."LastName") as "Cliente", i."InvoiceId" as "Factura"
from "Customer" c 
left join "Invoice" i on c."CustomerId" = i."CustomerId" 

-- Ejercico 10: Encuentra todos los álbumes y, si existen, muestra los nombres de los artistas que los crearon. Incluye también los álbumes que no tienen un artista asignado (aunque en este caso en la base de datos de Chinook, todos los álbumes tienen un artista asignado).
select a."Title" as "Album", a2."Name" as "Artista"
from "Album" a 
left join "Artist" a2 on a."ArtistId" = a2."ArtistId" 

-- Ejercicio 11: Cuenta cuántas pistas hay en cada género. Ordena los generos en función del número de canciones de mayor a menor. 
select count(t."TrackId") as Pistas, g."Name" as "Genero" 
from "Track" t 
inner join "Genre" g on t."GenreId" = g."GenreId" 
group by g."Name" 
order by pistas desc 

--  Ejercicio 12: Muestra los títulos de los álbumes y la duración total de todas las pistas en cada álbum.
SELECT a."Title" AS "Album", SUM(t."Milliseconds") AS "Duracion_Total"
FROM "Album" a 
INNER JOIN "Track" t ON a."AlbumId" = t."AlbumId"
GROUP BY a."Title";


-- Ejercicio 14: Encuentra los nombres de los clientes y el total gastado por cada uno.
select concat(c."FirstName", ' ', c."LastName") as Clientes, sum(i."Total") as Total_Gastado
from "Customer" c 
inner join "Invoice" i on c."CustomerId" = i."CustomerId" 
group by concat(c."FirstName", ' ', c."LastName") 

-- Ejercicio 15: Encuentra todos los empleados y, si existen, muestra los nombres de los clientes que tienen asignados. Incluye también los empleados que no tienen clientes asignados.
select concat(e."FirstName", ' ', e."LastName") as "empleado", concat(c."FirstName", ' ', c."LastName") as "cliente"
from "Employee" e 
left join "Customer" c on e."EmployeeId" = c."SupportRepId" 


