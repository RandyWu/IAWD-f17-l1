var gum = (function () {
    var shoppingCartPrice = 0.0;
    var shoppingCartItems = 0;
    var brands = {
        'extra' : 1.00,
        'trident': 1.50,
        'doublemint' : 2.00,
        'bubble gum' : 2.50
      };

    return {
      addPrice: function(gumBrand) {
        shoppingCartPrice += brands[gumBrand];
        shoppingCartItems ++;
        document.getElementById('cart').innerHTML = 'Shopping Cart Items: $' + shoppingCartPrice
        document.getElementById('total').innerHTML = 'Shopping Cart Total: ' + shoppingCartItems
      },

      clearPrice: function() {
        shoppingCartPrice = 0;
        shoppingCartItems = 0;
        document.getElementById('cart').innerHTML = 'Shopping Cart Items:'
        document.getElementById('total').innerHTML = 'Shopping Cart Total:'
      },
    };
})();

/*
 Used getElementsByTagName('td') because I wanted to practice navigating DOM
 Could've given each td a class or id
 */
var gumList = document.getElementById('gums').getElementsByTagName('td')
var clearButton = document.getElementById('clear')

// Brand = Extra
gumList[0].addEventListener('click', function () {
  gum.addPrice('extra')
  }
);

// Brand = Doublemint
gumList[1].addEventListener('click', function () {
  gum.addPrice('doublemint')
  }
);

// Brand = Trident
gumList[2].addEventListener('click', function () {
  gum.addPrice('trident')
  }
);

// Brand = Bubble Gum
gumList[3].addEventListener('click', function () {
  gum.addPrice('bubble gum')
  }
);

// Clear Price
clearButton.addEventListener('click', function () {
  gum.clearPrice();
  }
);
