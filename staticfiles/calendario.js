document.addEventListener("DOMContentLoaded", () => {
    const calendarElement = document.getElementById("calendar");
    const yearInput = document.getElementById("yearInput"); o
    const yearForm = document.getElementById("yearForm"); 

    
    let calendar = new FullCalendar.Calendar(calendarElement, {
        initialView: 'dayGridMonth',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay',
        },
        eventColor: '#FF5733', 
        eventClick: function (info) {
           
            alert(`Evento: ${info.event.title}\nDescripción: ${info.event.extendedProps.description}`);
        },
    });

    
    calendar.render();

    
    yearForm.addEventListener("submit", function (event) {
        event.preventDefault(); 

        const year = yearInput.value.trim(); 

        if (year) {
            fetch(`/programaApi/consultar-feriados/?year=${year}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`Error al consultar feriados: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    calendar.removeAllEvents(); 
                    calendar.addEventSource(data); 
                })
                .catch(error => {
                    console.error('Error al cargar los feriados:', error);
                });
        } else {
            alert("Por favor, ingresa un año válido.");
        }
    });
});