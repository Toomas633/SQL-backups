const settingsElement = document.getElementById("settings");

function openSettings() {
  settingsElement.style.display = "block";
}

function closeSettings() {
  settingsElement.style.display = "none";
}

const button = document.getElementById("passwordChangeBtn");
button.addEventListener("click", function (event) {
  event.preventDefault();
});

var form = document.getElementById("passwordForm");
form.addEventListener("keypress", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
  }
});

function changePassword() {
  const currentPassword = document.getElementById("currentPassword").value;
  const newPassword = document.getElementById("newPassword").value;
  const confirmPassword = document.getElementById("confirmPassword").value;

  if (newPassword !== confirmPassword) {
    openPopupJS("ERROR: New password and confirm password do not match.");
    return;
  }

  fetch("/change-password", {
    method: "POST",
    body: JSON.stringify({
      currentPassword: currentPassword,
      newPassword: newPassword,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        openPopupJS("Password changed successfully.");
        setTimeout(function() {
          window.location.href = '/logout';
        }, 3000);
      } else {
        openPopupJS(data.message);
      }
    })
    .catch((error) => {
      console.error(error);
      openPopupJS(data.message);
    });
}

function openPopupJS(message) {
  popupElement.style.display = "block";
  if (message.startsWith("ERROR")) {
    popupMessageElement.textContent = message.slice(7);
    popupElement.style.backgroundColor = "darkred";
  } else {
    popupMessageElement.textContent = message;
    popupElement.style.backgroundColor = "green";
  }
  setTimeout(closePopupJS, 3000);
}

function closePopupJS() {
  popupElement.style.display = "none";
}
