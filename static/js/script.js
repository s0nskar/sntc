var causeRepaintsOn = $('.score-text');

$(window).resize(function () {
    causeRepaintsOn.css("z-index", 1);
});

$('.club_wrapper').hover(function(){
  // console.log(this.id+" h4")
  $("#"+this.id+" h4").animate({opacity:1},300)
},function(){
  // console.log(this.id)
  $("#"+this.id+" h4").animate({opacity:0.5},300)
})

// $( "#book" ).animate({
//     opacity: 0.25,
//     left: "+=50",
//     height: "toggle"
//   }, 5000, function() {
//     // Animation complete.
//   });