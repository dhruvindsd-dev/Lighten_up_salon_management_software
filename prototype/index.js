let isTransparent = true;
const nav = document.querySelector('nav');

window.addEventListener('scroll', event => {
    if (window.pageYOffset > 70 && isTransparent) {
        nav.classList.add('_fixed');
        isTransparent = false;
    }

    if (window.pageYOffset <= 70 && !isTransparent) {
        nav.classList.remove('_fixed');
        isTransparent = true;
    }
});
