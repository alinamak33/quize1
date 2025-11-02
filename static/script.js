let quizData = [];
let currentQuestion = 0;
let score = 0;
let userName = "";

const loginBox = document.getElementById("login-box");
const quizBox = document.getElementById("quiz-box");
const resultBox = document.getElementById("result-box");
const questionEl = document.getElementById("question");
const optionsEl = document.getElementById("options");
const nextBtn = document.getElementById("next-btn");
const scoreEl = document.getElementById("score");
const playerNameEl = document.getElementById("player-name");

fetch("/get-quiz")
  .then(res => res.json())
  .then(data => {
    quizData = data;
  });

function startQuiz() {
  const input = document.getElementById("username").value.trim();
  if (input === "") {
    alert("Please enter your name!");
    return;
  }
  userName = input;
  loginBox.classList.add("hidden");
  quizBox.classList.remove("hidden");
  loadQuestion();
}

function loadQuestion() {
  const q = quizData[currentQuestion];
  questionEl.textContent = q.question;
  optionsEl.innerHTML = "";

  q.options.forEach(option => {
    const btn = document.createElement("button");
    btn.classList.add("option");
    btn.textContent = option;
    btn.onclick = () => selectAnswer(option);
    optionsEl.appendChild(btn);
  });
}

function selectAnswer(selected) {
  const correct = quizData[currentQuestion].answer;
  if (selected === correct) {
    score++;
  }

  currentQuestion++;
  if (currentQuestion < quizData.length) {
    loadQuestion();
  } else {
    showResult();
  }
}

function showResult() {
  quizBox.classList.add("hidden");
  resultBox.classList.remove("hidden");
  playerNameEl.textContent = `🎉 Well done, ${userName}!`;
  scoreEl.textContent = `Your Score: ${score} / ${quizData.length}`;
}

function restartQuiz() {
  currentQuestion = 0;
  score = 0;
  resultBox.classList.add("hidden");
  loginBox.classList.remove("hidden");
}
