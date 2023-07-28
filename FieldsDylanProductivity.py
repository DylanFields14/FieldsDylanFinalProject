from tkinter import * #imports all classes, functions, and constants from tkinter
from tkinter.font import Font #allows you to customize fonts 
from PIL import ImageTk, Image # allows you to use images
from tkinter import messagebox #provides functions for displaying popup messages
from datetime import datetime # allows you to work with times and dates


splash_shown = False #This variable keeps track of whether the splash screen has been shown or not. Indicating initially, that the splash hasn't been displayed yet.
main_window_created = False #This variable keeps track of whether the main window has been created or not. Indicates that it hasn't been shown initially. 
splash_root = None # Since the splash screen is displayed as a separate root window, this variable is initially set to none. Later it will be assigned the reference to the splash screen's Tk instance when its created.

def main_window():
    global main_window_created
    if not main_window_created:
        root = Tk() # creates the main window
        root.title('Home Page') # Sets the title of window
        root.geometry("500x500") # Sets the size of the window
        splash_root.withdraw() #hides the splash screen
        def exit_program():  # exit variable to close out the window
            root.destroy() # destroy the root window
            splash_root.destroy() # destroy the splash screen if its still up
            exit() #exit
        btn = Button(root, text="Open To-do-List", command=todo) #button to open to-do list
        btn2= Button(root, text="Journal", command=journal) #button to open the journal
        exit_button = Button(root, text="Exit", command=exit_program) # button to exit the program
        btn.pack() # makes the button appear
        btn2.pack() # makes the button appear 
        exit_button.pack()
        root.mainloop() # enters the main event loop for the main window



# This is my to-do list. It allows for entry of to-do items and allows you to delete, add, cross, and uncross. 
def todo(): 
    todo_window = Toplevel() # Creates a new window for the To-Do list
    todo_window.title('Productivity Manager') # Sets the title of the window
    todo_window.geometry("500x500") # Size of main window
    my_font = Font(family="Comic Sans", size=25, weight="bold") # What font I want to use 
    frame = Frame(todo_window) # Creates a frame for the to-do window
    frame.pack(pady=10) # Adds some padding to the frame
    todo_list = Listbox(frame, font=my_font, width=25, height=5, bd=5, fg="#464646",) #The box for the items that you need to-do
    
    todo_list.pack(side=LEFT, fill=BOTH) # Packs the listbox to the left side of the frame with both
    placeholder = ["Insert To-Do List"] #placeholder text for the initial listbox display
    for item in placeholder:
        todo_list.insert(END, item)
        
    #Create Scrollbar 
    scrollbar = Scrollbar(frame) # Where I am putting the scrollbar
    scrollbar.pack(side=RIGHT, fill=BOTH) # The position of the scrollbar 
    # Add Scrollbar
    todo_list.config(yscrollcommand=scrollbar.set) # connects the scrollbar to the listbox's yview command 
    scrollbar.config(command=todo_list.yview) # connects the scrollbar's command to the listbox's yview
    #Create the entry box to add items to To-do
    entry = Entry(todo_window, font=("Helvetica", 18)) # Creates the entry widget for input and makes the font
    entry.pack(pady=20) # adds padding to entry widget 

#Function for deleting, adding, uncrossing, and crossing off items. 
    button_frame = Frame(todo_window)
    button_frame.pack(pady=20)
    # Functions for deleting, adding, uncrossing, and crossing off items. 
    def delete_item(): #delets the selected item from the listbox
        todo_list.delete(ANCHOR)
    def add_item(): # adding an item to the box, underneath is also some code for the error message. 
        item_text = entry.get().strip()
        if item_text: #if else statement to see if there is something in the text box or not. 
            todo_list.insert(END, entry.get()) 
            entry.delete(0, END)
        else:
            error_message = "Error: Please fill in the item field" #Error message pop up that says to fill in the field. 
            messagebox.showerror("Error", error_message)
    def cross_off():
        #cross off item
        todo_list.itemconfig(todo_list.curselection(), fg="#dedede")
        todo_list.selection_clear(0, END)
    def uncross(): # uncross off the selected item by changing its color back to normal 
        todo_list.itemconfig(todo_list.curselection(), fg='#464646')
        todo_list.selection_clear(0, END)


    #Add buttons
    delete_button = Button(button_frame, text="Delete Item", command=delete_item) #Button to delete
    add_button = Button(button_frame, text="Add Item", command=add_item) # Button to add
    cross_button = Button(button_frame, text="Cross Off Item", command=cross_off) # Button to cross-off
    uncross_button = Button(button_frame, text="Uncross Item", command=uncross) # Button to uncross
    add_button.grid(row=0, column=0)  # Positions the add button
    delete_button.grid(row=0, column=1, padx=20) # Positions to delete button
    cross_button.grid(row=0, column=2) #positions the cross button
    uncross_button.grid(row=0, column=3, padx=20) # Positions the uncross
    back_frame = Frame(todo_window)  # creates a new frame 
    back_frame.pack(pady=10) #displays the back_frame in the todo_window with a padding
    def go_back(): # a function that lets you go back to the main window
        todo_window.destroy() # Destroys the todo_window
    back_button = Button(back_frame, text="Back To Home", command=go_back) #creates the button to go back to the main screen with the function go_back
    back_button.pack() #displays the button.
    
def validate_date(date_str): #checks if the date was inputted correctly
    try:
        datetime.strptime(date_str, '%m-%d-%Y') #what type of Date format you should use
        return True #if the date is successful, it returns true, showing that the data was input correctly
    except ValueError: #If an issue occurs during the date formatting, the function returns false, indicating an invalid format
        return False # see above

# Journal Function, it is my function for a user to write about their day/thoughts/or anything they want to. It has been proven to decrease stress, depression, and anxiety.
def journal():
    journal_window = Toplevel() #creates a new window for the journal 
    journal_window.title('Journal') #sets the title of the window
    journal_window.geometry("800x800") #sets the size of the window

    def set_background_image():
        bg_image_path = "wood.jpeg" # path of the photo
        bg_image = Image.open(bg_image_path) # open the background image
        bg_photo = ImageTk.PhotoImage(bg_image) #tkinter get photo
        bg_label = Label(journal_window, image=bg_photo) # creates a label with background image
        bg_label.image = bg_photo  # Keep a reference to the image to prevent garbage collection
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Set label size to fill the entire window
    set_background_image()
    

# Function to go back to the main window
    def go_back():
        journal_window.destroy() #closes the journal window
        
#function to save the journal 
    def save_entry(): 
        date = date_entry.get() #box for date
        title = title_entry.get() #box for title
        journal = journal_text.get("1.0", END).strip()#box for text

        if not date or not title or not journal: # A function to make error popups if all fields are not shown
            messagebox.showerror("Error", "Please fill all fields")
            return
        elif not validate_date(date):
            messagebox.showerror("Error", "Invalid date format. Please use MM-DD-YYYY") #shows an error message if date field is input incorrectly
            return
        else: #save the entry if all fields are filled
            date_entry.delete(0, END) #allows you to delete date
            title_entry.delete(0, END) #allows you to delete title
            journal_text.delete("1.0", END)  #allows you to delete text

        with open("diary_entries.txt", "a") as file:
            file.write(f"Date: {date}\n")
            file.write(f"Title: {title}\n")
            file.write(f"Journal: {journal}\n")
            file.write("-" * 20 + "\n")  # Separator between entries

    def show_entries(): #open window to see previous saved entries
        entries_window = Toplevel() #makes a new window 
        entries_window.title('Previous Entries') # title of new window
        entries_window.geometry("800x800") # the dimensions of the window

        
        # Read previous entries from the file (if they were saved to a file)
        try:
            with open("diary_entries.txt", "r") as file: #gives you an error message if nothing saved.
                entries = file.read()
                entry_date = ""
                entry_title = ""
                entry_journal = ""
                formatted_entries = ""
                #iterate through the lines and extract date, title, and journal entry
            for line in entries: 
                if line.startswith("Date:"): # # Assign the line (without leading/trailing spaces) to the 'entry_date' variable.
                    entry_date = line.strip()
                elif line.startswith("Title:"): # Assign the line (without leading/trailing spaces) to the 'entry_title' variable.
                    entry_title = line.strip()
                elif line.startswith("Journal:"): # Assign the line (without leading/trailing spaces) to the 'entry_journal' variable.
                    entry_journal = line.strip()
                elif line.startswith("--------------------"):  # Separator between entries
                    # Append the formatted entry to the result string
                    formatted_entries += f"{entry_date}\n{entry_title}\n{entry_journal}\n\n"
                    # Reset the variables for the next entry to empty strings.
                    entry_date = "" 
                    entry_title = ""
                    entry_journal = ""
                if entry_date and entry_title and entry_journal: 
                    formatted_entries += f"{entry_date}\n{entry_title}\n{entry_journal}\n\n"  # Append the formatted entry (date, title, and journal) to the 'formatted_entries' string.
        except FileNotFoundError:
            entries = "No entries found." #if you have no previous entries, this shows up.

        entries_text = Text(entries_window, font=("Helvetica", 12)) # creates a new text widget using the Helvetica font in size 12
        entries_text.pack(fill=BOTH, expand=True) # makes the widget appear and adjusts it to fill space in both directions 
        entries_text.insert("1.0", entries) #inserts the content of the "entries" variable.
        entries_text.config(state=DISABLED) #Disables the text widget to prevent user modification


    date_label = Label(journal_window, text="Date:")
    date_label.pack(pady=5) #makes the button appear on the window with a padding of 5

    date_entry = Entry(journal_window, font=("Helvetica", 14))
    date_entry.pack(pady=5) #makes the button appear on the window with a padding of 5

    title_label = Label(journal_window, text="Title:")
    title_label.pack(pady=5) #makes the button appear on the window with a padding of 5

    title_entry = Entry(journal_window, font=("Helvetica", 14))
    title_entry.pack(pady=5) #makes the button appear on the window with a padding of 5 

    journal_label = Label(journal_window, text="Journal:")
    journal_label.pack(pady=5) #makes the button appear on the window with a padding of 5

    journal_text = Text(journal_window, font=("Helvetica", 12), wrap=WORD) #creates a text widget with the font of 12/Helvetica, allowing the text to  wrap within the boundaries.
    journal_text.pack(fill=BOTH, expand=True)

    save_button = Button(journal_window, text="Save Entry", command=save_entry)
    save_button.pack(side="bottom", fill="both", pady=10) #makes the button appear on the window with a padding of 10
 
    show_entries_button = Button(journal_window, text="Show Previous Entries", command=show_entries) 
    show_entries_button.pack(side="bottom", fill="both", pady=5) #makes the button appear on the window with a padding of 5

    exit_button = Button(journal_window, text="Back To Home", command=go_back) # Button to go back to main window 
    exit_button.pack(side="bottom", fill="both", pady=5) #makes the button appear on the window with a padding of 5




def show_splash(): # Show splash screen 
    global splash_shown, main_window_created
    splash_shown = True #makes the splash_shown variable true. 
    splash_root.deiconify() #makes the splash screen visiblee
    splash_root.after(2000, main_window) # Make the splash screen appear for only 2 seconds and then go to the main window. 


# Create the splash screen as the main root window
splash_root = Tk() # creates the main root window for the splash screen
splash_root.title("Productivity!") # Titles the splash root
splash_root.overrideredirect(True) # Remove window borders and title bar 
splash_root.geometry("500x300+500+200") # Sets the size and position of the splash window

splash_label = Label(splash_root, font=("Helvetica", 18)) 
splash_label.pack(pady=20)
splash_image = ImageTk.PhotoImage(Image.open("product.jpg")) #loads an image onto the splash screen.
image_label = Label(splash_root, image=splash_image) #creates a widget in the splash root window and displays the splash image.
image_label.pack() #makes the label appear

splash_root.after(0, show_splash) #immediately open the splash root

# Call the mainloop for the splash screen
splash_root.mainloop()
