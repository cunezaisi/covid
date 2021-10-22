const natoggle = document.querySelector(".toggle");
const menu = document.querySelector(".nav-menu");

natoggle.addEventListener("click", () => {
    menu.classList.toggle("navegar_active");
});