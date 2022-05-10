function myFunction() {
  var x = document.getElementById("form");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function wallet_NotExist() {
  alert("Account ID does not exist");
}

function notEnoughMoney() {
  alert("You don't have enoguh money to transfer")
}