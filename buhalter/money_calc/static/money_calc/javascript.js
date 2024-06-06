let menuToggle = document.querySelector('#menu-toggle');
let menuList = document.querySelector('.menu-list');

menuToggle.addEventListener('change', function() {
    if (this.checked) {
        menuList.style.display = 'block';
    } else {
        menuList.style.display = 'none';
    }
});