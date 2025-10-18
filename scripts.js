function alternarLista(albumId) {
    // Esto busca el elemento por el ID: 'folklore_lista'
    var lista = document.getElementById(albumId + '_lista'); 
    
    // Es buena práctica verificar si el elemento existe antes de manipularlo
    if (lista) { 
        // Alternamos la clase: si está, la quita (MUESTRA); si no está, la pone (OCULTA).
        if (lista.classList.contains('oculto')) {
            lista.classList.remove('oculto');
        } else {
            lista.classList.add('oculto');
        }
    }
}