from record import Record
import sqlite3


class DatabaseInterface:
    """A database interface object that handles interactions with the DB"""

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)  # Connection to database
        self.cursor = self.conn.cursor()  # Our connection's cursor

    def create_table(self):
        # Create a new Table called 'music', with an artist and name field.
        with self.conn:
            self.cursor.execute(""" CREATE TABLE music (
                            artist text,
                            album text,
                            size integer,
                            location text
                            ) """)

    def insert_record(self, newRecord: Record):
        # Insert records into the database.
        artist = newRecord.get_artist()
        album = newRecord.get_record_name()
        size = newRecord.get_size()
        location = newRecord.get_location()

        with self.conn:
            self.cursor.execute("INSERT INTO music VALUES (:artist, :album, :size, :location)",
                                {'artist': artist, 'album': album, 'size': size, 'location': location})

    def remove_record(self, deletedRecord: Record):
        # Removes a record from the music Database.
        artist = deletedRecord.get_artist()
        album = deletedRecord.get_record_name()
        with self.conn:
            self.cursor.execute("DELETE from music WHERE artist = :artist AND album = :album",
                                {'artist': artist, 'album': album})

    def find_records_by_artist(self, artist: str):
        # Find every record with given artist name
        self.cursor.execute("SELECT * FROM music WHERE artist=:artist",
                            {'artist': artist})

        records = self.cursor.fetchall()
        return records

    def find_records_by_album(self, album: str):
        # Find every record with given album name
        self.cursor.execute("SELECT * FROM music WHERE album=:album",
                            {'name': album})

        records = self.cursor.fetchall()
        return records

    def find_specific_record(self, artist: str, album: str):
        # Find a single record with the given artist and album name.
        self.cursor.execute("SELECT * FROM music WHERE artist=:artist AND album = :album",
                            {'artist': artist, 'album': album})

        record = self.cursor.fetchone()
        return record

    def update_location(self, updatedRecord: Record):
        artist = updatedRecord.get_artist()
        album = updatedRecord.get_record_name()

        with self.conn:
            self.cursor.execute("""UPDATE music SET location = :newloc
                                WHERE artist = :artist AND album = :album""",
                                {'artist': artist, 'album': album})

    def close(self):
        # Closes the connection to the database
        self.conn.close()
