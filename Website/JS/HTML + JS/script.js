function validate(e) {
    e.preventDefault();


    const email = document.getElementById("mail").value;
    const pass = document.getElementById("password").value;
    const age = document.getElementById("age").value;
    const msgBox = document.getElementById("message");

    let message = "";
    if (email = "") {
        message = "Please enter an Email.";
        msgBox.style.color = "red";
    }
    else if (pass = "") {
        message = "Please enter an password.";
        msgBox.style.color = "red";
    }
    else if (age = "") {
        message = "Please enter your age.";
        msgBox.style.color = "red";
    }
    else {
        message = "Login Successful!";
        msgBox.style.color = "green";
    }
    msgBox.innerHTML = message;
}

//Run Validate when log in is clicked
document.getElementById("loginForm").onsubmit = validate;

//Run Real-time validation like the screenshots

document.getElementById("email").oninput = () => validate({ preventDefault: () => { } });

document.getElementById("password").oninput = () => validate({ preventDefault: () => { } });

document.getElementById("age").oninput = () => validate({ preventDefault: () => { } });

