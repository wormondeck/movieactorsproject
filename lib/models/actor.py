from models.__init__ import CURSOR, CONN

class Actor:

    all_actors = {}
    
    def __init__(self, name, id=None):
        self.id = id
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Actor name must be a non-empty string")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS actor (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS actor;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO actor (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all_actors[self.id] = self

    @classmethod
    def create(cls, name):
        actor = cls(name)
        actor.save()
        return actor
    
    def update(self):
        sql = """
            UPDATE actor
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM actor
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all_actors[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        actor = cls.all_actors.get(row[0])
        if actor:
            actor.name = str(row[1]) if row[1] != '' else None

        else:
            actor = cls(row[1], row[0])
            cls.all_actors[actor.id] = actor
        return actor
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM actor
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM actor
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM actor
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def movies(self):
        from models.movie import Movie
        sql = """
            SELECT * FROM movie
            WHERE actor_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Movie.instance_from_db(row) for row in rows
        ]
