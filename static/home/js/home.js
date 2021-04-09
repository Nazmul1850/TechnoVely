$(document).ready(function() { 
    console.log('Reached');
	$('#all-services').owlCarousel({
    loop:($("#all-services .item").length > 1) ? true: false,
    center:true,
    nav:true,
    navText:["<div class='nav-btn prev-slide'></div>","<div class='nav-btn next-slide'></div>"],
    items:1,
    margin:10,
    autoplay:true,
    dots:true,
    autoplayTimeout:8500,
    smartSpeed:450,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
        },
        768:{
            items:3,
        },
        1170:{
            items:3,
        }
    }
});

});