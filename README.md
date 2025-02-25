# Hospitality_process

Project Overview
The project aims to digitalize the hospitality process for group accommodation. It involves a web application that allows users to upload two CSV files containing group information and hostel information. The application processes these files and allocates rooms to the groups based on certain criteria, ensuring that members of the same group stay together, room capacities are not exceeded, and gender-specific accommodations are respected.

Project Components

Frontend:

HTML (index.html): Provides the structure and layout for the web page.
CSS (styles.css): Styles the web page to make it visually appealing.
JavaScript (scripts.js): Handles the file upload, communicates with the backend, and displays the results.

Backend:
Python (app.py): Uses Flask to handle file uploads, process CSV files, allocate rooms, and return the results.

Logic and Flow  -

Frontend Logic:

HTML Structure (index.html):
Contains a form with file inputs for uploading the group and hostel CSV files.
Displays the results and provides a download link for the allocation CSV.

CSS Styling (styles.css):
Styles the form, buttons, and result container to ensure a user-friendly interface.

JavaScript Handling (scripts.js):
Adds an event listener to the form submission.
Prevents the default form submission behavior and gathers the uploaded files.
Sends the files to the backend using a fetch request.
Parses the JSON response from the backend and displays the allocation results.
Provides a link to download the allocation CSV.

Backend Logic:

File Upload Handling (app.py):

Uses Flask to create a web server that listens for file uploads.
Reads the uploaded CSV files into pandas DataFrames.
Processes the data to allocate rooms based on the given criteria.
Returns the allocation results as JSON and a CSV string.
Room Allocation Logic:

Filters hostels by gender.
Iterates through the groups and allocates members to appropriate rooms.
Ensures that room capacities are not exceeded and that members of the same group stay together as much as possible.

Usage -

Step 1: Open the Web Application

Open the web application in your browser by navigating to the URL where it is hosted.
Step 2: Upload CSV Files

Upload the Group Information CSV file and the Hostel Information CSV file using the provided form.
Step 3: Allocate Rooms

Click the "Allocate Rooms" button to submit the form.
Step 4: View Results

The application will process the files and display the room allocation results on the page.
You can also download the allocation results as a CSV file.
Example CSV Files
Group Information CSV (group_info.csv):

sql
Group ID,Members,Gender
101,3,Boys
102,4,Girls
103,2,Boys
104,5,Girls
105,8,5 Boys & 3 Girls
Hostel Information CSV (hostel_info.csv):

css
Hostel Name,Room Number,Capacity,Gender
Boys Hostel A,101,3,Boys
Boys Hostel A,102,4,Boys
Girls Hostel B,201,2,Girls
Girls Hostel B,202,5,Girls
Example Output
Room Allocation Results:

css
Group ID,Hostel Name,Room Number,Members Allocated
101,Boys Hostel A,101,3
102,Girls Hostel B,202,4
103,Boys Hostel A,102,2
104,Girls Hostel B,202,5
105,Boys Hostel A,102,4
105,Girls Hostel B,201,3
Deployment
To deploy this project, you can host the frontend files (HTML, CSS, JavaScript) on any static web hosting service (like GitHub Pages, Netlify, or Vercel). The backend can be hosted on any platform that supports Flask (like Heroku, PythonAnywhere, or AWS).

This project provides a user-friendly interface for managing group accommodations in hostels, making the process more efficient and organized.