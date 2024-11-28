
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
    



   
    const eventosData = JSON.parse(listaEventos);
    
    const feriadosData = JSON.parse(listaFeriados);
    
    function renderizarCalendario(anio, mes) {
        const contenedor = document.getElementById('calendario');
        contenedor.innerHTML = ''; 

        
        const primerDia = new Date(anio, mes, 1);
        const ultimoDia = new Date(anio, mes + 1, 0);
        const totalDias = ultimoDia.getDate();

        
        const mapaFeriados = new Map(feriadosData.map(f => [f.nombre, f.descripcion, f.fecha_fin , f.fecha_fin]));
        const mapaEventos = new Map(eventosData.map(e => [e.nombre, e.descripcion, e.fecha_inicio, e.fecha_fin]));

        
        for (let dia = 1; dia <= totalDias; dia++) {
            const fecha = new Date(anio, mes, dia);
            const fechaISO = fecha.toISOString().split('T')[0];

            
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

    
    const hoy = new Date();
    renderizarCalendario(hoy.getFullYear(), hoy.getMonth());




    const fetchEvents = async () => {
        try {
            const response = await fetch(API_URL);
            if (response.ok) {
                const data = await response.json();
                renderCalendar(data.response.holidays.map(holiday => ({
                    fecha: holiday.date.iso,
                    nombre: holiday.name,
                    tipo: holiday.type[0]
                })));
            } else {
                console.error("Error al obtener los eventos.");
            }
        } catch (error) {
            console.error("Error al conectar con el servidor:", error);
        }
    };

    fetchEvents();
});