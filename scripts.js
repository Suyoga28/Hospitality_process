// Event listener for the form submission
document.getElementById('upload-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    // Get the uploaded files
    const groupFile = document.getElementById('group-file').files[0];
    const hostelFile = document.getElementById('hostel-file').files[0];

    // Create a FormData object to send the files to the server
    const formData = new FormData();
    formData.append('group_file', groupFile);
    formData.append('hostel_file', hostelFile);

    // Send the files to the server using fetch
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    // Parse the JSON response
    const result = await response.json();
    
    // Display the result in the browser
    displayResult(result.allocation);
    
    // Enable the download link for the CSV file
    enableDownload(result.csv);
});

// Function to display the result in the browser
function displayResult(allocation) {
    const container = document.getElementById('result-container');
    container.innerHTML = '<h2>Room Allocation Result</h2>';
    
    allocation.forEach(item => {
        const div = document.createElement('div');
        div.textContent = `Group ID: ${item["Group ID"]}, Hostel Name: ${item["Hostel Name"]}, Room Number: ${item["Room Number"]}, Members Allocated: ${item["Members Allocated"]}`;
        container.appendChild(div);
    });
}

// Function to enable the download link for the CSV file
function enableDownload(csv) {
    const downloadLink = document.getElementById('download-link');
    downloadLink.style.display = 'block';
    downloadLink.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);
    downloadLink.download = 'room_allocation.csv';
    downloadLink.textContent = 'Download Allocation CSV';
}
