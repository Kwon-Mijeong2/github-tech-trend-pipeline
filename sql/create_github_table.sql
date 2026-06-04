CREATE TABLE IF NOT EXISTS github_trending (

    id SERIAL PRIMARY KEY,

    repository VARCHAR(255),

    language VARCHAR(100),

    stars INTEGER,

    collected_date DATE
);