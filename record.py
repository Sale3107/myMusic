class Record:

    """A record object that holds information about it's name, artist name,
    record size, and where it is being stored in the collection"""

    def __init__(self, artist: str,
                 record_name: str, size: int, location: str):

        self.artist = artist
        self.record_name = record_name
        self.size = size
        self.location = location

    # Functions to return the information a Record holds.

    def get_artist(self) -> str:
        return self.artist

    def get_record_name(self) -> str:
        return self.record_name

    def get_size(self) -> int:
        return self.size

    def get_location(self) -> str:
        return self.location

    # End

    def format_for_output(self) -> str:
        # Generic method for creating a formatted string based of a database record.
        newString = """
        [Artist]: {art}
        [Album]: {alb}
        [Location]: {loc}\n
        """.format(art=self.get_artist(),
                   alb=self.get_record_name(),
                   loc=self.get_location())

        return newString
