/* =============================================
   PRE-WRITTEN HELPERS — Do not change
   ============================================= */

function selectShow(el) {
  document.querySelectorAll(".showtime").forEach(function(s) {
    s.classList.remove("selected");
  });
  el.classList.add("selected");
}

document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("tickets").addEventListener("input", function() {
    var t = this.value;
    document.getElementById("s-tickets").textContent = t ? t + " × ₹299" : "—";
    document.getElementById("s-total").textContent   = t ? "₹ " + (t * 299) : "—";
  });
  document.getElementById("seat").addEventListener("input", function() {
    document.getElementById("s-seat").textContent = this.value ? "Seat " + this.value : "—";
  });
});


/* =============================================
   YOUR TASK — Write your code below
   ============================================= */

function checkField(inputId, fieldId, msgId) {

  // Step 1: Declare var input — get element by inputId

  // Step 2: Declare var field — get element by fieldId

  // Step 3: Declare var msg — get element by msgId

  // Step 4: if !input.checkValidity() — set field.className to "field error", set msg.textContent to "❌ " + input.validationMessage, return false

  // Step 5: else — set field.className to "field valid", set msg.textContent to "✓ Valid", return true

}

function confirmBooking() {

  // Step 6: Declare var t1 — call checkField() for "tickets", "f-tickets", "m-tickets"

  // Step 7: Declare var t2 — call checkField() for "seat", "f-seat", "m-seat"

  // Step 8: Declare var t3 — call checkField() for "mobile", "f-mobile", "m-mobile"

  // Step 9: Declare var t4 — call checkField() for "email", "f-email", "m-email"

  // Step 10: if t1 && t2 && t3 && t4 — get "confirm" element, set display to "block", set innerHTML to the booking summary

}