const print_age = (name) => console.log(name);
print_age("Noel");

const clic = document.getElementById("cambiarColor");
clic.addEventListener("click", () => {
	clic.style.background = "#ee00ee";
});

const title_button = document.getElementById("cambiarTexto");
const title = document.getElementById("titulojs");

title_button.addEventListener("click", () => {
	title.textContent = "Puro HACKZTECS bro";
});
