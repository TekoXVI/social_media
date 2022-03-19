CREATE TABLE people (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	username TEXT NOT NULL UNIQUE,
	date_created DATE NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE following (
	from_id INTEGER NOT NULL,
	following_id INT NOT NULL REFERENCES people (id),
	date_created DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (from_id, following_id),
	FOREIGN KEY (from_id) REFERENCES people (id)
);
CREATE TABLE posts (
	id INTEGER PRIMARY KEY,
	user_id INT NOT NULL,
	content TEXT NOT NULL,
	date_created DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES people (id)
);
CREATE TABLE comments (
	id INTEGER PRIMARY KEY,
	user_id INT NOT NULL,
	post_id INT NOT NULL,
	reply_id INT,
	content TEXT NOT NULL,
	date_created DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES people (id),
	FOREIGN KEY (post_id) REFERENCES posts (id)
);
CREATE TABLE likes (
	id INTEGER PRIMARY KEY,
	user_id INT NOT NULL,
	post_id INT NOT NULL,
	date_created DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES people (id),
	FOREIGN KEY (post_id) REFERENCES posts (id)
);
