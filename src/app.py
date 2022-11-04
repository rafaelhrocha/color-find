from flask import Flask, request
import sqlite3 as lite
        
app = Flask(__name__)

def create_table():
    cursor, conn = get_db_connection()
    cursor.execute("""  
                    CREATE TABLE IF NOT EXISTS images(
                        id INTEGER PRIMARY KEY,
                        image TEXT,
                        color_one TEXT,
                        color_two TEXT,
                        color_three TEXT );
                    """)

def get_db_connection():
    conn = lite.connect('database.db')
    cursor = conn.cursor()
    return cursor, conn


@app.route('/a', methods=['POST'])
def insert_image():
    response = request.json
    
    cursor, conn = get_db_connection()
    cursor.execute("""
                    INSERT INTO images(image) VALUES (?);
                """, (response['image'],))      
    conn.commit()
    return "ok"


@app.route('/b', methods=['POST'])
def insert_colors():
    response = request.json

    cursor, conn = get_db_connection()
    cursor.execute("""
                    UPDATE images
                    SET color_one = ?, color_two = ?, color_three = ?
                    WHERE id = ?
                ;""", (response['color_one'], response['color_two'], response['color_three'], response['id'] ))
                
    conn.commit()
    return "ok"

create_table()
app.run()