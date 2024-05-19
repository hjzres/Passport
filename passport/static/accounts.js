let modal = document.getElementById("myModal");
let addAccountBtn = document.getElementById("add-account");
let span = document.getElementsByClassName("close")[0];

addAccountBtn.addEventListener('click', () => {
  modal.style.display = "block";
});

span.addEventListener('click', () => {
  modal.style.display = "none";
});

window.addEventListener('click', (event) => {
  if (event.target == modal) {
    modal.style.display = "none";
  }
});