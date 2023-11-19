document.addEventListener('DOMContentLoaded', function() {
    if ('scrollbarColor' in document.documentElement.style) {
        document.documentElement.style.scrollbarColor = 'black black';
    } else {
        console.log('O navegador não suporta a personalização da barra de rolagem.');
    }
});



