
CREATE TABLE spieler (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE wertung (
    id INT PRIMARY KEY,
    runde INT,
    spieler_id INT NOT NULL REFERENCES spieler(id),
    punkte INT,
    vorhersage INT,
    stiche INT
);


CREATE TYPE farbe AS ENUM ('blau', 'gelb', 'rot', 'gruen', 'narr', 'wizard');

CREATE TABLE karten (
    id INT PRIMARY KEY,
    kartenfarbe farbe,
    zahl INT CHECK (zahl >= 1 AND zahl <= 13),
    rang NUMERIC
);


-- prüfen welche Tabellen in der Datenbank sind
-- \dt in Postgres, in DuckDb weißnich

-- Tabelle löschen bei Fehler
-- DROP TABLE wertung;

-- Tabellen leeren
DELETE FROM spieler;
DELETE FROM wertung;
DELETE FROM karten;

-- Beispieldaten erstellen
INSERT INTO spieler VALUES (1, 'Dominik');
INSERT INTO spieler VALUES (2, 'Nixon');
INSERT INTO spieler VALUES (3, 'Karin');
INSERT INTO spieler VALUES (4, 'Isa');
INSERT INTO spieler VALUES (5, 'Kristian');

--                         id ru sp  pu vo sti
INSERT INTO wertung VALUES (1, 1, 1, 20, 0, 0);
INSERT INTO wertung VALUES (2, 1, 3, 30, 1, 1);
INSERT INTO wertung VALUES (3, 1, 4, 20, 0, 0);
INSERT INTO wertung VALUES (4, 1, 5, 20, 0, 0);
INSERT INTO wertung VALUES (5, 1, 2, 20, 0, 0);

-- Anwendungsfall 1: Vorhersagen speichern für Runde 2
INSERT INTO wertung VALUES (6, 2, 1, NULL, 0, NULL);
INSERT INTO wertung VALUES (7, 2, 3, NULL, 1, NULL);
INSERT INTO wertung VALUES (8, 2, 4, NULL, 1, NULL);
INSERT INTO wertung VALUES (9, 2, 5, NULL, 1, NULL);
INSERT INTO wertung VALUES (10,2, 2, NULL, 0, NULL);

-- Anzeige
SELECT * FROM wertung
    INNER JOIN spieler ON wertung.spieler_id = spieler.id;

 
-- Anwendungsfall 2: Punkte nach einer Runde eintragen
UPDATE wertung SET punkte=20, stiche=0 WHERE id=6; -- Dominik

UPDATE wertung SET punkte=20, stiche=0 WHERE spieler_id=2 AND runde=2; -- Nixon

UPDATE wertung SET punkte=-10, stiche=2 WHERE id=9; -- Kristian

UPDATE wertung SET punkte=-10, stiche=0 WHERE punkte IS NULL; -- Karin & Isa

-- hübschere Anzeige
SELECT runde, name, vorhersage, stiche, punkte FROM wertung
    INNER JOIN spieler ON wertung.spieler_id = spieler.id
    ORDER BY runde, name;


-- Anwendungsfall 3: Punkte zählen
SELECT name, sum(punkte) FROM wertung
    INNER JOIN spieler ON wertung.spieler_id = spieler.id
    GROUP BY name
    ORDER BY sum(punkte) DESC;