//validate the profile form
function validate(e){

    e.preventDefault();

    var valid=true;

    //display warning if firstName is not entered
    if(profileForm.firstName.value === ""){
    document.getElementById('fnameWarning').innerHTML="*Please enter a First Name*";
        valid = false;
    }

    //display warning if lastName is not entered
    if(profileForm.lastName.value == ""){
        document.getElementById('lnameWarning').innerHTML="*Please enter a Last Name*";
        valid=false;
    }

    //display warning if course is not selected
    if(profileForm.courses.options.selectedIndex === -1){
        valid = false;
        document.getElementById("courseWarning").innerHTML="*Select at least one course*";
    }

    if(valid){
        alert("Have a nice day!");
    }

    return valid;

};
