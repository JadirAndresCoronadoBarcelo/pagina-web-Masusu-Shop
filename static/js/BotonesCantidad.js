document.addEventListener('DOMContentLoaded', () => {
    const btnMenos = document.getElementById('btnMenos');
    const btnMas = document.getElementById('btnMas');
    const spanCantidad = document.getElementById('cantidad');
    const spanStock = document.getElementById('stock');
    
    // Opcional: si tienes un input oculto para enviar la cantidad en el formulario
    const inputCantidad = document.getElementById('inputCantidad');

    // Convertimos el texto del stock a un número entero
    const stockMaximo = parseInt(spanStock.textContent) || 0;

    // Si por alguna razón el stock es 0, iniciamos en 0 y bloqueamos
    if (stockMaximo === 0) {
        spanCantidad.textContent = 0;
        if (inputCantidad) inputCantidad.value = 0;
    }

    btnMas.addEventListener('click', () => {
        let cantidadActual = parseInt(spanCantidad.textContent);
        
        // Solo permitimos aumentar si la cantidad actual es menor al stock disponible
        if (cantidadActual < stockMaximo) {
            cantidadActual++;
            spanCantidad.textContent = cantidadActual;
            if (inputCantidad) inputCantidad.value = cantidadActual;
        }
    });

    btnMenos.addEventListener('click', () => {
        let cantidadActual = parseInt(spanCantidad.textContent);
        
        if (cantidadActual > 1) {
            cantidadActual--;
            spanCantidad.textContent = cantidadActual;
            if (inputCantidad) inputCantidad.value = cantidadActual;
        }
    });
});