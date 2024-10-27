import csv
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os
import sys

# Load questions from CSV file
def load_questions(filename):
    questions = []
    print("f", filename)
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            print(row)
            if row['question'] and row['option1'] and row['option2'] and row['option3'] and row['option4']:
                questions.append(row)
    return questions

def load_all_questions(data_folder):
    all_questions = []
    print("Current working directory:", os.getcwd())
    data_folder = os.path.join(os.getcwd(), data_folder)
    for filename in os.listdir(data_folder):
        if filename.endswith('.csv'):
            filepath = os.path.join(data_folder, filename)
            all_questions.extend(load_questions(filepath))
    return all_questions

# Main Quiz Application class
class QuizApp:
    def __init__(self, root, questions, immediate_feedback):
        self.root = root
        self.questions = questions
        self.immediate_feedback = immediate_feedback
        self.score = 0
        self.current_question_index = 0
        self.answers_summary = []  # To store answers for end summary
        
        random.shuffle(self.questions)
        
        self.root.title("Exphil Quiz")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f0f0")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close_keep_results)

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
                self.options[idx].config(text=option, bg="#e6e6e6", state=tk.NORMAL)

            # Update progress label
            self.progress_label.config(text=f"Spørsmål {self.current_question_index + 1} av {len(self.questions)}")
        else:
            self.show_results()

    def check_answer(self, selected_index):
        question = self.questions[self.current_question_index]
        correct_answer = question['option1']
        selected_answer = self.options[selected_index].cget("text")

        # Disable all options after selecting an answer
        for btn in self.options:
            btn.config(state=tk.DISABLED)

        correct = selected_answer.strip().lower() == correct_answer.strip().lower()
        if self.immediate_feedback:
            if correct:
                self.options[selected_index].config(bg="green")
                messagebox.showinfo("Riktig!", f"Riktig svar! {question['reason1']}")
            else:
                self.options[selected_index].config(bg="red")
                messagebox.showerror("Feil", f"{self.current_options[selected_index][1]}")
        else:
            # Do not change color if immediate feedback is off
            pass
        
        if correct:
            self.score += 1
        
        self.answers_summary.append({
            'question': question['question'],
            'selected_answer': selected_answer,
            'correct_answer': correct_answer,
            'reason': question['reason1'] if correct else self.current_options[selected_index][1]
        })

    def next_question(self):
        self.current_question_index += 1
        self.display_question()

    def show_results(self):
        result_window = tk.Toplevel(self.root)
        result_window.title("Oppsummering av resultater")
        result_window.geometry("1000x800")
        result_frame = tk.Frame(result_window, bg="#ffffff", padx=20, pady=20)
        result_frame.pack(fill="both", expand=True)

        # Use a Text widget for better readability of long paragraphs
        result_text = tk.Text(result_frame, wrap="word", font=("Helvetica", 12), bg="#ffffff", fg="#000")
        result_text.pack(pady=10, padx=10, fill="both", expand=True)
        
        for answer in self.answers_summary:
            result_text.insert(tk.END, f"Spørsmål: {answer['question']}\n")
            result_text.insert(tk.END, f"Ditt svar: {answer['selected_answer']}\n")
            result_text.insert(tk.END, f"Riktig svar: {answer['correct_answer']}\n")
            result_text.insert(tk.END, f"Begrunnelse: {answer['reason']}\n\n")
        
        result_text.config(state=tk.DISABLED)

        messagebox.showinfo("Resultater", f"Quiz ferdig! Din poengsum: {self.score}/{len(self.questions)}")
        restart = messagebox.askyesno("Start på nytt?", "Vil du starte quizen på nytt?")
        if restart:
            self.restart_quiz()
        else:
            # Keep result window open
            pass

    def restart_quiz(self):
        self.score = 0
        self.current_question_index = 0
        self.answers_summary = []
        self.questions = random.sample(all_questions, len(self.questions))
        random.shuffle(self.questions)
        self.display_question()

    def on_close_keep_results(self):
        self.root.quit()
        # Do nothing to keep the results window open

if __name__ == "__main__":
    data_folder = 'generated_question_folder'
    all_questions = load_all_questions(data_folder)

    root = tk.Tk()
    # Create a more visually appealing initial dialog window
    start_frame = tk.Frame(root, padx=20, pady=20, bg="#f0f0f0")
    start_frame.pack(fill="both", expand=True)
    
    title_label = tk.Label(start_frame, text="Velkommen til Exphil Quiz!", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
    title_label.pack(pady=15)
    
    num_questions_label = tk.Label(start_frame, text="Hvor mange spørsmål ønsker du å svare på?", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
    num_questions_label.pack(pady=5)
    
    num_questions_spinbox = tk.Spinbox(start_frame, from_=1, to=len(all_questions), width=5, font=("Helvetica", 12))
    num_questions_spinbox.pack(pady=5)
    
    def start_quiz():
        num_questions = int(num_questions_spinbox.get())
        immediate_feedback = messagebox.askyesno("Velg modus", "Ønsker du å se om svaret ditt er riktig umiddelbart?")
        selected_questions = random.sample(all_questions, num_questions)
        app = QuizApp(root, selected_questions, immediate_feedback)
        start_frame.destroy()

    start_button = tk.Button(start_frame, text="Start Quiz", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", command=start_quiz)
    start_button.pack(pady=15)
    
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()
    sys.exit()