function showPopup(message, type) {
    const container = document.getElementById("popupContainer");
    const popup = document.createElement("div");
    popup.className = `popup ${type}`;
    popup.textContent = message;

    container.appendChild(popup);

    setTimeout(() => {
      popup.remove();
    }, 3000);
  };