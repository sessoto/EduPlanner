document.addEventListener("DOMContentLoaded", () => {
    const calendarElement = document.getElementById("calendar");
    const yearInput = document.getElementById("yearInput"); // Input para el año
    const yearForm = document.getElementById("yearForm"); // Formulario para enviar el año

    // Inicializar el calendario
    let calendar = new FullCalendar.Calendar(calendarElement, {
        initialView: 'dayGridMonth',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay',
        },
        eventColor: '#FF5733', // Color predeterminado para eventos
        eventClick: function (info) {
            // Mostrar información del evento al hacer clic
            alert(`Evento: ${info.event.title}\nDescripción: ${info.event.extendedProps.description}`);
        },
    });

    // Renderizar el calendario
    calendar.render();

    // Manejar el envío del formulario para actualizar los feriados
    yearForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevenir la recarga de la página

        const year = yearInput.value.trim(); // Obtener el año ingresado

        if (year) {
            fetch(`/programaApi/consultar-feriados/?year=${year}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`Error al consultar feriados: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    calendar.removeAllEvents(); // Limpiar eventos actuales
                    calendar.addEventSource(data); // Agregar nuevos eventos al calendario
                })
                .catch(error => {
                    console.error('Error al cargar los feriados:', error);
                });
        } else {
            alert("Por favor, ingresa un año válido.");
        }
    });
});