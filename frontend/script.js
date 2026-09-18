const input = document.getElementById("questionInput");
const askButton = document.getElementById("askButton");

const answerSection = document.getElementById("answerSection");
const answerText = document.getElementById("answerText");



async function askQuestion(question) {

    if (!question.trim()) {
        return;
    }

    answerSection.classList.remove("hidden");

    answerText.textContent = "Thinking...";

    answerSection.scrollIntoView({
        behavior: "smooth"
    });


    try {

        const response = await fetch("http://127.0.0.1:8000/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });


        if (!response.ok) {
            throw new Error("Server error");
        }


        const data = await response.json();

        answerText.textContent = data.answer;

    }

    catch (error) {

        console.error(error);

        answerText.textContent =
            "I couldn't connect to the Campus Guide backend. Make sure the Python server is running.";

    }
}



askButton.addEventListener("click", () => {

    askQuestion(input.value);

});



input.addEventListener("keydown", (event) => {

    if (event.key === "Enter") {

        askQuestion(input.value);

    }

});



const cards = document.querySelectorAll(".question-card");

cards.forEach(card => {

    card.addEventListener("click", () => {

        const question = card.dataset.question;

        input.value = question;

        askQuestion(question);

    });

});
