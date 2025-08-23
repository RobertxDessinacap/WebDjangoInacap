
document.getElementById("botonJextra").addEventListener("click", function() {
    const extraInfo = document.getElementById("extra");
    extraInfo.classList.toggle("info-visible");
    extraInfo.classList.toggle("info-oculta");
});

mostrarFormBtn.addEventListener('click', function() {      // Animación de despliegue del formulario
    if (formulario.classList.contains('formulario-visible')) {
        // Cierra el formulario con animación
        formulario.classList.remove('formulario-visible');
        setTimeout(() => {
            formulario.style.display = 'none';
        }, 500);
    } else {
        // Abre el formulario con animación
        formulario.style.display = 'block';
        setTimeout(() => {
            formulario.classList.add('formulario-visible');
        }, 10);
    }
});