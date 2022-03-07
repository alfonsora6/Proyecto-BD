--Primero accedemos con -> mysql -u root -p

--Creación de BD y usuario (Definiendole los privilegios)

CREATE DATABASE alumnos;
CREATE USER 'alfonso'@'%' IDENTIFIED BY 'proyectobd';
GRANT ALL PRIVILEGES ON alumnos.* to 'alfonso'@'%';
FLUSH PRIVILEGES;
USE alumnos;

--Luego podremos acceder a la base de datos desde el programa, con las credenciales del usuario que hemos definido.

--Creación de tablas

CREATE TABLE alumnos (
	id_alumno INT NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(32) NOT NULL,
	apellido VARCHAR(64) NOT NULL,
	fecha_nac DATE NOT NULL,
	PRIMARY KEY id_alumno_uq (id_alumno)
);

CREATE TABLE profesores (
	id_profesor INT NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(32) NOT NULL,
	apellido VARCHAR(64) NOT NULL,
	PRIMARY KEY id_profesor_uq (id_profesor)
);

CREATE TABLE asignaturas (
	id_asignatura INT NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(64) NOT NULL,
	profesor INT NOT NULL,
	PRIMARY KEY id_asignatura_uq(id_asignatura),
	FOREIGN KEY profesor_asignatura(profesor) REFERENCES profesores(id_profesor)
);

CREATE TABLE matriculas (
	alumno INT NOT NULL,
	asignatura INT NOT NULL,
	fecha YEAR NOT NULL,
	nota DECIMAL(3,2),
	PRIMARY KEY (alumno, asignatura, fecha),
	FOREIGN KEY alumno_matriculado(alumno) REFERENCES alumnos(id_alumno),
	FOREIGN KEY asignatura_matriculada(asignatura) REFERENCES asignaturas(id_asignatura)
);

--Insercción de datos

INSERT INTO alumnos VALUES
    (1,'Elena','Pérez','2000-02-18'),
    (2,'David','Sánchez','2001-11-13'),
    (3,'Miguel','López','1997-12-05'),
    (4,'Daniel','Gómez','2002-04-15'),
    (5,'Ana','Martínez','1995-09-29');

INSERT INTO profesores VALUES
    (1,'Javier','Sánchez'),
    (2,'Teresa','López'),
    (3,'Agustín','Domínguez');

INSERT INTO asignaturas VALUES
    (6,'Fundamentos de Hardware',1),
    (7,'Lenguaje de Marcas',2),
    (8,'Bases de Datos',2),
    (9,'Implantación de Sistemas Operativos',3);

INSERT INTO matriculas VALUES
	(1,6,YEAR('2021-06-15'),6.23),
	(1,8,YEAR('2022-11-12'),9.57),
	(2,6,YEAR('2020-02-03'),9.5),
	(2,7,YEAR('2020-09-23'),7.5),
	(2,8,YEAR('2020-02-24'),6.12),
	(3,6,YEAR('2021-07-15'),5.75),
	(4,9,YEAR('2021-10-23'),4.25),
	(4,6,YEAR('2021-10-23'),3.75),
	(5,9,YEAR('2022-10-13'),4.8);
