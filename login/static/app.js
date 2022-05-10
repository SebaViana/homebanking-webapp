function myFunction() {
  var x = document.getElementById("form");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function viewPassword1() {
  var x = document.getElementById("password1");
  if (x.type === "password") {
    x.type = 'text';
  } else {
    x.type = 'password'
  }
}

function wallet_NotExist() {
  alert("Account ID does not exist");
}

function notEnoughMoney() {
  alert("You don't have enoguh money to transfer")
}

function trasnactionSuccessful() {
  alert("the transaction was successful")
}