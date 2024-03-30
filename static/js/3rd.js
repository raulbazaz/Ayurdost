document.addEventListener('DOMContentLoaded', function() {
    // Get the "Submit" button element
    const submitButton = document.getElementById('submitButton');

    // Add event listener for button click
    submitButton.addEventListener('click', function(event) {
        // Get the input value
        const symptomsInput = document.getElementById('symptoms').value;

        // Store the input value in session storage
        sessionStorage.setItem('symptomsInput', symptomsInput);
    });

    // Get the "Next" button element
    const nextButton = document.getElementById('nextButton');

    // Add event listener for button click
    nextButton.addEventListener('click', function(event) {
        // Redirect to the next page
        window.location.href = '../templates/4th.html';
    });
});
document.getElementById('nextButton').addEventListener('click', function(event) {
    // Get the stored symptoms from session storage
    const symptomsInput = sessionStorage.getItem('symptomsInput');

    // Send the symptoms to the server using fetch API
    fetch('/treatment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `symptoms=${encodeURIComponent(symptomsInput)}`
    })
    .then(response => response.text())
    .then(data => {
        // Redirect to the treatment page
        window.location.href = '/treatment';
    })
    .catch(error => console.error('Error:', error));
});
