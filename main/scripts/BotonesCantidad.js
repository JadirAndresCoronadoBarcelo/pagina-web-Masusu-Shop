document.addEventListener('DOMContentLoaded', () => {
    const btnMenos = document.getElementById('btnMenos');
    const btnMas = document.getElementById('btnMas');
    const spanCantidad = document.getElementById('cantidad');

    btnMas.addEventListener('click', () => {
        let cantidadActual = parseInt(spanCantidad.textContent);
        spanCantidad.textContent = cantidadActual + 1;
    });

    btnMenos.addEventListener('click', () => {
        let cantidadActual = parseInt(spanCantidad.textContent);
        
        if (cantidadActual > 1) {
            spanCantidad.textContent = cantidadActual - 1;
        }
    });
});