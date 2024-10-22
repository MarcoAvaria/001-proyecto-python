CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios(
    id int auto_increment not null,
    nombre varchar(100),
    apellidos varchar(255),
    email varchar(255) not null,
    password varchar(255) not null,
    fecha date not null,
    PRIMARY KEY(id),
    UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE notas(
    id int auto_increment not null,
    usuario_id int not null,
    titulo varchar(255) not null,
    descripcion MEDIUMTEXT,
    fecha date not null,
    PRIMARY KEY(id),
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;