
document.addEventListener("DOMContentLoaded", () => {
    const calendarElement = document.getElementById("calendar");
    const API_URL = "/programaApi/feriados/2024/";
    async function recibirDatos(){

        try {

            var respuestaEventos = await fetch ('/api_eventos/');
            var listaEventos = await respuestaEventos.json();

            var respuestaFeriados = await fetch ('/consultar_feriados/');
            var listaFeriados = await respuestaFeriados.json();
            var unaWea =reque
            
        } catch (error) {

            console.log(error);
            
        }


    }
    



    // Código JavaScript
    const eventosData = JSON.parse(listaEventos);
    
    const feriadosData = JSON.parse(listaFeriados);
    
    function renderizarCalendario(anio, mes) {
        const contenedor = document.getElementById('calendario');
        contenedor.innerHTML = ''; // Limpiar calendario previo

        // Obtener días del mes
        const primerDia = new Date(anio, mes, 1);
        const ultimoDia = new Date(anio, mes + 1, 0);
        const totalDias = ultimoDia.getDate();

        // 
        const mapaFeriados = new Map(feriadosData.map(f => [f.nombre, f.descripcion, f.fecha_fin , f.fecha_fin]));
        const mapaEventos = new Map(eventosData.map(e => [e.nombre, e.descripcion, e.fecha_inicio, e.fecha_fin]));

        // Generar días del calendario
        for (let dia = 1; dia <= totalDias; dia++) {
            const fecha = new Date(anio, mes, dia);
            const fechaISO = fecha.toISOString().split('T')[0];

            // Crear día
            const elementoDia = document.createElement('div');
            elementoDia.classList.add('dia');

            if (mapaFeriados.has(fechaISO)) {
                elementoDia.classList.add('feriado');
                elementoDia.textContent = `${dia} - ${mapaFeriados.get(fechaISO)}`;
            } else if (mapaEventos.has(fechaISO)) {
                elementoDia.classList.add('suceso');
                elementoDia.textContent = `${dia} - ${mapaEventos.get(fechaISO)}`;
            } else {
                elementoDia.classList.add('libre');
                elementoDia.textContent = dia;
            }

            contenedor.appendChild(elementoDia);
        }
    }

    // Renderizar calendario del mes actual
    const hoy = new Date();
    renderizarCalendario(hoy.getFullYear(), hoy.getMonth());




    // Hacer la petición a la API
fetch('http://127.0.0.1:8000/programaApi/consultar-feriados/?year=2000')
.then(response => response.json())
.then(data => {
  // Integrar los datos al calendario
  let calendar = new FullCalendar.Calendar(document.getElementById('calendar'), {
    events: data, // Agregar directamente los eventos desde la API
    eventColor: '#FF5733', // Color predeterminado para los eventos
  });
  calendar.render();
})
.catch(error => {
  console.error('Error al cargar los feriados:', error);
});
});