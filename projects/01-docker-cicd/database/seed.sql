INSERT INTO tasks (title)
SELECT sample.title
FROM (VALUES
    ('Levantar la aplicación local'),
    ('Diseñar la solución Docker')
) AS sample(title)
WHERE NOT EXISTS (
    SELECT 1
    FROM tasks
    WHERE tasks.title = sample.title
);
