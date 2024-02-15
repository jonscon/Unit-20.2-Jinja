/* Form Validation*/

let questionFields = document.getElementsByClassName("question-field");
let questionForm = document.getElementById("questions-form");

questionForm.addEventListener("submit", function(e) {
    for (let i = 0; i < questionFields.length; i++) {
        // Check if the fields are empty
        if (questionFields[i].value === "") {
            alert("FILL IN THE FIELDS DUMMY");
            e.preventDefault();
            break;
        }
        // Check if the answers are at least three characters
        if (questionFields[i].value.length < 3) {
            alert("Please make sure all your answers are at least 3 characters long!");
            e.preventDefault();
            break;
        }
    }

})