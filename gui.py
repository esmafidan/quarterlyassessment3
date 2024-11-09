import sqlite3
import tkinter as tk
from tkinter import messagebox

class MCQApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Question Viewer")
        self.root.geometry("600x400")

        # Create a label for the title of the app
        self.title_label = tk.Label(self.root, text="Multiple Choice Questions", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Drop-down menu to select the course (table)
        self.course_label = tk.Label(self.root, text="Select Course")
        self.course_label.pack()
        self.course_var = tk.StringVar()
        self.course_menu = tk.OptionMenu(self.root, self.course_var, "DS4210", "DS3850", "DS4220", "DS3860", "DS3841")
        self.course_menu.pack()

        # Button to load questions based on selected course
        self.load_button = tk.Button(self.root, text="Load Questions", command=self.load_questions)
        self.load_button.pack(pady=10)

        # Label for the question (initially hidden)
        self.question_label = tk.Label(self.root, text="", font=("Arial", 12), wraplength=550)
        
        # Variables for the answer options (radio buttons)
        self.option_var = tk.StringVar(value="")  # Set the default value to empty string to prevent preselection

        # Radio buttons for answer options (initially hidden)
        self.option_a = tk.Radiobutton(self.root, text="A", variable=self.option_var, value="A")
        self.option_b = tk.Radiobutton(self.root, text="B", variable=self.option_var, value="B")
        self.option_c = tk.Radiobutton(self.root, text="C", variable=self.option_var, value="C")
        self.option_d = tk.Radiobutton(self.root, text="D", variable=self.option_var, value="D")

        # Button to submit the answer and move to the next question (initially hidden)
        self.submit_button = tk.Button(self.root, text="Submit Answer", command=self.submit_answer)

        # Store the current question and correct answer
        self.current_question = None
        self.correct_answer = None
        self.question_index = 0
        self.questions = []

    def load_questions(self):
        # Get the selected course (table name)
        course = self.course_var.get()
        if not course:
            messagebox.showerror("Error", "Please select a course.")
            return

        # Connect to the database and fetch all questions for the selected course
        conn = sqlite3.connect('quiz_questions.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {course}")  # Fetch all questions
        rows = cursor.fetchall()
        conn.close()

        if rows:
            self.questions = rows  # Store the questions
            self.question_index = 0  # Reset question index to 0
            self.show_question(self.question_index)  # Show the first question
            
            # Show the question widgets now that the quiz has started
            self.question_label.pack(pady=10)
            self.option_a.pack()
            self.option_b.pack()
            self.option_c.pack()
            self.option_d.pack()
            self.submit_button.pack(pady=10)

        else:
            messagebox.showinfo("No Questions", f"No questions found for {course}.")

    def show_question(self, index):
        # Display the current question and options
        if index < len(self.questions):
            row = self.questions[index]
            self.current_question = row
            self.question_label.config(text=row[1])  # Display the question
            self.option_a.config(text=f"A. {row[2]}")
            self.option_b.config(text=f"B. {row[3]}")
            self.option_c.config(text=f"C. {row[4]}")
            self.option_d.config(text=f"D. {row[5]}")
            self.correct_answer = row[6]  # Store the correct answer
        else:
            messagebox.showinfo("End of Questions", "You have completed all the questions!")
            self.reset_quiz()

    def submit_answer(self):
        # Check if the selected answer is correct
        selected_answer = self.option_var.get()
        if not selected_answer:
            messagebox.showerror("Error", "Please select an answer.")
            return

        # Provide feedback to the user
        if selected_answer == self.correct_answer:
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Wrong answer. The correct answer is {self.correct_answer}.")

        # Move to the next question
        self.question_index += 1
        self.show_question(self.question_index)

    def reset_quiz(self):
        # Reset the quiz state
        self.question_index = 0
        self.questions = []
        self.question_label.config(text="")
        self.option_var.set("")  # Reset the option_var to its initial empty state
        self.option_a.config(text="A")
        self.option_b.config(text="B")
        self.option_c.config(text="C")
        self.option_d.config(text="D")
        
        # Hide question-related widgets again
        self.question_label.pack_forget()
        self.option_a.pack_forget()
        self.option_b.pack_forget()
        self.option_c.pack_forget()
        self.option_d.pack_forget()
        self.submit_button.pack_forget()

# Set up the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MCQApp(root)
    root.mainloop()
