function openAddForm() {
  document.getElementById("addPopup").style.display = "block";
}

function closeAddForm() {
  document.getElementById("addPopup").style.display = "none";
}

const addButton = document.getElementById("addConnectionBtn");
addButton.addEventListener("click", function (event) {
  event.preventDefault();
});

const connectionForm = document.getElementById("addForm");
connectionForm.addEventListener("keypress", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
  }
});
