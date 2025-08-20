document.addEventListener("DOMContentLoaded", function () {
    var swiper = new Swiper(".category-swiper", {
        slidesPerView: 3,
        spaceBetween: 25,
        loop: true,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        breakpoints: {
            320: {slidesPerView: 1},
            640: {slidesPerView: 2},
            1024: {slidesPerView: 3}
        }
    });
});
