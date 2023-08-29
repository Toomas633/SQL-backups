function openPopup() {
  document.getElementById("popup").style.display = "block";
  setTimeout(closePopup, 3000);
}

function closePopup() {
  document.getElementById("popup").style.display = "none";
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
  document.getElementById("popup-message").textContent = messageFromURL;
  openPopup();
}
