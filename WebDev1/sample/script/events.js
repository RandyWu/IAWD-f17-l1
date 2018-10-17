//Add Event Handlers

//When the user enters their name the input value is displayed as innerHTML
document.getElementById("firstName").addEventListener("change", function(){
    greeting.innerHTML = "Hello " + this.value;
});

//remove warning if firstName has input
document.getElementById("firstName").addEventListener("blur", function(){
    if(this.value !== ""){
        fnameWarning.innerHTML = "";
    }
});

//remove warning if course is selected
document.getElementById("courses").addEventListener("click", function(){
    if(profileForm.courses.options.selectedIndex !== -1){
        courseWarning.innerHTML = "";
    }
});

//remove warning if lastName has input
document.getElementById("lastName").addEventListener("blur", function(){
    if(this.value !== ""){
        lnameWarning.innerHTML = "";
    }
});

document.getElementById("status").addEventListener("click", function() {
    // access properties using this keyword
    if ( this.checked ) {
        // if checked ...
        alert("full-time is checked");
    } else {
        alert("full-time is unchecked");
    }
});

// Add an event to the form on submit to validate input
document.profileForm.addEventListener("submit", validate);


//add option to campus dropdown list
function addOption(){
        var other = new Option("Other", "other",false,false);
        var campus = profileForm.campus;
        campus.options[campus.options.length] = other;
}

//add onclick event to multiple elements
var radCountry = profileForm.country;

for(var i = 0; i < radCountry.length; i++){
    radCountry[i].onclick = function(){
        if(this.value !== "Canada"){
            addOption();
        }
    }
}
