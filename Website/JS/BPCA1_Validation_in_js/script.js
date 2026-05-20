/* =============================================
   PRE-WRITTEN HELPER — Do not change
   ============================================= */

function check(name, msgId, condition, errText, okText) {
  var input = document.forms["signupForm"][name];
  var field = input.closest(".field");
  var msg = document.getElementById(msgId);
  if (!condition) {
    field.className = "field error";
    msg.textContent = errText;
    return false;
  }
  field.className = "field valid";
  msg.textContent = okText;
  return true;
}


/* =============================================
   YOUR TASK — Write your code below
   ============================================= */

function validateForm() {





  // Step 1: Declare var name — read "fullname" from signupForm and trim spaces

  // Step 2: Declare var email — read "email" from signupForm and trim spaces

  // Step 3: Declare var pwd — read "password" from signupForm

  // Step 4: Declare var age — read "age" from signupForm

  // Step 5: Declare var v1 — call check() for "fullname", "msg-name", condition: name !== ""

  // Step 6: Declare var v2 — call check() for "email", "msg-email", condition: email !== "" && email.includes("@")

  // Step 7: Declare var v3 — call check() for "password", "msg-pwd", condition: pwd.length >= 8

  // Step 8: Declare var v4 — call check() for "age", "msg-age", condition: age !== "" && Number(age) >= 13

  // Step 9: if v1 && v2 && v3 && v4 — get "success" element, set display to "block", set innerHTML to the welcome message

  var name = document.forms["signup Form"]["fullname"].value.trim();
  var email = document.forms["signupForm"]["email"].value.trim();
  var pwd = document.forms["signup Form"]["password"].value;
  var age = document.forms["signupForm"]["age"].value;

  var v1 = check("fullname", "msg-name", name !== "", "Full name is required.",
    "✓ Looks good!");

  var v2 = check("email", "msg-email", email !== "" && email.includes("@"), email == "" ? "A Email is required." : "Must include @.",
    "✓Valid email address.");

  var v3 = check("password", "msg-pwd", pwd.length >= 8, pwd == "" ? "Password is required." : "Min 8 characters.", "✓ Strong password!");
  var v4 = check("age", "msg-age", age !== "" && Number(age) >= 13, age == "" ? "Age is required." : "Must be 13 or older.", "✓ Age verified.");



  if (v1 && v2 && v3 && v4) {
    var el = document.getElementById("success");
    el.style.display = "block";
    el.innerHTML = " <strong>Account created!</strong><br>Welcome to Instagram,< strong > " + name + "</strong >.Start sharing your moments.";
  }

  return false;
}