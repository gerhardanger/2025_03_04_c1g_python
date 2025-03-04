import sqlite3
from pathlib import Path


def execute_query_and_print_result(sql):

    BASE_PATH = Path(__file__).parent
    DB_PATH = BASE_PATH / "data/2025_03_03_Material_und_Gehalt_angereichert.db"

    connection = None

    try:
        connection = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
        cursor = connection.cursor()
        for row in cursor.execute(sql):
            print(row)
    except Exception as e:
        print(e)
    finally:
        connection.close()


def uebung_1():
    sql = "SELECT id, seriennummer, kaufdatum FROM Material WHERE typ = 'Laptop'"
    execute_query_and_print_result(sql)

def uebung_2():
    sql = """SELECT Mitarbeiter.vorname, Mitarbeiter.nachname,  Materialausgabe.ausgabedatum, Material.id
                FROM Mitarbeiter
                INNER JOIN Materialausgabe ON Mitarbeiter.id = Materialausgabe.mitarbeiter_id
                INNER JOIN Material ON Material.id = Materialausgabe.material_id
                WHERE Material.typ = 'Laptop'"""
    execute_query_and_print_result(sql)

def uebung_3():
    sql = """SELECT DISTINCT Mitarbeiter.vorname, Mitarbeiter.nachname
            FROM Mitarbeiter
            JOIN Materialausgabe ON Mitarbeiter.id = Materialausgabe.mitarbeiter_id"""
    execute_query_and_print_result(sql)

def uebung_4():
    sql = """SELECT  Mitarbeiter.vorname, Mitarbeiter.nachname
                FROM Mitarbeiter
                LEFT JOIN Materialausgabe ON Mitarbeiter.id = Materialausgabe.mitarbeiter_id
                WHERE Materialausgabe.id IS NULL"""
    execute_query_and_print_result(sql)

def uebung_5():
    sql = """SELECT count(*) AS cnt, Material.typ FROM Material 
                INNER JOIN Materialausgabe ON Materialausgabe.material_id = Material.id
                GROUP BY Material.typ
                ORDER BY cnt ASC, typ ASC"""
    execute_query_and_print_result(sql)

if __name__ == "__main__":
    uebung_1()
    uebung_2()
    uebung_3()
    uebung_4()
    uebung_5()

