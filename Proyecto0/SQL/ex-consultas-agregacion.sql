
/* MIN y MAX */

-- Ejercicio 1: Encontrar la duración mínima de las pistas en milisegundos.
select min("Milliseconds") as "Duracion_Minima"
from "Track" t 

-- Ejercicio 2: Encontrar la duración máxima de las pistas en milisegundos.
select max("Milliseconds") as "Duracion_Maxima"
from "Track" t 

-- Ejercicio 3: Encontrar el precio mínimo de las pistas.
select min("UnitPrice") as "Precio_Minimo"
from "Track" t 

-- Ejercicio 4: Encontrar el precio máximo de las pistas.
select max("UnitPrice") as "Precio_Maximo"
from "Track" t 

-- Ejercicio 5: Encontrar la fecha mínima de la factura.
select min("InvoiceDate") as "Fecha_Minima_Factura"
from "Invoice" i 

-- Ejercicio 6: Encontrar la fecha máxima de la factura.
select max("InvoiceDate") 
from "Invoice" i 

/* COUNT y SUM */

-- Ejercicio 7: Contar el número total de pistas.
select count("TrackId")  as "Total_Pistas"
from "Track" t 

-- Ejercicio 8: Contar el número de clientes en Brasil.
select count("CustomerId") as "Clientes_Brasil"
from "Customer" c 
where "Country" = 'Brazil'

-- Ejercicio 9: Sumar la duración total de todas las pistas en milisegundos.
select sum("Milliseconds") 
from "Track" t 

-- Ejercicio 10: Contar el número de empleados con el título 'Sales Support Agent'.
select count("EmployeeId") as "Empleados_Sales_Support_Agent"
from "Employee" e 
where "Title" = 'Sales Support Agent'

-- Ejercicio 11: Sumar el total de las cantidades en las facturas.
select sum("Total") as "Suma_Ventas"
from "Invoice" i 

/* AVG, STDDEV, VARIANCE */

-- Ejercicio 12: Calcular la duración media de las pistas en milisegundos.
select avg("Milliseconds") as "Duracion_Media_mm"
from "Track" t 

-- Ejercicio 13: Calcular el precio medio de las pistas.
select avg("UnitPrice") as "Precio_Medio"
from "Track" t 

-- Ejercicio 14: Calcular la desviación estándar de la duración de las pistas.
select round(stddev("Milliseconds"),2) as "Desv_Estandar_Pistas"
from "Track" t 

-- Ejercicio 15: Calcular la varianza de la duración de las pistas.
select round(variance("Milliseconds"),2) as "Varianza_Pistas"
from "Track" t 

-- Ejercicio 16: Calcular la desviación estándar del precio de las pistas.
select round(stddev("UnitPrice"),2) as "Desv_Estandar_PrecioPistas"
from "Track" t 

/* CONCAT */

-- Ejercicio 17: Concatenar el nombre y el apellido de los clientes.
select concat("FirstName",' ', "LastName") as "Nombre_Cliente"
from "Customer" c 
