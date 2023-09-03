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

function addConnection() {
  const name = document.getElementById("name").value;
  const type = document.getElementById("type").value;
  const address = document.getElementById("address").value;
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const elements = connectionForm.elements;
  let isFormValid = true;

  for (let i = 0; i < elements.length; i++) {
    if (elements[i].value === "" && elements[i].hasAttribute("required")) {
      isFormValid = false;
      break;
    }
  }

  if (isFormValid) {
    fetch("/add-connection", {
      method: "POST",
      body: JSON.stringify({
        name: name,
        type: type,
        address: address,
        username: username,
        password: password,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          openPopupJS("Connection added");
        } else {
          openPopupJS(data.message);
        }
      })
      .catch((error) => {
        console.error(error);
        openPopupJS(error);
      });
  } else {
    openPopupJS("ERROR: All fields must be filled");
  }
  
}
