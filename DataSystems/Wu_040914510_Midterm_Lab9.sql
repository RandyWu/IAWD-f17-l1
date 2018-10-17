-- Lab 9 Midterm --

-- Q1 --
select distinct code
    from airports
    order by code asc
;

-- Q2 --
select count (distinct code)
    from airports
;

-- Q3 --
select count(*) as "Number of Airports in Spain"
    from airports
    where country like "ES"
;

-- Q4 --
select code, name
    from airports
    where city like "New York"
;

-- Q5  I think there are no airlines with no short_name --
select *
    from airlines
    where short_name like null
;

-- Q6 --
select code
    from airlines
    where code like "E%"
    order by code desc
;

-- Q7 --
select countries.code, count(*)
    from countries
    inner join airports
        on airports.country = countries.code
    group by countries.code
;

-- Q8 --
select departure, arrival, duration
    from flights
    where duration >= 700 and duration <= 1000
;

-- Q9 --
select count(name)
    from countries
    where continent > 2
;
