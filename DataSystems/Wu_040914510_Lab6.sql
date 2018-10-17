USE WORLD;

-- Q1 --
SELECT countrycode, count(name)
    FROM city
    GROUP BY countrycode;

-- Q2 --
SELECT countrycode, count(name)
    FROM city
    GROUP BY countrycode
    HAVING count(name) > 200;

-- Q3 --
/* Query doesn't work due to syntax error, WHERE cannot be after GROUP BY together in the same line */

-- Q4 --
SELECT countrycode, count(name), sum(population)
    FROM city
    GROUP BY countrycode;

-- Q5 --
SELECT district, countrycode, count(name)
    FROM city
    GROUP BY district, countrycode;

-- Q6 --
SELECT countrycode, count(name) AS number_of_cities, sum(population) AS pop_total, avg(population) AS pop_average
    FROM city
    GROUP BY countrycode;

-- Q7 --
SELECT district, countrycode, count(name) AS number_of_cities, sum(population) AS pop_total, avg(population) AS pop_average
    FROM city
    GROUP BY district, countrycode
    HAVING district LIKE 'a%';

-- Q8 --
SELECT district, countrycode, count(name) AS number_of_cities, sum(population) AS pop_total, avg(population) AS pop_average
    FROM city
    GROUP BY district, countrycode
    HAVING district LIKE 'a%' AND number_of_cities > 10;

-- Q9 --
SELECT count(name) AS number_of_cities, sum(population) as pop_total, avg(population) AS pop_average, min(population) as min_pop, max(population) as max_pop
    FROM city;
