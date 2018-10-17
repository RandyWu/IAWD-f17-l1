//lab6 JavaScript file
function addBooks(){
    var bookArray = new Array();
    var numberOfBooks = Number(prompt("How many books would you like to add? "))
    for (i = 0; i < numberOfBooks; i++) {
        var newAuthor = prompt('Who is the author of the recommended book? ');
        var newTitle = prompt('What is the title of the recommended book? ');
        var newGenre = prompt('What is the genre of the recommended book? ');

        book = {
            author: newAuthor,
            title: newTitle,
            genre: newGenre
        };
        bookArray.push(book);
    };
    return bookArray;
};

function displayRecommendations(bookArray) {
    for (i = 0; i < bookArray.length; i++) {
        var bookList = document.getElementById('bookList');
        var h3 = document.createElement('h3');
        var ul = document.createElement('ul');
        var listElement = document.createElement('li');
        var bookHeader = document.createTextNode(bookArray[i].title);

        listElement.appendChild(document.createTextNode(bookArray[i].title + ', Written By: ' + bookArray[i].author + ', Genre: ' + bookArray[i].genre))
        ul.appendChild(listElement)
        h3.appendChild(bookHeader)
        bookList.appendChild(h3)
        bookList.appendChild(ul)
    };
};

var recomendedBooks = addBooks();
displayRecommendations(recomendedBooks);
