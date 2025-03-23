// Wait for the entire DOM to load before running the script
document.addEventListener("DOMContentLoaded", function () {
    // Get the login form element
    const form = document.getElementById("loginForm");
  
    // Listen for the form submission event
    form.addEventListener("submit", function (e) {
      // Get the input values and trim any extra spaces
      const username = document.getElementById("username").value.trim();
      const password = document.getElementById("password").value.trim();
  
      // Basic client-side validation: check if either field is empty
      if (username === "" || password === "") {
        // Prevent the form from submitting to the server
        e.preventDefault();
        // Show error message as a popup
        showPopup("Username and Password are required!", "error");
      }
    });
  
    // Function to display a popup message on the screen
    function showPopup(message, type) {
      const container = document.getElementById("popupContainer");
  
      // Create the popup element and apply styling
      const popup = document.createElement("div");
      popup.className = `popup ${type}`;
      popup.textContent = message;
  
      // Append the popup to the popup container
      container.appendChild(popup);
  
      // Automatically remove the popup after 3 seconds
      setTimeout(() => {
        popup.remove();
      }, 3000);
    }
  });
  