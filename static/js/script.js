async function fetchData(gender) {
    try {
        // Fetch data from the Flask API
      
        const url = `/standings_data?option=${encodeURIComponent(gender)}`;
        const response = await fetch(url);

        // Check if the response is OK (status code 200)
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        // Parse JSON data
        const data = await response.json();
        
        // Skip the first row (headers) and get the rest of the data
        const tableData = data.slice(1);
        
        // Populate the table
        const table = document.getElementById('data-table');
        
        // Create table headers
        const headers = ['Team', 'GP', 'W', 'L', 'OTL', 'SOL', 'Last 10', 'Streak', 'GF', 'GA', 'G Diff', 'PTS', 'Pt %']; // First row of data as headers
        let thead = '<tr>';
        headers.forEach(header => thead += `<th>${header}</th>`);
        thead += '</tr>';
        
        // Create table rows
        let tbody = '<tbody>';
        tableData.forEach(row => {
            tbody += '<tr>';
            row.forEach(cell => tbody += `<td>${cell}</td>`);
            tbody += '</tr>';
        });
        tbody += '</tbody>';
        
        // Insert headers and rows into the table
        table.innerHTML = thead + tbody;
        
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}