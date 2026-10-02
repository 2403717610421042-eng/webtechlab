document.addEventListener("DOMContentLoaded", () => {
    let slides = document.querySelectorAll(".slide");
    if(slides.length > 0) {
        let current = 0;
        slides[current].classList.add("active");
        setInterval(() => {
            slides[current].classList.remove("active");
            current = (current + 1) % slides.length;
            slides[current].classList.add("active");
        }, 3000);
    }
});
