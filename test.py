import csv
import random

def load_questions(filename):
    questions = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if all(row[col].strip() for col in row):  # Check if all columns are non-empty
                questions.append(row)
    return questions

def quiz_user(questions, n):
    score = 0
    random.shuffle(questions)  # Shuffle the questions list
    for i in range(n):
        question = questions[i]
        print(f"\n{'-'*40}\nSpørsmål {i+1}: {question['question']}\n{'-'*40}\n")
        options = [question['option1'], question['option2'], question['option3'], question['option4']]
        random.shuffle(options)
        
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        
        try:
            correct_answer = question['option1']
            correct_reason = question['reason1']
        except KeyError:
            print("Error: The question does not have an 'answer' key.")
            continue
        
        while True:
            answer = (input("\nDitt svar (1-4): ").strip())
            try:
                answer = int(answer)
                if options[int(answer) - 1].strip().lower() == correct_answer.strip().lower():
                    print(f"\nRiktig! {correct_reason}\n")
                    score += 1
                else:
                    print(f"\nDette er feil, det rette svaret var: {correct_answer}\n{correct_reason}\n")
                break

            except (ValueError, IndexError): 
                if answer == "slutt":
                    print("Quiz avsluttet.")
                    break
                print("Vennligst skriv inn et tall (1-4).")
                continue

    print(f"\n{'='*40}\nQuiz ferdig! Din poengsum: {score}/{n}\n{'='*40}")

if __name__ == "__main__":
    filename = 'generated_questions.csv'
    questions = load_questions(filename)
    print("\n\n\nVelkommen til Exphil Quiz basert på boken 'Tenk'!\n")
    print(f"Antall tilgjengelige spørsmål: {len(questions)}")
    print("Du vil få spørsmål med fire svaralternativer, hvor kun ett er riktig.")
    print("Skriv inn tallet (1-4) som tilsvarer ditt svar.\n")
    print("Skriv slutt som  ditt svar om du vil avslutte quizen.\n")
    print("-" * 40)
    
    n = int(input("Hvor mange spørsmål vil du svare på? "))
    print("-" * 40)
    quiz_user(questions, n)