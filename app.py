import csv
import random
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Load questions from CSV file
def load_questions(filename):
    questions = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if all(row[col].strip() for col in row):  # Check if all columns are non-empty
                questions.append(row)
    return questions

# Main Quiz Application class
class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.score = 0
        self.current_question_index = 0
        
        random.shuffle(self.questions)
        
        self.root.title("Exphil Quiz")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f0f0")

        # UI Elements
        self.title_label = tk.Label(root, text="Velkommen til Exphil Quiz!", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=15)

        self.progress_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0", fg="#666")
        self.progress_label.pack(pady=5)

        self.question_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief="groove", bd=2)
        self.question_frame.pack(pady=10, fill="both", expand=True)

        self.question_label = tk.Label(self.question_frame, text="", wraplength=600, font=("Helvetica", 14), bg="#ffffff", fg="#000")
        self.question_label.pack(pady=10)

        self.options = []
        for i in range(4):
            btn = tk.Button(self.question_frame, text="", font=("Helvetica", 12), bg="#e6e6e6", fg="#000", relief="raised", bd=2, wraplength=500, justify="left", anchor="w", command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5, fill="both")
            self.options.append(btn)

        self.next_button = tk.Button(root, text="Neste Spørsmål", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=20, command=self.next_question)
        self.next_button.pack(pady=20)

        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=f"Spørsmål {self.current_question_index + 1}: {question['question']}")
            
            options = [
                (question['option1'], question['reason1']),
                (question['option2'], question['reason2']),
                (question['option3'], question['reason3']),
                (question['option4'], question['reason4'])
            ]
            random.shuffle(options)
            
            self.current_options = options  # Store the shuffled options with reasons
            
            for idx, (option, reason) in enumerate(options):
                self.options[idx].config(text=option, bg="#e6e6e6")

            # Update progress label
            self.progress_label.config(text=f"Spørsmål {self.current_question_index + 1} av {len(self.questions)}")
        else:
            self.show_results()

    def check_answer(self, selected_index):
        question = self.questions[self.current_question_index]
        correct_answer = question['option1']
        selected_answer = self.options[selected_index].cget("text")

        if selected_answer.strip().lower() == correct_answer.strip().lower():
            self.options[selected_index].config(bg="green")
            messagebox.showinfo("Riktig!", f"Riktig svar! {question['reason1']}")
            self.score += 1
        else:
            messagebox.showerror("Feil", f"{self.current_options[selected_index][1]}")

    def next_question(self):
        self.current_question_index += 1
        self.display_question()

    def show_results(self):
        messagebox.showinfo("Resultater", f"Quiz ferdig! Din poengsum: {self.score}/{len(self.questions)}")
        self.root.quit()

if __name__ == "__main__":
    filename = 'generated_questions1.csv'
    questions = load_questions(filename)

    root = tk.Tk()
    app = QuizApp(root, questions)
    root.mainloop()
