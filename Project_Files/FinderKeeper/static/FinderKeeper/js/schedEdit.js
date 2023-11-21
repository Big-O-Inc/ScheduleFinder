document.addEventListener("DOMContentLoaded", function () {
  var addModal = document.getElementById("addModal");
  var addBtn = document.getElementById("addBtn");
  var delModal = document.getElementById("delModal");
  var delBtn = document.getElementById("delBtn");
  var editModal = document.getElementById("editModal");
  var editBtn = document.getElementById("editBtn");
  var cancelAddBtn = document.getElementById("cancelAddBtn");
  var cancelDelBtn = document.getElementById("cancelDelBtn");
  var cancelEditBtn = document.getElementById("cancelEditBtn");
  var spanAdd = document.getElementsByClassName("closeAdd")[0];
  var spanEdit = document.getElementsByClassName("closeEdit")[0];
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