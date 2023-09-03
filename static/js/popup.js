const popupMessageElement = document.getElementById("popup-message");
const popupElement = document.getElementById("popup");

function openPopup() {
  popupElement.style.display = "block";
  setTimeout(closePopup, 3000);
}

function closePopup() {
  popupElement.style.display = "none";
}

function getParameterByName(name, url) {
  if (!url) {
    url = window.location.href;
  }
  name = name.replace(/[\[\]]/g, "\\$&");
  const regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
    results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return "";
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}

let messageFromURL = getParameterByName("message");

if (messageFromURL) {
  openPopup();
  if (messageFromURL.startsWith("ERROR")) {
    popupMessageElement.textContent = messageFromURL.slice(7);
    popupElement.style.backgroundColor = "darkred";
  } else {
    popupMessageElement.textContent = messageFromURL;
    popupElement.style.backgroundColor = "green";
  }
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