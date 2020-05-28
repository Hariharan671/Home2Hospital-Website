
$(document).ready(function(){
  var zindex = 10;
  
  $("div.card").click(function(e){
    e.preventDefault();

    var isShowing = false;

    if ($(this).hasClass("show")) {
      isShowing = true
    }

    if ($("div.cards").hasClass("showing")) {
      // a card is already in view
      $("div.card.show")
        .removeClass("show");

      if (isShowing) {
        // this card was showing - reset the grid
        $("div.cards")
          .removeClass("showing");
      } else {
        // this card isn't showing - get in with it
        $(this)
          .css({zIndex: zindex})
          .addClass("show");

      }

      zindex++;

    } else {
      // no cards in view
      $("div.cards")
        .addClass("showing");
      $(this)
        .css({zIndex:zindex})
        .addClass("show");

      zindex++;
    }
    
  });
});

$('#help ul li').on('click', function(){
    // clicking a questions reveals its answer
    //   if the answer is already visible, it's hidden
    if (false === $(this).children('ul').children('li').is(':visible')){
        $('#help ul li ul li').stop().slideUp('slow');
        $(this).children('ul').stop().children('li').slideDown('slow');
    } else {
        $(this).children('ul').stop().children('li').slideUp('slow'); 
    }
});


