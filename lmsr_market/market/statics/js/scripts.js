// scripts.js

// Function to display an alert when the button is clicked
function showAlert() {
    alert("Button clicked!");
}

// Attach the showAlert function to the button with id 'myButton'
document.addEventListener('DOMContentLoaded', (event) => {
    const myButton = document.getElementById('myButton');
    if (myButton) {
        myButton.addEventListener('click', showAlert);
    }
});