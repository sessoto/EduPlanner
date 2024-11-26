document.addEventListener("DOMContentLoaded", () => {
    const calendarElement = document.getElementById("calendar");
    const API_URL = "/eventos/api_eventos/";

    // Función para renderizar el calendario
    const renderCalendar = (events) => {
        const date = new Date();
        const year = date.getFullYear();
        const month = date.getMonth();

        // Obtener el primer día y el número de días del mes actual
        const firstDayIndex = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        // Nombres de los días de la semana
        const weekDays = ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"];
        calendarElement.innerHTML = `<div class="day-header">${weekDays.join("</div><div class='day-header'>")}</div>`;

        // Añadir espacios en blanco para los días antes del primer día del mes
        for (let i = 0; i < firstDayIndex; i++) {
            calendarElement.innerHTML += `<div class="day empty"></div>`;
        }

        // Rellenar el calendario con los días del mes
        for (let day = 1; day <= daysInMonth; day++) {
            const currentDate = new Date(year, month, day).toISOString().split("T")[0];
            let className = "day";

            // Verificar si el día es un evento o feriado
            const event = events.find(event => event.fecha === currentDate);
            if (event) {
                className += event.es_feriado ? " holiday" : " event";
            }

            calendarElement.innerHTML += `<div class="${className}">${day}</div>`;
        }
    };

    
    const fetchEvents = async () => {
        try {
            const response = await fetch(API_URL);
            if (response.ok) {
                const data = await response.json();
                renderCalendar(data.eventos); 
            } else {
                console.error("Error al obtener los eventos.");
            }
        } catch (error) {
            console.error("Error al conectar con el servidor:", error);
        }
    };

    fetchEvents(); 
});