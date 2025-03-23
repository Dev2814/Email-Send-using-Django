// Wait for the DOM to fully load before running the script
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("signupForm");

    // Listen for form submission
    form.addEventListener("submit", function (e) {
        // Get and trim values from all input fields
        const firstname = document.getElementById("firstname").value.trim();
        const lastname = document.getElementById("lastname").value.trim();
        const username = document.getElementById("username").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();
        const confirmPassword = document.getElementById("confirm_password").value.trim();

        // Check if any field is empty
        if (!firstname || !lastname || !username || !email || !password || !confirmPassword) {
            e.preventDefault(); // Prevent form submission
            showPopup("All fields are required!", "error");
            return;
        }

        // Check if passwords match
        if (password !== confirmPassword) {
            e.preventDefault();
            showPopup("Passwords do not match!", "error");
            return;
        }

        // Check password length
        if (password.length < 6) {
            e.preventDefault();
            showPopup("Password must be at least 6 characters!", "error");
            return;
        }
    });

    // Function to display popup messages
    function showPopup(message, type) {
        const container = document.getElementById("popupContainer");

        // Create a new popup div
        const popup = document.createElement("div");
        popup.className = `popup ${type}`; // Set class based on message type
        popup.textContent = message;

        // Add popup to the container
        container.appendChild(popup);

        // Automatically remove popup after 3 seconds
        setTimeout(() => {
            popup.remove();
        }, 3000);
    }
});
