import tkinter as tk


class MusicCollectionGUI:
    def action_menu(self):
        action = tk.Tk()

        topText = tk.Label(
            text="Music Collection!",
            fg="black",
            bg="DarkGoldenrod1",
            width=50,
            height=2)

        topText.place(x=180, y=0)

        addRecord = tk.Button(action, text="Add Record", fg="black",
                              width=20, height=1, command=self.return_add_record)

        addRecord.place(x=190, y=40)
        removeRecord = tk.Button(action, text="Add Record", fg="black",
                                 width=20, height=1, command=self.return_add_record)

        removeRecord.place(x=190, y=40)

        action.title("Music Collection Database Tracker")
        action.geometry("500x500+500+200")
        action.mainloop()

    def create_add_record_window(self):
        # Window that is created when the add record button is left clicked.
        window = tk.Toplevel()

        artistLabel = tk.Label(window, text="Artist:",
                               fg="Black", bg="Navajowhite3", width=18, height=1)
        artistLabel.place(x=20, y=0)

        artistEntry = tk.Entry(window, text="Enter Artist here", bd=5)
        artistEntry.place(x=20, y=30)

        albumLabel = tk.Label(window, text="Album:",
                              fg="Black", bg="Navajowhite4", width=18, height=1)
        albumLabel.place(x=20, y=60)

        albumEntry = tk.Entry(window, text="Enter Album here", bd=5)
        albumEntry.place(x=20, y=80)

        recordType = tk.Label(window, text="Record Size:",
                              fg="White", bg="firebrick1",
                              width=18, height=1)
        recordType.place(x=20, y=115)

        v = tk.StringVar(window, "1")
        values = {"12 inch": "12",
                  "10 inch": "10",
                  "7 inch": "7"}

        count = 0
        for (text, value) in values.items():
            count += 1
            tk.Radiobutton(window, text=text, variable=v,
                           value=value).place(x=25, y=120 + (count * 25))

        recordLocation = tk.Label(window, text="Record Location:",
                                  fg="White", bg="CadetBlue4",
                                  width=18, height=1)
        recordLocation.place(x=150, y=0)

        v2 = tk.StringVar(window, "1")
        values2 = {"Main Box": "MainBox",
                   "Floor Box": "FloorBox",
                   "Other": "Other"}

        count2 = 0
        for (text, value) in values2.items():
            count2 += 1
            tk.Radiobutton(window, text=text, variable=v2,
                           value=value).place(x=150, y=10 + (count2 * 25))

        def addRecord(self):

        addNewRecord = tk.Button(window, text="Add New Record",
                                 fg="black", bg="honeydew3",
                                 width=12, height=1,
                                 command=addRecord)

        addNewRecord.bind('<Button-1>, addRecord')

        addNewRecord.place(x=20, y=300)

        window.title("Add New Record")
        window.geometry("400x400+450+150")
