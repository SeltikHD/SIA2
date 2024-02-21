CREATE TABLE cultura (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    trefle_id INTEGER NOT NULL
);

CREATE TABLE dados_periodicos (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    temperatura FLOAT NOT NULL,
    umidade FLOAT NOT NULL,
    path_image TEXT,
    cultura_id INTEGER REFERENCES cultura(id) ON DELETE CASCADE
);

CREATE TABLE condicoes_ideias (
    id SERIAL PRIMARY KEY,
    temperatura_min FLOAT NOT NULL,
    temperatura_max FLOAT NOT NULL,
    umidade_min FLOAT NOT NULL,
    umidade_max FLOAT NOT NULL,
    cultura_id INTEGER REFERENCES cultura(id) ON DELETE CASCADE
);

CREATE TABLE chave_api (
    id SERIAL PRIMARY KEY,
    chave TEXT NOT NULL,
    ativo BOOLEAN NOT NULL
);

CREATE TABLE log_acesso (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    ip TEXT NOT NULL,
    chave_api_id INTEGER REFERENCES chave_api(id) ON DELETE CASCADE
);

-- Inserir uma cultura de teste --
INSERT INTO cultura (nome, trefle_id) VALUES
    ('Tomate', 269338);

-- Inserir condições ideais para a cultura de teste --
INSERT INTO condicoes_ideias (temperatura_min, temperatura_max, umidade_min, umidade_max, cultura_id) VALUES
    (20.0, 30.0, 50.0, 70.0, 1);

-- Inserir dados de temperatura e umidade fictícios 
INSERT INTO dados_periodicos (timestamp, temperatura, umidade, cultura_id) VALUES
    ('2024-02-11 08:00:00', 25.5, 60.2, 1),
    ('2024-02-11 09:00:00', 26.1, 59.8, 1),
    ('2024-02-11 10:00:00', 27.3, 57.6, 1),
    ('2024-02-11 11:00:00', 28.5, 55.3, 1),
    ('2024-02-11 12:00:00', 29.8, 53.1, 1);

-- Inserir um dado com imagem fictícia
INSERT INTO dados_periodicos (timestamp, temperatura, umidade, cultura_id, path_image) VALUES
    ('2024-02-11 13:00:00', 30.2, 52.0, 1, './imgs/greenhouse/example.jpg');

-- Inserir uma chave de API de teste --
INSERT INTO chave_api (chave, ativo) VALUES
    ('123456', TRUE);
