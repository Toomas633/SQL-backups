const settingsElement = document.getElementById("settings");
function openSettings() {
  settingsElement.style.display = "block";
  getSettings();
}
function closeSettings() {
  settingsElement.style.display = "none";
}

const passwordButton = document.getElementById("passwordChangeBtn");
passwordButton.addEventListener("click", function (event) {
  event.preventDefault();
});

const settingsButton = document.getElementById("saveSettingsBtn");
settingsButton.addEventListener("click", function (event) {
  event.preventDefault();
});

const passwordForm = document.getElementById("passwordForm");
passwordForm.addEventListener("keypress", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
  }
});

const settingsForm = document.getElementById("settingsForm");
settingsForm.addEventListener("keypress", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
  }
});

function changePassword() {
  const currentPassword = document.getElementById("currentPassword").value;
  const newPassword = document.getElementById("newPassword").value;
  const confirmPassword = document.getElementById("confirmPassword").value;

  if (newPassword !== confirmPassword) {
    openPopupJS("ERROR: New password and confirm password do not match");
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
        openPopupJS("Password changed successfully");
        setTimeout(function () {
          window.location.href = "/logout";
        }, 3000);
      } else {
        openPopupJS(data.message);
      }
    })
    .catch((error) => {
      console.error(error);
      openPopupJS(error);
    });
}

function getSettings() {
  const dumps = document.getElementById("dumps");
  const cron = document.getElementById("cron");

  fetch("/get-settings", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        dumps.value = data.dumps;
        cron.value = data.cron;
      } else {
        openPopupJS(data.message);
      }
    })
    .catch((error) => {
      console.error(error);
      openPopupJS(error);
    });
}

function saveSettings() {
  const dumps = document.getElementById("dumps").value;
  const cron = document.getElementById("cron").value;

  fetch("/change-settings", {
    method: "POST",
    body: JSON.stringify({
      dumps: dumps,
      cron: cron,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        openPopupJS("Settings changed successfully");
      } else {
        openPopupJS(data.message);
      }
    })
    .catch((error) => {
      console.error(error);
      openPopupJS(error);
    });
}
