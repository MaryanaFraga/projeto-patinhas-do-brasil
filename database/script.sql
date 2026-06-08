CREATE DATABASE IF NOT EXISTS adocao_animais;
USE adocao_animais;

CREATE TABLE IF NOT EXISTS animais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    especie VARCHAR(255) NOT NULL,
    idade INT NOT NULL,
    status_adocao VARCHAR(50) NOT NULL,
    descricao TEXT,
    foto VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS adotantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS adocoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_animal INT NOT NULL,
    id_adotante INT NOT NULL,
    data_adocao DATE NOT NULL,
    FOREIGN KEY (id_animal) REFERENCES animais(id),
    FOREIGN KEY (id_adotante) REFERENCES adotantes(id)
);