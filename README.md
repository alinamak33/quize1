🧠 Python Quiz Challenge
This is a simple, modern, and interactive web quiz application built with Flask and pure HTML/CSS/JavaScript. It challenges users on fundamental Python programming concepts.

✨ Features
Python Fundamentals: A bank of multiple-choice questions covering topics like variables, data types, operators, lists, dictionaries, and functions.

Interactive UI: A single-page application experience managed by JavaScript.

Score Tracking: Tracks the user's progress and displays the final score.

Stylish Design: Uses a dark, modern interface with a "glow" effect for an engaging look.

⚙️ Project Structure
quize/
├── app.py                      # Flask application logic and quiz data
├── requirements.txt            # Python dependencies
├── static/
│   ├── script.js               # Frontend quiz logic (fetching data, game flow)
│   └── style.css               # Styling for the quiz interface
└── templates/
    └── index.html              # Main HTML structure (Login, Quiz, Result pages)
🛠️ Setup and Installation
Prerequisites
Python 3.x

pip (Python package installer)

Steps
Navigate to the project directory:

Bash

cd quize
Install Dependencies: The application requires only Flask.

Bash

pip install -r requirements.txt
Run the Application: Start the Flask server:

Bash

python app.py
Access the Quiz: Open your web browser and go to the address displayed in your terminal, usually: http://127.0.0.1:5000/

🎮 How to Play
Login: Upon opening the app, enter your name in the Login Page and click Start Quiz.

Answer Questions: The quiz will present multiple-choice questions one by one. Click on the option button that you believe is the correct answer.

Progression: The quiz automatically moves to the next question after an answer is selected. Your score is updated in the background.

Results: Once all questions are answered, the Result Page will appear, showing your name and final score.

Restart: Click Play Again to restart the quiz from the beginning.

💻 Technical Details
Backend (app.py): Stores the quiz questions and answers as a Python list of dictionaries. The /get-quiz route serves this data as JSON to the frontend.

Frontend (script.js): Fetches the quiz data, manages the three main views (Login, Quiz, Result), handles button clicks, tracks the currentQuestion index, and calculates the score.

Styling (style.css): Provides a dark, modern aesthetic using CSS variables, a gradient background, and animated effects.
