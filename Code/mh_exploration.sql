SELECT * FROM mh_suicide_and_depression;
SELECT * FROM mh_by_sex;

SELECT * FROM mh_disorders;
SELECT * FROM mh_depression;


/* Get data to compare depression prevalence in USA to similarly sized con=untriees */ 
SELECT AVG(t1.Population) as us_pop
FROM
	(SELECT dep.Year, dep.Code, dep.Depression_prevalence, snd.Population
	FROM mh_depression dep
	JOIN mh_suicide_and_depression snd ON dep.Entity = snd.Entity AND dep.Year = snd.Year
	WHERE dep.Year BETWEEN 2000 AND 2017 AND dep.Code = 'USA') as t1;


SELECT dep.Year, dep.Entity, dep.Depression_prevalence, snd.Population
FROM mh_depression dep
JOIN mh_suicide_and_depression snd ON dep.Entity = snd.Entity AND dep.Year = snd.Year
WHERE dep.Year BETWEEN 2002 AND 2017 AND snd.Population BETWEEN 100000000 AND 360000000;



/* Data to chart anxiety trend in USA over time vs other disordders */ 
SELECT Entity, Year, `Anxiety_disorders(%)`, `Schizophrenia(%)`, `Bipolar_disorder(%)`, `Eating_disorders(%)`, `Depression(%)`
FROM mh_disorders
WHERE Code = 'USA';


/* Data to chart difference in male v female mental health in USA over time */ 
SELECT Entity, Year, `Prevalence_in_males(%)`, `Prevalence_in_females(%)`
FROM mh_by_sex
WHERE Code = 'USA';


/* Data to examine correlation between depression, alcohol abuse, drug abuse and suicide */ 
SELECT dis.Entity, ROUND(AVG(dis.`Alcohol_use_disorders(%)`), 2) as alcohol_use, ROUND(AVG(dis.`Drug_use_disorders(%)`), 2) as drug_use, ROUND(AVG(snd.`Depression_rate(per100.000)`), 2) as depression_rate, ROUND(AVG(snd.`Suicide_rate(per100.000)`), 2) as suicide_rate
FROM mh_disorders dis
JOIN mh_suicide_and_depression snd ON dis.Entity = snd.Entity AND dis.Year = snd.Year
GROUP BY dis.Entity;
