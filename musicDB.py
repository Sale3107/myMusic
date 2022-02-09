from record import Record
from DatabaseInterface import DatabaseInterface
from gui import MusicCollectionGUI
import tkinter as tk

myRecord = Record('MOVLP354', 'Slowdive', 'Just For A Day', '12', 'MainBox')

interface = DatabaseInterface('musicCollection.db')
interface.close()

# Adding records: interface.insert_record(arg1 -> Record)
# Removing records: interface.remove_record(arg1 -> Record)
# Finding records by artist name: interface.find_records_by_artist(arg1 -> str)
# Finding records by album name: interface.find_records_by_album(arg1 -> str)

# You should Close the database connection once you are finished with it:
# interface.close()

myGUI = MusicCollectionGUI()
action = myGUI.action_menu()
