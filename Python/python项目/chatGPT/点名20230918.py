import tkinter as tk
import random

# Create a new window
window = tk.Tk()
window.title("Roll Call")

# Create a list of students
students = ["Alice", "Bob", "Charlie", "David", "Eve"]


# Define the roll_call function
def roll_call():
    # Randomly select a student from the list of students
    student = random.choice(students)

    # Display the student's name in the label
    label.config(text=student)

    # Remove the student from the list of students
    students.remove(student)

    # If there are still students left in the list, start the roll call again
    if students:
        roll_call()


# Create a label to display the current student
label = tk.Label(window, text="Current Student:")
label.pack()

# Create a button to start the roll call
button = tk.Button(window, text="Start Roll Call", command=roll_call)
button.pack()

# Create a listbox to display the list of students
listbox = tk.Listbox(window, height=5, width=20)
for student in students:
    listbox.insert(tk.END, student)
listbox.pack()

# Create a scrollbar to scroll through the list of students
scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Start the roll call
roll_call()

# Run the window
window.mainloop()