--
-- Ziel: eine Spielsituation in Splendor komplett in der DB speichern.
--

CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name TEXT
);

INSERT INTO status(name) VALUES ('stapel');


CREATE TABLE spieler (
    id SERIAL PRIMARY KEY,

    token_rot INT,
    token_blau INT,
    token_weiss INT, 
    token_schwarz INT, 
    token_gruen INT, 

    name TEXT, 
    punkte INT
);

INSERT INTO spieler 1, 0, 0, 1, 1, 1, 'Jakob', 12);


CREATE TABLE karten (
    id SERIAL PRIMARY KEY,
    
    preis_rot INT,
    preis_blau INT,
    preis_weiss INT,
    preis_schwarz INT,
    preis_gruen INT,

    farbe CHAR,
    besitzer INT REFERENCES spieler(id),
    punkte INT,
    status_id INT REFERENCES status(id)
);

INSERT INTO karten VALUES (1, 1, 1, 1, 2, 0, 'G', 1, 0, 4);
INSERT INTO karten VALUES (2, 3, 3, 2, 0, 0, 'W', 2, 1, 4);
INSERT INTO karten VALUES (3, 0, 0, 0, 0, 3, 'S', NULL, 0, 2);


SELECT * FROM karten
    INNER JOIN status ON karten.status_id = status.id
    LEFT JOIN spieler ON karten.besitzer = spieler.id
;
