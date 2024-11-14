/* welcome.html */

// Function to animate word display
function animateWord(word) {
    const container = document.getElementById("container");
    word.split("").forEach((char, index) => { 
        const letter = document.createElement("span");
        letter.textContent = char === " " ? "\u00A0" : char;
        letter.classList.add("letter");
        container.appendChild(letter);
        
        // Delay the appearance of each letter
        setTimeout(() => {
            letter.style.opacity = 1;
            letter.style.transform = "translateY(0)";
        }, index * 100);  // Adjust timing for each letter
    });
}

// Initialization for welcome page animation
document.addEventListener("DOMContentLoaded", function() {
    const word = "PROBABLY FUN!";
    animateWord(word);

    // Redirect after 3 seconds
    setTimeout(function() {
        window.location.href = "/signup";  // Update the URL as needed
    }, 3000);
});

/* landing */
function toggleUploadButtons() {
    document.getElementById("uploadButton").classList.remove("hidden");
    document.getElementById("backButton").classList.remove("hidden");
}

function handleUpload() {
    const files = document.getElementById("imageInput").files;
    const formData = new FormData();
    for (let file of files) {
        formData.append("images", file);
    }

    fetch("/upload_images", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("successMessage").classList.remove("hidden");
        document.getElementById("generateButton").classList.remove("hidden");
        document.getElementById("uploadButton").classList.add("hidden");
    });
}

function handleBack() {
    fetch("/clear_images", { method: "POST" })
    .then(response => response.json())
    .then(data => {
        document.getElementById("imageInput").value = "";
        document.getElementById("successMessage").classList.add("hidden");
        document.getElementById("generateButton").classList.add("hidden");
        document.getElementById("uploadButton").classList.add("hidden");
    });
}

function showTimerOptions() {
    document.getElementById("timerPopup").classList.remove("hidden");
}

function startTimer(seconds) {
    alert(`Timer started for ${seconds} seconds.`);
    document.getElementById("timerPopup").classList.add("hidden");
}

/* random*/
