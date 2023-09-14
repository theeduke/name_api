from flask import Flask, jsonify, request, abort
from dotenv import load_dotenv
load_dotenv
import os
import psycopg2
DATABASE_URI=os.getenv("DATABASE_URI")

app = Flask(__name__)

#Define Database Connection
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URI)
    return conn

#Create Database Table
def create_table():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
    conn.commit()
    conn.close()

#Create Person
@app.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()
    #if 'name' not in data or 'age' not in data:
        #abort(400) # Bad request
    name = data.get['name']
    age = data.get['age']

    conn = get_db_connection()
    conn.execute('INSERT INTO persons (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Person created successfully!'}), 201

#Read Person
@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    conn = get_db_connection()
    person = conn.execute('SELECT * FROM persons WHERE id = ?', (user_id,)).fetchone()
    conn.close()

    if person is None:
        abort(404) # Not found

    return jsonify({'id': person['id'], 'name': person['name'], 'age': person['age']}), 200

#Update Person
@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    conn = get_db_connection()
    conn.execute('UPDATE persons SET name = ?, age = ? WHERE id = ?', (name, age, user_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Person updated successfully!'}), 200

#Delete Person
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM persons WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Person deleted successfully!'}), 200

if __name__ == '__main__':
    create_table()
    app.run(debug=True)