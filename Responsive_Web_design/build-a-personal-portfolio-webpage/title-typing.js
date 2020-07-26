/* Reference to source code by Gregory Schier (https://codepen.io/gschier/pen/jkivt?editors=1010) */


/* Algorithmic definition of the text animation as a functional 'class' */
var TxtRotate = function(element, toRotate, period) {

    this.toRotate = toRotate;
    this.el = element;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.txt = '';
    this.effect();
    this.isDeleting = false;
};

/* Definition of tick() function */
TxtRotate.prototype.effect = function(){

    var i = this.loopNum % this.toRotate.length;
    var fullTxt = this.toRotate[i];

    if(this.isDeleting)
        this.txt = fullTxt.substring(0, this.txt.length - 1); // Remove chars while deleting
    else
        this.txt = fullTxt.substring(0, this.txt.length + 1); // Insert chars while not deleting

    // Replace the displayed string with modified (txt)
    this.el.innerHTML = '<span class="wrap">'+ this.txt +'</span>';

    var that = this;
    var delta = 250 - Math.random() * 100;

    // Animation duration halved while it is deleting chars when there are more left
    if(this.isDeleting) { delta /= 2; }

    if(!this.isDeleting && this.txt === fullTxt){
        delta = this.period;
        this.isDeleting = true;

    } else if(this.isDeleting && this.txt === ''){
        this.isDeleting = false;
        this.loopNum++;
        delta = 500;
    }

    setTimeout(function(){that.effect();}, delta);
};

/* Function executed when the webpage loaded */
window.onload = function(){

    // Find the target element
    var elements = this.document.getElementsByClassName('title-typing');

    for(var i=0; i<elements.length; i++) {
        var toRotate = elements[i].getAttribute('data-rotate');
        var period = elements[i].getAttribute('data-period');

        // Create and execute the TxtRotate object iff there is string options given 
        // from referenced innerHTML element(s)
        if(toRotate) { new TxtRotate(elements[i], JSON.parse(toRotate), period); }
    }

    // Define .wrap class as an external stylesheet
    var css = document.createElement("style");
    css.type = "text/css";

    // The input starting line in the animation
    css.innerHTML = ".title-typing > .wrap { border-right: 0.1em solid #666; } "; 
    this.document.body.appendChild(css);
};