# Importing the necessary libraries
import tkinter as tk

# Creating the main window
root = tk.Tk()

# Setting the window size
root.geometry('800x600')

# Disabling the maximize button
root.resizable(False, False)

# Setting the window background color
root.configure(bg='black')

# Creating a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Creating a File menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open")
file_menu.add_command(label="Exit", command=root.quit)

# Creating a label to display the 'Sony Computer Entertainment' text
label = tk.Label(root, text='PS1 BIOS Sony Computer Entertainment', bg='black', fg='white', font=('Helvetica', 16))
label.pack()

# Creating a canvas to display the N64 logo
canvas = tk.Canvas(root, width=200, height=200, bg='black')
canvas.pack()

# Drawing the N64 logo on the canvas
# Note: This is a simplified version of the N64 logo
canvas.create_polygon(100, 0, 200, 100, 100, 200, 0, 100, fill='red')

# Creating a status bar
status = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

# Running the GUI
root.mainloop()
