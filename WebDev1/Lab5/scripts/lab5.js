//Lab5 - Working with the Document Object Model

var mainTitle = document.getElementById('mainTitle')
var image = document.getElementById('image1')
var ul = document.getElementById('list')
var listElement1 = document.createElement('li')
var listElement2 = document.createElement('li')

var titleText = 'Learning about the Document Object Model ';
var imageTitle = 'JavaScript 1'
var listElement1Text = 'August 1996'
var listElement2Text = '1.8.2 June 22, 2009'
var editedElementText = '1.6 November 2005'

mainTitle.innerHTML = titleText;
mainTitle.style.textAlig = 'center';

image.title = imageTitle;
image.align = 'right'

listElement1.appendChild(document.createTextNode(listElement1Text))
ul.insertBefore(listElement1,ul.children[1])
listElement2.appendChild(document.createTextNode(listElement2Text))
ul.appendChild(listElement2)

ul.children[5].innerHTML = editedElementText

var totalLiTags = document.getElementsByTagName('li').length
document.write(totalLiTags)
