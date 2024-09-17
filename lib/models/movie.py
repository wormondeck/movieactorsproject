from models.__init__ import CURSOR, CONN
from models.actor import Actor

class Movie:

    all_movies = {}

    def __init__(self, movie, genre, actor_id, id=None):
        self.id = id
        self.movie = movie
        self.genre = genre
        self.actor_id = actor_id

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, movie):
        if isinstance(movie, str) and len(movie) > 0:
            self._movie = movie
        else:
            raise ValueError("Movie name must be a non-empty string")
    
    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str) and len(genre) > 0:
            self._genre = genre
        else:
            raise ValueError("Movie genre must be a non-empty string")
        
    @property
    def actor_id(self):
        return self._actor_id

    @actor_id.setter
    def actor_id(self, actor_id):
        if type(actor_id) is int and Actor.find_by_id(actor_id):
            self._actor_id = actor_id
        else:
            raise ValueError(
                "actor_id must reference a actor in the database")
        
    def _set_actor_id_from_db(self, actor_id):
        self._actor_id = actor_id
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS movie (
            id INTEGER PRIMARY KEY,
            movie TEXT,
            genre TEXT,
            actor_id INTEGER,
            FOREIGN KEY (actor_id) REFERENCES actor(id) ON DELETE CASCADE)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS movie;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO movie (movie, genre, actor_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.movie, self.genre, self.actor_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all_movies[self.id] = self

    def update(self):
        sql = """
            UPDATE movie
            SET movie = ?, genre = ?, actor_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.movie, self.genre,
                             self.actor_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM movie
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all_movies[self.id]

        self.id = None

    @classmethod
    def create(cls, movie, genre, actor_id):
        film = cls(movie, genre, actor_id)
        film.save()
        return film
    
    @classmethod
    def instance_from_db(cls, row):
        film = cls.all_movies.get(row[0])
        if film:
            film.movie = row[1]
            film.genre = row[2]
            film.actor_id = row[3]
        else:
            film = cls(row[1], row[2], row[3])
            film.id = row[0]
            cls.all_movies[film.id] = film
        return film
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM movie
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM movie
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, movie):
        sql = """
            SELECT *
            FROM movie
            WHERE movie is ?
        """

        row = CURSOR.execute(sql, (movie,)).fetchone()
        return cls.instance_from_db(row) if row else None