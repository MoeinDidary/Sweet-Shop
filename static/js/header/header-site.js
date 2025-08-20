(function () {
    const toggle = document.getElementById('menuToggle');
    const menu = document.getElementById('mainMenu');
    if (toggle && menu) {
        toggle.addEventListener('click', () => {
            const open = menu.classList.toggle('open');
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
    }
    const onScroll = () => {
        const scrolled = window.scrollY > 12;
        document.documentElement.classList.toggle('scrolled', scrolled);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, {passive: true});
})();
