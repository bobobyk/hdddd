напишите запрос который вернет:

superhero_name всех героев мужчин SELECT COUNT(*) FROM superhero WHERE gender_id = 1 AND full_name IS NOT NULL
количество героев женщин SELECT COUNT(*) FROM superhero WHERE gen

средний рост и вес всех мужчин SELECT AVG(height_cm) AS average_height, 
AVG(weight_kg) AS average_weight
FROM superhero
WHERE gender_id = 1
AND (height_cm != 0 OR weight_kg != 0)

средний рост и вес всех добрых героев SELECT AVG(height_cm) AS average_height, AVG(weight_kg) AS average_weight
FROM superhero
WHERE alignment_id = 1
AND (height_cm != 0 OR weight_kg != 0)

средний рост и вес всех злых героев
SELECT AVG(height_cm) AS average_height, AVG(weight_kg) AS average_weight
FROM superhero
WHERE alignment_id = 2
AND (height_cm != 0 OR weight_kg != 0)

superhero_name всех героев superhero_name которых начинаются с буквы s
SELECT superhero_name 
FROM superhero 
WHERE superhero_name LIKE 'S%'

superhero_name и рост всех героев, рост которых больше 180, отсортированный по убыванию
SELECT superhero_name, height_cm
FROM superhero
WHERE height_cm > 180 
ORDER BY height_cm DESC



