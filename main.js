
//SLideshow 

var slideIndex = 0;
showSlides(slideIndex);

//Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}
//Image control
function currentSlide(n) {
    showSlides(slideIndex = n );
}

function showSlides(n) {
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    if( n > slides.length - 1 ) { slideIndex = 0}
    if ( n < 0 ) { slideIndex = slides.length }
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
     for (var i = 0; i < dots.length; i++) {
         dots[i].className = dots[i].className.replace("active", "");
     }
     slides[slideIndex].style.display = "block";
     //dots[slideIndex].className += "active";
 }

 //Filtering items

 filterCategories("All")
 function filterCategories(c) {
     var x;
     x = document.getElementsByClassName("column");
     if(c == "All") c = "";

     for(var i =0; i < x.length; i++) {
         removeClass(x[i], "show");
         if(x[i].className.indexOf(c) > -1) addclass(x[i], "show");
     }
 }

 function addclass(element, name) {
     var el, nam;
     el = element.className.split(" ");
     nam = name.split(" ");
     for(var i = 0; i < nam.length; i++) {
         if(el.indexOf(nam[i]) == -1) {
             element.className += " " + nam[i];
         }
     }
 }

 function removeClass(element, name) {
     var el, nam;
     el = element.className.split(" ");
     nam = name.split(" ");
     for(var i = 0; i < nam.length; i++) {
         while (el.indexOf(nam[i]) > -1) {
             el.splice(el.indexOf(nam[i]), 1)
         }
     }
     element.className = el.join(" ");
 }


 