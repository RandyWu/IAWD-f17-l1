//form element events

//remove warning if fname is valid
document.getElementById('fname').addEventListener('blur', function() {
  if(this.value !== '') {
    fnameError.innerHTML = '';
  }
});

//remove warning if lname is valid
document.getElementById('lname').addEventListener('blur', function() {
  if(this.value !== '') {
    lnameError.innerHTML = '';
  }
});

//remove warning if address1 is valid
document.getElementById('address1').addEventListener('blur', function() {
  if(this.value !== '') {
    address1Error.innerHTML = '';
  }
});

//remove warning if city is valid
document.getElementById('city').addEventListener('blur', function() {
  if(this.value !== '') {
    cityError.innerHTML = '';
  }
});

//remove warning if province is valid
document.getElementById('province').addEventListener('blur', function() {
  if(profile.province.options.selectedIndex !== 0) {
    provinceError.innerHTML = '';
  }
});

//remove warning if country is valid
document.getElementById('country').addEventListener('blur', function() {
  if(profile.country.options.selectedIndex !== 0) {
    countryError.innerHTML = '';
  }
});


//validate form on submit
document.profile.addEventListener('submit', validate.validateProfile)
