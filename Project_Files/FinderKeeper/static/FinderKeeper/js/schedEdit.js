document.addEventListener("DOMContentLoaded", function () {
  var addModal = document.getElementById("addModal");
  var addBtn = document.getElementById("addBtn");
  var cancelAddBtn = document.getElementById("cancelAddBtn");
  var spanAdd = document.getElementsByClassName("closeAdd")[0];

  var editModal = document.getElementById("editModal");
  var editBtn = document.getElementById("editBtn");
  var cancelEditBtn = document.getElementById("cancelEditBtn");
  var spanEdit = document.getElementsByClassName("closeEdit")[0];

  var delModal = document.getElementById("delModal");
  var delBtn = document.getElementById("delBtn");
  var cancelDelBtn = document.getElementById("cancelDelBtn");
  var spanDel = document.getElementsByClassName("closeDel")[0];

  addBtn.onclick = function () {
    addModal.style.display = "block";
    document.body.classList.add('overflowHidden');
  }

  cancelAddBtn.onclick = function () {
    addModal.style.display = "none";
    document.body.classList.remove('overflowHidden');
  }

  spanAdd.onclick = function () {
    addModal.style.display = "none";
    document.body.classList.remove('overflowHidden');
  }

  editBtn.onclick = function () {
    editModal.style.display = "block";
    document.body.classList.add('overflowHidden');
  }

  cancelEditBtn.onclick = function () {
    editModal.style.display = "none";
    document.body.classList.remove('overflowHidden');
  }

  spanEdit.onclick = function () {
    editModal.style.display = "none";
    document.body.classList.remove('overflowHidden');
  }

  delBtn.onclick = function () {
    delModal.style.display = "block";
    document.body.classList.add('overflowHidden');
  }

  cancelDelBtn.onclick = function () {
    delModal.style.display = "none";
    document.body.classList.remove('overflowHidden');
  }

  spanDel.onclick = function () {
    delModal.style.display = "none";
    document.body.classList.remove('overflowHIdden');
  }

  window.onclick = function (event) {
    if (event.target == addModal) {
      addModal.style.display = "none";
      document.body.classList.remove('overflowHidden');
    }
    else if (event.target == editModal) {
      editModal.style.display = "none";
      document.body.classList.remove('overflowHidden');
    }
    else if (event.target == delModal) {
      delModal.style.display = "none";
      document.body.classList.remove('overflowHidden');
    }
  }
})

function loadForm() {
  const eventJson = JSON.parse(JSON.parse(document.getElementById("eventJson").textContent));

  var eventList = document.getElementById("editList");
  var eventSelected = eventList.options[eventList.selectedIndex];
  var eventId = eventSelected.getAttribute("value");

  for (i = 0; i < eventJson.length; i++) {
    if (eventJson[i]["id"] == eventId) {
      var currEvent = eventJson[i];
      break;
    } 
  }

  var titleBox = document.getElementById("editTitle");
  titleBox.value = currEvent["title"];

  var dayBoxes = document.getElementsByName("dayList");
  for (i = 0; i < dayBoxes.length; i++) { //Uncheck all day boxes
    dayBoxes[i].checked = false;
  }
  
  for (i = 0; i < currEvent["day"].length; i++) {
    switch (currEvent["day"][i]) {
      case "1":
        document.getElementById("monCheck").checked = true;
        break;
      case "2":
        document.getElementById("tueCheck").checked = true;
        break;
      case "3":
        document.getElementById("wedCheck").checked = true;
        break;
      case "4":
        document.getElementById("thuCheck").checked = true;
        break;
      case "5":
        document.getElementById("friCheck").checked = true;
        break;
    }
  }

  document.getElementById("editStart").value = currEvent["startTime"];
  document.getElementById("editEnd").value = currEvent["endTime"];
  document.getElementById("editLocation").value = currEvent["location"];
  document.getElementById("editDescription").value = currEvent["description"];
}