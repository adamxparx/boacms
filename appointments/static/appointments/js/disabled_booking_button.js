const form = document.getElementById('appointment-form');
const submitButton = document.getElementById('submit-button');

form.addEventListener('submit', function() {
    submitButton.disabled = true;
    submitButton.style.opacity = 0.5;
    submitButton.textContent = "Booking Appointment...";
});