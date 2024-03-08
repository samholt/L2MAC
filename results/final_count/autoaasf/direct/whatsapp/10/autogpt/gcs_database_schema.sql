CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

CREATE TABLE profiles (
  user_id INTEGER PRIMARY KEY REFERENCES users(id),
  display_name VARCHAR(255),
  bio TEXT,
  avatar_url VARCHAR(255),
  last_seen TIMESTAMP
);

CREATE TABLE contacts (
  user_id INTEGER REFERENCES users(id),
  contact_id INTEGER REFERENCES users(id),
  PRIMARY KEY (user_id, contact_id)
);