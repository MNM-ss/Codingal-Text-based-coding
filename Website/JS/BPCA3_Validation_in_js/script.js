/* =============================================
   PRE-WRITTEN HELPERS — Do not change
   ============================================= */

var currentOTP    = null;
var timerInterval = null;
var attempts      = 0;
var otpExpired    = false;

function el(id) {
  return document.getElementById(id);
}

function showScreen(id) {
  ["screen-phone", "screen-otp", "screen-success"].forEach(function(s) {
    el(s).style.display = "none";
  });
  el(id).style.display = "block";
}

function setMsg(text, type) {
  el("msg").textContent = text;
  el("msg").className   = "msg " + (type || "");
}

function tryAgain() {
  attempts = 0;
  otpExpired = false;
  if (timerInterval) clearInterval(timerInterval);
  el("otp-input").value           = "";
  el("otp-input").className       = "otp-input";
  el("phone-msg").textContent     = "";
  el("phone-wrap").className      = "phone-input-wrap";
  el("attempts-left").textContent = "";
  setMsg("", "");
  showScreen("screen-phone");
}

function sendOTP() {
  var phone = el("phone-input").value.trim();
  if (!phone || phone.length !== 10 || isNaN(Number(phone))) {
    el("phone-msg").textContent = "⚠ Enter a valid 10-digit mobile number.";
    el("phone-wrap").className  = "phone-input-wrap is-error";
    return;
  }
  el("phone-msg").textContent   = "";
  el("phone-wrap").className    = "phone-input-wrap";
  el("sent-to").textContent     = phone;
  currentOTP                    = String(Math.floor(100000 + Math.random() * 900000));
  el("otp-display").textContent = currentOTP;
  showScreen("screen-otp");
  startTimer();
}

function startTimer() {
  if (timerInterval) clearInterval(timerInterval);
  otpExpired                      = false;
  attempts                        = 0;
  el("attempts-left").textContent = "";
  el("otp-input").value           = "";
  el("otp-input").className       = "otp-input";
  setMsg("", "");
  var count                       = 30;
  el("timer").textContent         = count;
  el("timer-text").style.display  = "inline";
  el("resend-btn").style.display  = "none";
  el("resend-btn").disabled       = true;
  timerInterval = setInterval(function() {
    el("timer").textContent = --count;
    if (count <= 0) {
      clearInterval(timerInterval);
      otpExpired                     = true;
      el("timer-text").style.display = "none";
      el("resend-btn").style.display = "inline";
      el("resend-btn").disabled      = false;
    }
  }, 1000);
}


/* =============================================
   YOUR TASK — Write your code below
   ============================================= */

function verifyOTP() {

  // Step 1: Declare var entered — read "otp-input" value using el(), trim spaces

  // Step 2: Open a try block

    // Step 3: if !entered — throw "Please enter the OTP"

    // Step 4: if otpExpired — throw "OTP has expired. Please click Resend OTP."

    // Step 5: if entered.length !== 6 or isNaN(Number(entered)) — throw "OTP must be exactly 6 digits"

    // Step 6: if entered !== currentOTP — increment attempts, update "attempts-left" text, throw "Incorrect OTP" message

    // Step 7: Set "otp-input" className to "otp-input is-ok"

    // Step 8: setTimeout 400ms — call showScreen("screen-success")

  // Step 9: catch(e) — call setMsg(e, "error"), set "otp-input" className to "otp-input is-error"

  // Step 10: if attempts >= 3 — call tryAgain(), call setMsg with "Too many wrong attempts. Please try again."

}