from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    age = request.form['age']
    position = request.form['position']

    # Check if the Excel file exists, if not, create it with headers
    try:
        player_data = pd.read_excel('player_data.xlsx')
    except FileNotFoundError:
        player_data = pd.DataFrame(columns=['Name', 'Age', 'Position'])
    
    # Append the new data to the DataFrame and save it to the Excel file
    new_entry = pd.DataFrame({'Name': [name], 'Age': [age], 'Position': [position]})
    player_data = pd.concat([player_data, new_entry], ignore_index=True)
    player_data.to_excel('player_data.xlsx', index=False)

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
