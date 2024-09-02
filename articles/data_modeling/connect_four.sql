
CREATE TABLE IF NOT EXISTS grid (

    x INT,
    y INT,
    status CHAR

);
INSERT INTO grid VALUES (4, 1, 'O');
INSERT INTO grid VALUES (4, 2, 'X');
INSERT INTO grid VALUES (6, 1, 'O');

-- Höhe finden in der ein eingeworfener Stein landet 
--
-- a) coalesce nimmt das erste nicht-leere Argument
SELECT coalesce(max(y)+1, 1) FROM grid WHERE x=4;

-- b) Zeilen zählen + 1
SELECT count(*)+1 FROM grid WHERE x=2;
