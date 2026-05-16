// Select the element with the ID 'red_header'
const redHeaderTrigger = document.querySelector('#red_header');

// Select the <header> element
const headerElement = document.querySelector('header');

// Check if both elements exist before performing actions
if (redHeaderTrigger && headerElement) {
    // Add a click event listener to the trigger element
    redHeaderTrigger.addEventListener('click', function () {
        // Add the 'red' class to the header element
        headerElement.classList.add('red');
    });
}
