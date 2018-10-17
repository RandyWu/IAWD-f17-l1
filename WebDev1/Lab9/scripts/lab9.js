$(document).ready(function( ) {

    //2. Changing h1
    $("h1").text("Randy Wu");

    //3. Selecting id=header
    $("#header").html("<h3>Working with jQuery</h3>");

    //4). Selecting attribute=button
    $("input[type = 'button']").each(function() {
      $(this).addClass("btn-background")
    });

    //5. Selecting id=buttons
    $("#buttons").addClass("red-border");

    //6). Select all p elements
    $("p").each(function() {
      $(this).addClass("blue");
    });

    //7. Selecting id=first
    $("#first").on("click", function() {
      $("p").first().addClass("green-border");
    });

    //8. Selecting id=last
    $("#last").on("click", function() {
      $('p').last().addClass("orange-border");
    })

    //9. Selecting id=prev
    $("#prev").on("click", function() {
      $("#para3").prev().addClass("purple-border");
    })

    //10. Selecting id=next
    $("#next").on("click", function() {
      $("#para2").next().addClass("yellow-border");
    })

    //11. Selecting id=remove
    $("#remove").on("click", function() {
      $("#footer").remove();
    })
});
