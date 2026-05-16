// Select the element with the ID 'red_header'
const redHeaderTrigger = document.querySelector('#red_header');

// Select the <header> element whose color needs to change
const headerElement = document.querySelector('header');

// Check if both elements exist before adding the event listener
if (redHeaderTrigger && headerElement) {
    // Add a click event listener to the trigger element
    redHeaderTrigger.addEventListener('click', function () {
        // Update the header's text color to red (#FF0000)
        headerElement.style.color = '#FF0000';
    });
}
