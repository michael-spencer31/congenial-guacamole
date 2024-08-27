async function fetchData() {

    try {
        const response = await fetch('/data');
        const data = await response.json();
        const tbody = document.querySelector('#data-table tbody');

        tbody.innerHTML = '';

        data.forEach(row => {
            const tr = document.createElement('tr');
        })
    } catch (error) {
        console.error('Error fetching data:', error);
    }
    document.addEventListener('DOMContentLoaded', fetchData);
}