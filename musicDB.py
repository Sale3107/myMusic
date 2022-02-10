from record import Record
from DatabaseInterface import DatabaseInterface
# from gui import MusicCollectionGUI

myRecord = Record('Slowdive', 'Just For A Day', '12', 'MainBox')

interface = DatabaseInterface('musicCollection.db')
# interface.create_table()

# Adding records: interface.insert_record(arg1 -> Record)
# Removing records: interface.remove_record(arg1 -> Record)
# Finding records by artist name: interface.find_records_by_artist(arg1 -> str)
# Finding records by album name: interface.find_records_by_album(arg1 -> str)

# You should Close the database connection once you are finished with it:
# interface.close()


def get_artist_and_album():
    # Function to prompt the user to input an artist and album name
    artist = input("Artist: ")
    album = input("Album name: ")

    return (artist, album)


while True:
    action = input(
        """\n    [1] Add New Record
    [2] Remove a Record
    [3] Find a Record (Artist + Album)
    [4] Find all Records: by Artist
    [5] Find all Records: by Album Name
    [6] Return all records
    [CLOSE] Close connection to musicCollection.db
    [#] ~""")

    if action == "1":
        artist = input("Artist: ")
        album = input("Album name: ")
        size = input('Record size (12", 10", 7"): ')
        location = input('Location (MainBox, FloorBox, Other): ')
        newRecord = Record(artist, album, size, location)
        try:
            interface.insert_record(newRecord)
            print("Record Added!")
        except:
            print("Record could not be added.")
    elif action == "2":
        args = get_artist_and_album()
        try:
            interface.remove_record(args[0], args[1])
            print("{album}, by {artist} has been removed from the database...".format(
                artist=args[0], album=args[1]))
        except:
            print("Record Not Found.")
    elif action == "3":
        args = get_artist_and_album()
        print(interface.find_specific_record(args[0], args[1]))
    elif action == "4":
        artist = input("Artist name: ")
        print(interface.find_records_by_artist(artist))
    elif action == "5":
        album = input("Album name: ")
        print(interface.find_records_by_album(album))
    elif action == "6":
        all_records = interface.get_all_records()
        for item in all_records:
            record = Record(item[0], item[1], item[2], item[3])
            print(record.format_for_output())
    elif action.upper() == "CLOSE":
        break


interface.close()
