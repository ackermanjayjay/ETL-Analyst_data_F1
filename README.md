# ETL-Analyst_data_F1

## Objective
* Membuat service pipeline data dari file csv 
* Transformasi column data semulanya Capitalize menjadi lowercase
* Load data untuk dianalisa dalam bentuk SQL 

## workflow
![workflow](WORKFLOW.PNG)

## SQL query FIND most point in constructor
```
SELECT constructor , SUM(points) AS total_points
FROM f1_drivers 
GROUP BY "constructor" 
order  by sum(points) desc
limit 5;
```

## SQL query find Max points
```
SELECT driver_name, points  
FROM f1_drivers 
GROUP BY driver_name ,points  
order  by points desc
limit 5;
```

## Result
# Most points driver name
|driver_name|points|
|-----------|------|
|Max Verstappen|454|
|Charles Leclerc|308|
|Sergio Perez|305|
|George Russell|275|
|Carlos Sainz|246|

# Most points constructor name
|constructor|total_points|
|-----------|------------|
|Red Bull Racing RBPT|759|
|Ferrari|554|
|Mercedes|515|
|Alpine Renault|173|
|McLaren Mercedes|159|

