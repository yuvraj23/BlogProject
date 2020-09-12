jQuery(document).ready(function(){
"use strict"

$('.slider').ripples({
  dropRadius: 18,
  perturbance: 0.1,
});

$(".textdec").typed({
strings:["<strong class='sentence1'>Opportunity does not ", " <strong class='sentence1'>waste time with those🤔</strong>","<strong class='sentence1'> who are unprepared.", " <strong class='sentence2'>So Stop believing in luck,</strong >"
,"<strong class='sentence3'>And Start believing </strong>","<strong class='sentence2'>in preparation.😊</strong>"],
typespeed:0,
loop:true

});


$(".textdec2").typed({
strings:["<strong>Here You Can Find😊 </strong>",
"<strong>Content Related To</strong>",
"<strong>Placement Coding Problem</strong>",
"<strong>Interview Coding Questions</strong>",
"<strong>Aptitude Tips And Tricks</strong>",
"<strong>And Many More.</strong>"],
typespeed:0,
loop:true
});



$('.work').magnificPopup({
  delegate: 'a', // child items selector, by clicking on it popup will open
  type: 'image',
  gallery: {
     enabled: true
   }
});




var textWrapper1 = document.querySelector('.ml2');
textWrapper1.innerHTML = textWrapper1.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({loop: true})
  .add({
    targets: '.ml2 .letter',
    scale: [4,1],
    opacity: [0,1],
    translateZ: 0,
    easing: "easeOutExpo",
    duration: 950,
    delay: (el, i) => 70*i
  }).add({
    targets: '.ml2',
    opacity: 0,
    duration: 1000,
    easing: "easeOutExpo",
    delay: 1000
  });





    var textWrapper3 = document.querySelector('.ml5');
    textWrapper3.innerHTML = textWrapper3.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

    anime.timeline({loop: true})
      .add({
        targets: '.ml5 .letter',
        scale: [4,1],
        opacity: [0,1],
        translateZ: 0,
        easing: "easeOutExpo",
        duration: 950,
        delay: (el, i) => 70*i
      }).add({
        targets: '.ml5',
        opacity: 0,
        duration: 1000,
        easing: "easeOutExpo",
        delay: 1000
      });







var textWrapper = document.querySelector('.ml3');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({loop: true})
  .add({
    targets: '.ml3 .letter',
    opacity: [0,1],
    easing: "easeInOutQuad",
    duration: 2250,
    delay: (el, i) => 150 * (i+1)
  }).add({
    targets: '.ml3',
    opacity: 0,
    duration: 1000,
    easing: "easeOutExpo",
    delay: 1000
  });


$('.service-area').waypoint(function(direction){

$('.service-area').addClass('animated zoomIn')},{offset:'440px'});


});
