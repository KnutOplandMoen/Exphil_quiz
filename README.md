# Exphil_quiz
## Mappestruktur

`Exphil_quiz` er organisert som følger:

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

- **app.py**: Hovedapplikasjonsfilen som inneholder logikken for å kjøre Exphil Quiz.
- **generated_question_folder/**: En mappe som inneholder CSV-filer med quizspørsmål. Hver CSV-fil skal ha kolonner for spørsmålet, alternativer og begrunnelser.
- **question_generation_folder/**: Denne mappen inneholder skript for å generere quizspørsmål. Hvert skript implementerer en annen metode for spørsmålsgenerering.

## Kjøre applikasjonen

For å kjøre Exphil Quiz-applikasjonen, kjør `app.py`-filen. Dette vil starte quizgrensesnittet hvor du kan velge antall spørsmål og om du vil ha umiddelbar tilbakemelding på svarene dine.

```bash
python app.py
```

## Nødvendige biblioteker

Følgende biblioteker er nødvendige for å kjøre applikasjonen:

```python
import csv
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os
import sys
```

Sørg for å installere disse bibliotekene ved hjelp av pip:

```bash
pip install csv random tkinter os sys
```
