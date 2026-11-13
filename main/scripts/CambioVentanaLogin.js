const tabs = document.querySelectorAll('.tab-btn');
const forms = document.querySelectorAll('.auth-form');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        // Quitar clase active de todos
        tabs.forEach(t => t.classList.remove('active'));
        forms.forEach(f => f.classList.remove('active'));

        // Añadir clase active al seleccionado
        tab.classList.add('active');
        document.getElementById(tab.dataset.target).classList.add('active');
    });
});