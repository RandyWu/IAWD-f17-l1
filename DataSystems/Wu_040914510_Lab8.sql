USE world;
-- Querying tables city and country --

-- Q1 --
SELECT city.name, city.population, country.continent
    FROM city INNER JOIN country
        ON city.countrycode = country.code
    ORDER BY country.continent, city.population, city.name;

-- Q2 --
SELECT city.name, city.population, country.continent
    FROM city, country
    WHERE city.countrycode = country.code
    ORDER BY country.continent, city.population, city.name;

-- Q3 --
SELECT city.name, city.population, country.continent, country.indepyear
    FROM country INNER JOIN city
        ON city.countrycode = country.code
    WHERE country.indepyear = "1960"
    ORDER BY country.continent, city.population, city.name;

-- Q4 --
SELECT city.name, city.population, country.continent, country.indepyear
    FROM country, city
    WHERE city.countrycode = country.code
    AND country.indepyear = "1960"
    ORDER BY country.continent, city.population, city.name;

-- Q5 --
SELECT city.name, country.headofstate
    FROM city INNER JOIN country
        ON city.countrycode = country.code
    WHERE city.name = "Ottawa";

-- Q6 --
SELECT city.name, city.population as city_pop, country.continent, country.population as country_pop
    FROM city INNER JOIN country
        ON city.countrycode = country.code
    WHERE city.name = "Toronto";


-- Querying tables city and countryLanguage --

-- Q1 --
SELECT city.name, countryLanguage.language, countryLanguage.percentage
    FROM city INNER JOIN countryLanguage
        ON city.countrycode = countryLanguage.countrycode
    WHERE city.name = "Ottawa";

-- Q2 --
SELECT city.name, countryLanguage.language, countryLanguage.percentage
    FROM city, countryLanguage
    WHERE city.countrycode = countryLanguage.countrycode
    AND city.name = "Ottawa"
    AND countryLanguage.isofficial = "T";

-- Q3 --
SELECT city.name, countryLanguage.language, countryLanguage.isofficial, countryLanguage.percentage
    FROM city INNER JOIN countryLanguage
        ON city.countrycode = countryLanguage.countrycode
    WHERE city.name = "Ottawa"
    AND (
      countryLanguage.isofficial = "T" OR countryLanguage.language = "Polish"
    );

-- Q4 --
SELECT SUM(countryLanguage.percentage)
    FROM city INNER JOIN countryLanguage
        on city.countrycode = countryLanguage.countrycode
    WHERE city.name = "Ottawa"
    AND (
      countryLanguage.isofficial = "T" OR countryLanguage.language = "Russian"
    );


-- Querying tables city, country and countryLanguage --

-- Q1 --
SELECT city.name, country.continent, country.headofstate, country.indepyear, (city.population * (countryLanguage.percentage/100)) as total_pop_speaking_language
   FROM city INNER JOIN country
       ON city.countrycode = country.code
   INNER JOIN countryLanguage
       ON country.code = countryLanguage.countrycode
   WHERE city.name = "Toronto"
   AND countryLanguage.language = "Italian";

-- Q2 --
SELECT city.name, country.continent, country.headofstate, country.indepyear, (city.population * (countryLanguage.percentage/100)) as total_pop_speaking_language
   FROM city, country, countryLanguage
   WHERE city.countrycode = country.code
   AND country.code = countryLanguage.countrycode
   AND city.name = "Toronto"
   AND countryLanguage.language = "Italian";
