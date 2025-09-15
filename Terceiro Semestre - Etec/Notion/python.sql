create database bloco;
use bloco;

create table contatinhos(
	id int not null auto_increment primary key,
    nome varchar(100),
    email varchar(50),
    telefone varchar(11),
    tipotelefone varchar(11)
);