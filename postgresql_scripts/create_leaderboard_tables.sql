CREATE TABLE my_leaderboard (
    segment_id INTEGER PRIMARY KEY,
    rank INTEGER NOT NULL,
    total_entries INTEGER NOT NULL,
    num_attempts INTEGER NOT NULL,
    read_date TIMESTAMP NOT NULL
);
