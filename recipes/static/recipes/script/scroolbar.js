document.addEventListener('DOMContentLoaded', function() {
    if ('scrollbarColor' in document.documentElement.style) {
        document.documentElement.style.scrollbarColor = 'black black';
    } else {
        console.log('seu navegador é uma merda.');
    }
});

