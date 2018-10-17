//validate module
var validate = (function(){


  var fnameError = document.getElementById('fnameError')
  var lnameError = document.getElementById('lnameError')
  var address1Error = document.getElementById('address1Error')
  var cityError = document.getElementById('cityError')
  var provinceError = document.getElementById('provinceError')
  var countryError = document.getElementById('countryError')

    return {
      validateProfile: function (e) {
        e.preventDefault();
        var checkValid = true;

        //display warning if fname is empty
        if (profile.fname.value === '') {
          fnameError.innerHTML = '--Please enter a First Name--';
          checkValid = false;
        };

        //display warning if lname is empty
        if (profile.lname.value === '') {
          lnameError.innerHTML = '--Please enter a Last Name--';
          checkValid = false;
        };

        //display warning if address1 is empty
        if (profile.address1.value === '') {
          address1Error.innerHTML = '--Please enter a Address--';
          checkValid = false;
        };

        //display warning if city is empty
        if (profile.city.value === '') {
          cityError.innerHTML = '--Please enter a City--';
          checkValid = false;
        };

        //display warning if province is not selected
        if (profile.province.options.selectedIndex === 0) {
          provinceError.innerHTML = '--Please select a valid Province--';
          checkValid = false;
        };

        //display warning if country is not selected
        if (profile.country.options.selectedIndex === 0) {
          countryError.innerHTML = '--Please select a valid Country--';
          checkValid = false;
        };

        //check if form is valid
        if(checkValid) {
          alert("Thank you for filling out the form")
        };

        return checkValid;
      }
    }

}());
