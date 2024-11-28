document.addEventListener("DOMContentLoaded", async () => {
    const calendarElement = document.getElementById("calendar");

    
    const API_EVENTOS = '/api_eventos/';
    const API_FERIADOS = '/consultar_feriados/';

    
    async function obtenerEventosFeriados() {
        try {
            const [respuestaEventos, respuestaFeriados] = await Promise.all([
                fetch(API_EVENTOS),
                fetch(API_FERIADOS)
            ]);
    
            if (!respuestaEventos.ok || !respuestaFeriados.ok) {
                throw new Error('Error al cargar los datos.');
            }
    
            const listaEventos = await respuestaEventos.json();
            const listaFeriados = await respuestaFeriados.json();
    
            console.log('Eventos cargados:', listaEventos);  
            console.log('Feriados cargados:', listaFeriados); 
    
            return [...listaEventos, ...listaFeriados];
        } catch (error) {
            console.error('Error al cargar los eventos y feriados:', error);
            alert('No se pudieron cargar los eventos y feriados.');
            return [];
        }
    }
    
    async function inicializarCalendario() {
        const eventosFeriados = await obtenerEventosFeriados();

        const calendar = new FullCalendar.Calendar(calendarElement, {
            initialView: 'dayGridMonth',
            locale: 'es',
            headerToolbar: {
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth,timeGridWeek,timeGridDay'
            },
            events: eventosFeriados,  
            eventClick: function(info) {
                alert(`Evento: ${info.event.title}\nDescripción: ${info.event.extendedProps.description}`);
            }
        });

        calendar.render();
    }

    
    inicializarCalendario();
});