import csv
from database import connect_database

def insert_data():
    conn = connect_database()
    curs = conn.cursor()
    sql = "insert into blood_sugar (device, serial_number, timestamp, device_type, past_blood_sugar, scan_blood_sugar) values (%s, %s, %s, %s, %s, %s)"
    
    try:
        f = open('user1.csv', 'r', encoding='utf-8')
        rd = csv.reader(f)
        lines = list(rd)

        def convert_to_int(value):
            if value is None:
                return 0
            else:
                try:
                    return int(value)
                except ValueError:
                    return 0

        for line in lines[3:]:
            print(line)
            curs.execute(sql, (line[0], line[1], line[2], int(line[3]), convert_to_int(line[4]), convert_to_int(line[5])))

        conn.commit()
        return {"message": "Data inserted successfully!"}
    except Exception as e:
        return {"message": f"Error: {str(e)}"}
    finally:
        if conn is not None:
            conn.close()
        if f is not None:
            f.close()
