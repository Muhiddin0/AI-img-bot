let title = document.querySelector('.title')
let moon = document.querySelector('.moon')
let mountain = document.querySelector('.mountain')
let road = document.querySelector('.road')
let bg_img = document.querySelector('.bg')
let message_0 = document.querySelector('.message_0')

window.addEventListener('scroll', function(){
    let value = scrollY;
    title.style.top = 55 - value * 0.2 +"%";
    message_0.style.bottom = 0 + value * 0.2 +"%";

    moon.style.top = 40 - value * 0.6+"%";
    moon.style.left = 10 + value * 0.8+"%";

    mountain.style.bottom = 0 - value * 0.1+"%";

    road.style.bottom = 0 - value * 0.1 + "%";
})