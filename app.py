from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    # Get the uploaded files
    group_file = request.files['group_file']
    hostel_file = request.files['hostel_file']

    # Read the CSV files into pandas DataFrames
    group_df = pd.read_csv(group_file)
    hostel_df = pd.read_csv(hostel_file)

    # Call the function to allocate rooms
    allocation = allocate_rooms(group_df, hostel_df)
    
    # Convert the allocation result to a DataFrame
    allocation_df = pd.DataFrame(allocation)

    # Convert the DataFrame to a CSV string
    allocation_csv = allocation_df.to_csv(index=False)

    # Return the JSON response with the allocation result and the CSV string
    return jsonify({'allocation': allocation_df.to_dict(orient='records'), 'csv': allocation_csv})

def allocate_rooms(group_df, hostel_df):
    allocation = []

    # Filter hostels by gender
    boys_hostels = hostel_df[hostel_df['Gender'] == 'Boys'].copy()
    girls_hostels = hostel_df[hostel_df['Gender'] == 'Girls'].copy()

    # Function to allocate a group to hostels
    def allocate_group(group, hostels):
        members_remaining = group['Members']
        for index, room in hostels.iterrows():
            if members_remaining <= 0:
                break
            if room['Capacity'] > 0:
                allocated = min(members_remaining, room['Capacity'])
                allocation.append({
                    'Group ID': group['Group ID'],
                    'Hostel Name': room['Hostel Name'],
                    'Room Number': room['Room Number'],
                    'Members Allocated': allocated
                })
                hostels.at[index, 'Capacity'] -= allocated
                members_remaining -= allocated

    # Allocate each group to appropriate hostels
    for _, group in group_df.iterrows():
        if 'Boys' in group['Gender']:
            allocate_group(group, boys_hostels)
        if 'Girls' in group['Gender']:
            allocate_group(group, girls_hostels)

    return allocation

if __name__ == '__main__':
    app.run(debug=True)
