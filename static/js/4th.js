document.addEventListener('DOMContentLoaded', function() {
    // Get the container element to display symptoms
    const symptomsContainer = document.getElementById('symptomsContainer');

    // Retrieve the saved symptoms data from session storage
    const symptomsInput = sessionStorage.getItem('symptomsInput');

    // Check if symptoms data exists
    if (symptomsInput) {
        // Split the symptoms data by comma and create an array
        const symptomsArray = symptomsInput.split(',');

        // Create a list element to display symptoms
        const ul = document.createElement('ul');

        // Loop through the symptoms array and create list items
        symptomsArray.forEach(symptom => {
            const li = document.createElement('li');
            li.textContent = symptom;
            ul.appendChild(li);
        });

        // Append the list to the container
        symptomsContainer.appendChild(ul);
    } else {
        // If no symptoms data is found, display a message
        symptomsContainer.textContent = 'No symptoms data available.';
    }
});
