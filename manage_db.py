import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class SocialDB:

    def __init__(self):
        self.con = sqlite3.connect('blueit.db')
        self.con.row_factory = dict_factory 
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.commit()
        self.con.close()

    def addPerson(self, name, username): 
        self.cur.execute('INSERT INTO people (name, username) VALUES (?, ?)', [name, username])

    def addPost(self, user, content):
        un = self.un2id(user)
        self.cur.execute('INSERT INTO posts (user_id, content) VALUES (?, ?)', [un, content])

    def circles(self, user, count):
        un = self.un2id(user)
        self.cur.execute('''WITH RECURSIVE circles(fromi, following, n) AS (
                 SELECT from_id, following_id, 0
                 FROM following
                 WHERE from_id = ?
                UNION
                 SELECT A.following, B.following_id, n+1 
                 FROM circles A JOIN following B
                 ON A.following = B.from_id
                 WHERE A.n < ?
            )
                 SELECT people.id, people.username, MIN(n)+1 AS degree
                 FROM circles JOIN people
                 ON circles.following = people.id
                 GROUP BY circles.following
                UNION
                 SELECT people.id, people.username, 0 AS degree
                 FROM people
                 WHERE people.id = ?
                ORDER BY degree;
        ''', [un, count, un])
        circles = self.cur.fetchall()
        return circles


    def comment(self, un, post, content):
        user = self.un2id(un)
        self.cur.execute('INSERT INTO comments (user_id, post_id, content) VALUES (?, ?, ?)', [user, post, content])

    def following(self, from_un, following_un):
        from_id = self.un2id(from_un)
        following_id = self.un2id(following_un)
        self.cur.execute('INSERT INTO following (from_id, following_id) VALUES (?, ?)', [from_id, following_id])

    def getFeed(self, un, count):
        user = self.un2id(un)
        self.cur.execute('SELECT posts.id, people.username, posts.content, posts.date_created FROM following JOIN posts ON following_id = posts.user_id JOIN people ON posts.user_id = people.id WHERE from_id = ? ORDER BY posts.date_created DESC LIMIT ?', [user, count])
        feed = self.cur.fetchall()
        return feed

    def getComments(self, post):
        #self.cur.execute('SELECT * FROM following JOIN posts ON following_id = posts.user_id WHERE from_id = ? ORDER BY posts.date_created DESC', [post, post])
        self.cur.execute('''WITH RECURSIVE replies( main, level, username, content, date_created ) AS (
             SELECT comments.id, 0, username, content, comments.date_created 
             FROM comments JOIN people
             ON user_id = people.id
             WHERE reply_id IS NULL AND post_id = ?
            UNION ALL
             SELECT comments.id, replies.level+1, people.username, comments.content, comments.date_created
             FROM comments JOIN replies
             ON main = comments.reply_id
             JOIN people 
             ON comments.user_id = people.id
             WHERE comments.post_id = ?
             ORDER BY 2 DESC
        )
        SELECT * 
        FROM replies;''', [post,post])
        comments = self.cur.fetchall()
        return comments

    def like(self, un, post):
        user = self.un2id(un)
        self.cur.execute('INSERT INTO likes (user_id, post_id) VALUES (?, ?)', [user, post])

    def reply(self, un, post, repl, content):
        user = self.un2id(un)
        self.cur.execute('INSERT INTO comments (user_id, post_id, reply_id, content) VALUES (?, ?, ?, ?)', [user, post, repl, content])

    def un2id(self, un):
        self.cur.execute('SELECT id FROM people WHERE username = ?', [un]) 
        ide = self.cur.fetchone()["id"]
        return ide

    def wipeTables(self):
        self.cur.execute('DELETE FROM people')
        self.cur.execute('DELETE FROM following')
        self.cur.execute('DELETE FROM posts')
        self.cur.execute('DELETE FROM comments')
        self.cur.execute('DELETE FROM likes')


