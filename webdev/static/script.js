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



/* landing*/

/// Function to toggle upload buttons when images are selected
function toggleUploadButtons() {
    document.getElementById("uploadButton").classList.remove("hidden");
    document.getElementById("backButton").classList.remove("hidden");
}

// Function to handle image upload
function handleUpload() {
    const files = document.getElementById("imageInput").files;
    const formData = new FormData();
    for (let file of files) {
        formData.append("images", file);
    }

    // POST the images to the server
    fetch("/upload_images", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // If upload is successful, show success message and generate button
        if (data.success) {
            document.getElementById("successMessage").classList.remove("hidden");
            document.getElementById("generateButton").classList.remove("hidden");
            document.getElementById("uploadButton").classList.add("hidden");
        }
    })
    .catch(error => console.error("Error during image upload:", error));
}


function clearUploadsAndRedirect(redirectUrl = null) {
    fetch("/clear_images", { method: "POST" })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                    // Reset UI elements
                const imageInput = document.getElementById("imageInput");
                if (imageInput) {
                    imageInput.value = ""; // Clear the file input
                }
    
                document.getElementById("successMessage")?.classList.add("hidden");
                document.getElementById("generateButton")?.classList.add("hidden");
                document.getElementById("uploadButton")?.classList.add("hidden");
                document.getElementById("backButton")?.classList.add("hidden");
    
                // Perform the redirection after successfully clearing images
                if (redirectUrl) {
                    window.location.href = redirectUrl;
                }
                
            } 
                else {
                    console.error("Failed to clear user uploads:", data.error);
                }
            })
            .catch(error => console.error("Error while clearing uploads:", error));
    }
    

document.addEventListener("DOMContentLoaded", function () {
    const navbarUploadButton = document.getElementById("navbarUpload");

    if (navbarUploadButton) {
        navbarUploadButton.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent default navigation
            clearUploadsAndRedirect("/landing"); // Clear uploads and redirect to landing page
        });
    }
});



function handleBack() {
    clearUploadsAndRedirect(); 
}


// Show timer options for random generation
function showTimerOptions() {
    document.getElementById("timerPopup").classList.remove("hidden");
}

// Start timer for image generation
function startTimer(seconds) {
    alert(`Timer started for ${seconds} seconds.`);
    document.getElementById("timerPopup").classList.add("hidden");

    window.location.href = `/random_generator?timer=${seconds}`;    
}

document.addEventListener("DOMContentLoaded", function () {
    const navbarUploadButton = document.getElementById("navbarUpload");

    if (navbarUploadButton) {
        navbarUploadButton.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent default navigation
            clearUploadsAndRedirect("/landing"); // Clear uploads and redirect to the landing page
        });
    }
});







