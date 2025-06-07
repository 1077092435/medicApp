document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const dropdownMenu = document.getElementById('dropdownMenu');
    const menuOverlay = document.getElementById('menuOverlay');
    const cerrarMenu = document.getElementById('cerrarMenu');
    
    menuToggle.addEventListener('click', function() {
        dropdownMenu.classList.toggle('menu-visible');
        menuOverlay.classList.toggle('overlay-visible');
        this.classList.toggle('active');
    });
    
    menuOverlay.addEventListener('click', function() {
        dropdownMenu.classList.remove('menu-visible');
        this.classList.remove('overlay-visible');
        menuToggle.classList.remove('active');
    });

    cerrarMenu.addEventListener('click', function(){
        dropdownMenu.classList.remove('menu-visible');
        menuOverlay.classList.remove('overlay-visible');
        menuToggle.classList.remove('active');
    })
});