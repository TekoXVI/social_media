# 4307-socmedia
## Preston & Ian

## GUIDE
The database management is condensed within a class. If you want to directly interact with it using the commands, import manage\_db.py, init a SocialDB object and continue from there. The object will automatically commit and close the session upon deconstruction.

The file scripts.py provides an automated demonstration that prepopulates the tables and shows the content of the three main SELECT commands.

## SCHEMA	

```sql
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
```

## COMMANDS

Method		| Arguments | Function
----------------|-----------|----------------------
addPerson	| Name (string), Username (string) | Create a new user with their name and username
addPost		| Username (string), Content (string) | Create a new post for a user with their name and the post content
circles		| Username (string), Count (integer) | Fetch all users that are followed by a specified user's followed creators, up to a certain degree of separation.
comment		| Username (string), Post (integer), Content (String) | Comments on another user's post
following	| Current User (string), Followed User (string) | Follow another user
getFeed		| Username (string), Post Count (integer) | Get a specified number of posts from a users followed creators
getComments	| Post (integer) | Get all comment threads underneath a specified post
like		| Username (string), Post (integer) | Add specified post to a user's likes.
reply		| Username (string), Post (integer), Comment ID (integer), Content (string) | Respond to another user's comment underneath a post.
un2id		| Username (string) | Convert provided username to the associated user id
wipeTables 	| NULL | Clear all rows from all tables to work with a completely empty database.
