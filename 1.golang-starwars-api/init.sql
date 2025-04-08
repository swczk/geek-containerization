CREATE TABLE IF NOT EXISTS characters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(50) NOT NULL,
    homeworld VARCHAR(50) NOT NULL,
    birth_year VARCHAR(20),
    force_user BOOLEAN NOT NULL DEFAULT false
);

-- Insert initial characters
INSERT INTO characters (name, species, homeworld, birth_year, force_user)
VALUES
('Luke Skywalker', 'Human', 'Tatooine', '19 BBY', true),
('Leia Organa', 'Human', 'Alderaan', '19 BBY', true),
('Han Solo', 'Human', 'Corellia', '32 BBY', false),
('Chewbacca', 'Wookiee', 'Kashyyyk', '200 BBY', false),
('Darth Vader', 'Human', 'Tatooine', '41.9 BBY', true),
('Yoda', 'Unknown', 'Unknown', '896 BBY', true),
('R2-D2', 'Droid', 'Naboo', 'Unknown', false),
('C-3PO', 'Droid', 'Tatooine', 'Unknown', false),
('Obi-Wan Kenobi', 'Human', 'Stewjon', '57 BBY', true),
('Boba Fett', 'Human', 'Kamino', '31.5 BBY', false);
