PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE employee ( 
id INTEGER PRIMARY KEY,
nombre VARCHAR(20),
apellido VARCHAR(20)
);
INSERT INTO employee VALUES(0,'maxi','Aguilar');
INSERT INTO employee VALUES(1,'franco','Alonso');
INSERT INTO employee VALUES(2,'messi','Álvarez');
INSERT INTO employee VALUES(3,'maxi','Arias');
INSERT INTO employee VALUES(4,'franco','Benítez');
INSERT INTO employee VALUES(5,'messi','Blanco');
INSERT INTO employee VALUES(6,'maxi','Blesa');
INSERT INTO employee VALUES(7,'franco','Bravo');
INSERT INTO employee VALUES(8,'messi','Caballero');
INSERT INTO employee VALUES(9,'ani','Cabrera');
COMMIT;
