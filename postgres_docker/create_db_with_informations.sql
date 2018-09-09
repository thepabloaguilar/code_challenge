CREATE TABLE user_login(
    id              SERIAL,
    username        VARCHAR,
    password        VARCHAR,
    creation_date   TIMESTAMP DEFAULT NOW(),
    CONSTRAINT pk_users PRIMARY KEY(id)
);

INSERT INTO user_login(username, password)
VALUES ('teste', '$pbkdf2-sha256$29000$z5lz7l0LwVgLoVRK6b2XMg$jTqFf9L8Q1vGZjTpXkaHechcFQJ.2OZIlR12vTfV6Io');

CREATE TABLE customer(
    id                  SERIAL,
    customer_name       VARCHAR,
    customer_address    VARCHAR,
    tax_id              VARCHAR,
    gender              CHAR(1),
    creation_date       TIMESTAMP DEFAULT NOW(),
    CONSTRAINT pk_customer PRIMARY KEY(id)
);

INSERT INTO customer(customer_name, customer_address, tax_id, gender)
VALUES
    ('Luke Skywalker', 'Tatooine', 'f7bc221a-3dca-43b3-bc71-2704e9815fd4', 'M'),
    ('Leia Organa', 'Alderaan', '0e3a25d0-b2d9-11e8-96f8-529269fb1459', 'F'),
    ('Owen Lars', 'Tatooine', '39729a84-b2d9-11e8-96f8-529269fb1459', 'M'),
    ('Beru Whitesun lars', 'Tatooine', '5c4b34ee-b2d9-11e8-96f8-529269fb1459', 'F');

CREATE TABLE business(
    id              SERIAL,
    business_name   VARCHAR,
    CONSTRAINT pk_business PRIMARY KEY(id)
);

INSERT INTO business(business_name)
VALUES
    ('A New Hope'),
    ('Attack of the Clones'),
    ('The Phantom Menace'),
    ('Revenge of the Sith'),
    ('Return of the Jedi'),
    ('The Empire Strikes Back'),
    ('The Force Awakens');

CREATE TABLE debt(
    id              SERIAL,
    customer_id     INTEGER,
    business_id     INTEGER,
    description     VARCHAR,
    amount          NUMERIC(16, 6),
    payment_date    DATE,
    expiry_date     DATE,
    CONSTRAINT pk_debt PRIMARY KEY(id),
    CONSTRAINT fk_debt_customer_id FOREIGN KEY(customer_id) REFERENCES customer(id),
    CONSTRAINT fk_debt_business_id FOREIGN KEY(business_id) REFERENCES business(id)
);

INSERT INTO debt(customer_id, business_id, description, amount, payment_date, expiry_date)
VALUES
    (1, 5, 'Sand Crawle', 150000.00, NULL, NOW()),
    (1, 6, 'T-16 skyhopper', 14500.00, NOW() - INTERVAL '1 day', NOW()),
    (2, 7, 'X-34 landspeeder', 10550.00, NOW() - INTERVAL '3 day', NOW()),
    (2, 2, 'Storm IV Twin-Pod cloud car', 75000.00, NOW() - INTERVAL '5 day', NOW()),
    (2, 3, 'Sail barge', 285000.00, NOW() - INTERVAL '2 day', NOW()),
    (3, 3, 'Bantha-II cargo skiff', 8000.00, NULL, NOW()),
    (4, 3, 'Imperial Speeder Bike', 8000.00, NULL, NOW()),
    (4, 4, 'Multi-Troop Transport', 138000.00, NULL, NOW()),
    (4, 4, 'Single Trooper Aerial Platform', 2500.00, NOW() - INTERVAL '10 day', NOW()),
    (4, 4, 'C-9979 landing craft', 200000.00, NOW() - INTERVAL '6 day', NOW());