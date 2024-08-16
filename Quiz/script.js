function submitQuiz() {
    const form = document.getElementById('quiz-form');
    const formData = new FormData(form);
    let score = 0;
    let totalQuestions = 5;

    // Check answers
    if (formData.get('q1') == '3') score += 1; // Correct answer for question 1
    if (formData.get('q2') == '3') score += 1; // Correct answer for question 2
    if (formData.get('q3') == '1') score += 1; // Correct answer for question 3
    if (formData.get('q4') == '2') score += 1; // Correct answer for question 4
    if (formData.get('q5') == '3') score += 1; // Correct answer for question 5

    displayResults(score, totalQuestions);
}

function displayResults(score, totalQuestions) {
    const quizContainer = document.getElementById('quiz-container');
    const resultsContainer = document.getElementById('results-container');
    const scoreElement = document.getElementById('score');
    const messageElement = document.getElementById('message');

    quizContainer.style.display = 'none';
    resultsContainer.style.display = 'block';

    scoreElement.textContent = `You scored ${score} out of ${totalQuestions}.`;

    let message = '';
    if (score === totalQuestions) {
        message = 'Excellent! You got all the questions right.';
    } else if (score >= totalQuestions / 2) {
        message = 'Good job! You passed.';
    } else {
        message = 'Better luck next time.';
    }
    messageElement.textContent = message;
}

function restartQuiz() {
    const quizContainer = document.getElementById('quiz-container');
    const resultsContainer = document.getElementById('results-container');

    quizContainer.style.display = 'block';
    resultsContainer.style.display = 'none';

    // Reset the form
    document.getElementById('quiz-form').reset();
}
