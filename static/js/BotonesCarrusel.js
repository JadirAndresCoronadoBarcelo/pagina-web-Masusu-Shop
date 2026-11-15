 const carruselPista = document.getElementById('caruselPista');
    const botonDer = document.getElementById('flechaDer');
    const botonIzq = document.getElementById('flechaIzq');
    
    let currentIndex = 0;
    const totalSlides = 3; // Tenemos 3 ofertas originales (sin contar la duplicada)

    // 1. Desactivamos la animación automática de CSS para dar el control total a los botones
    carruselPista.style.animation = 'none';
    carruselPista.style.transition = 'transform 0.6s ease-in-out';

    // Función para actualizar la posición visual del carrusel
    function moverCarrusel() {
        // Desplaza la pista usando unidades 'vw' (coincidiendo con el ancho de las imágenes)
        carruselPista.style.transform = `translateX(-${currentIndex * 100}vw)`;
    }

    // 2. Evento para la flecha derecha
    botonDer.addEventListener('click', () => {
        currentIndex++;
        if (currentIndex >= totalSlides) {
            currentIndex = 0; // Si llega al final, regresa circularmente a la primera
        }
        moverCarrusel();
    });

    // 3. Evento para la flecha izquierda
    botonIzq.addEventListener('click', () => {
        currentIndex--;
        if (currentIndex < 0) {
            currentIndex = totalSlides - 1; // Si está en la primera, salta a la última
        }
        moverCarrusel();
    });