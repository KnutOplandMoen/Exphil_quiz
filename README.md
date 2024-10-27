# Exphil_quiz
## Folder Structure

The `Exphil_quiz` folder is organized as follows:

```
Exphil_quiz/
├── question_generation_folder/
│   ├── method1.py
│   └── ...
├── app.py
├── generated_question_folder/
│   ├── questions1.csv
│   ├── questions2.csv
│   └── ...
└── README.md
```

- **app.py**: The main application file that contains the logic for running the Exphil Quiz.
- **generated_question_folder/**: A folder containing CSV files with quiz questions. Each CSV file should have columns for the question, options, and reasons.
- **question_generation_folder/**: This folder contains scripts for generating quiz questions. Each script implements a different method for question generation.

## Running the Application

To run the Exphil Quiz application, execute the `app.py` file. This will start the quiz interface where you can select the number of questions and whether you want immediate feedback on your answers.

```bash
python app.py
```

## Required Libraries

The following libraries are required to run the application:

```python
import csv
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os
import sys
```

Make sure to install these libraries using pip:

```bash
pip install csv random tkinter os sys
```
