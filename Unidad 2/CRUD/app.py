# Nombre: Eder Gael Saldaña Galván
# Fecha: 10/Noviembre/2023
# Descripción: CRUD para crear un servidor WEB para utilizar los métodos de GET, PUT, POST y DELETE enfocado hacia jugadores
# de fútbol

import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crud.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET: Muestra todos los jugadores en la base de datos
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('nomJug')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM jugador')
    data = cursor.fetchall()
    for reg in data:
       registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))

#Método PUT: Inserta un jugador nuevo en la base de datos
@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO jugador(uid, nomJug, apePat, apeMat, edadJug, equipoJug, altJug, nacJug) VALUES(?,?,?,?,?,?,?,?)'
    cursor.execute(insert, [record['uid'], record['nomJug'],record['apePat'],record['apeMat'],record['edadJug'],record['equipoJug'],record['altJug'],record['nacJug'],])
    conn.commit()
    conn.close()
    return jsonify(record)

# Método POST: Actualiza el nombre de un jugador que ya está en la base de datos
@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'UPDATE jugador SET nomJug = ? WHERE uid= ?'
    cursor.execute(delete, [record['nomJug'], record['uid']])
    conn.commit()
    conn.close()
    return jsonify(record)

# Método DELETE: Borra un jugador de la base de datos según su UID
@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM jugador WHERE uid= ?'
    cursor.execute(delete, [record['uid']])
    conn.commit()
    conn.close()
    return jsonify(record)
    
app.run(debug=True)