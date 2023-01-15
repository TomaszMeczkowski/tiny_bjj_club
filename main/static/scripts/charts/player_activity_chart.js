export function wykres(chart_id, dane_daty, dane_dane, title_chart) {

    let ctx = document.getElementById(chart_id).getContext("2d");
    let lineChar = new Chart(ctx, {
        type: "line",
        data: {
            labels: dane_daty,
            datasets: [
                {
                    label: "Aktywność",
                    data: dane_dane,
                    fill: true,
                    borderColor: "rgb(75, 192, 192)",
                    lineTension: 0.1
                }
            ]
        },
        options:
        {
            responsive: true,
            scales: { y: { beginAtZero: true, title: { display: true, text: "Ilość treningów" } } },
            plugins: {
                title: {
                    display: true,
                    text: title_chart,
                    font: { size: 16, weight: "normal" }
                }
            }
        }
    });

}
