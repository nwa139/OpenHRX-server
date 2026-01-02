#                      OpenHRX: Free and Open Source EMS
#                   Copyright (C) 2025-2026  <name of author>

import json
from datetime import datetime
from box import Box
import psycopg2

database="postgres"
host="127.0.0.1"
port=5432
user="postgres"
password="13009#"

def get_config():
    with open("config.json") as f:
        config = Box(json.load(f))
    return config

def get_conn():
    return psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password)

def ensure_db():
    try:
        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
        return True
    except Exception as e:
        return f"[DB Error/{datetime.now().strftime("%H:%M:%S")}]: {e}"

def get_employees():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""
                    SELECT employee_id,
                           first_name,
                           last_name,
                           birth_date,
                           manager_id,
                           job_title,
                           department_id,
                           office_id
                    FROM "Employees"
                    ORDER BY employee_id
                    """)
        rows = cur.fetchall()
        print(rows)
        employees = []
        for row in rows:
            employees.append({
                "employee_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "birth_date": row[3],
                "manager_id": row[4],
                "job_title": row[5],
                "department": row[6],
                "office": row[7]
            })
        return employees




def get_employee(employee_id):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""SELECT employee_id,
                              first_name,
                              last_name,
                              birth_date,
                              phone_number,
                              professional_email,
                              personal_email,
                              country,
                              region,
                              city,
                              zip_code,
                              house_number,
                              complementary,
                              department_id,
                              job_title,
                              manager_id,
                              pfp,
                              office_id,
                              address,
                              professional_phone_number
                       FROM "Employees"
                       WHERE employee_id = %s """, (employee_id,))
        row = cur.fetchone()
        print(row)
        if row:
            employee = {
                "employee_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "birth_date": row[3],
                "phone_number": row[4],
                "professional_email": row[5],
                "personal_email": row[6],
                "country": row[7],
                "region": row[8],
                "city": row[9],
                "zip_code": row[10],
                "house_number": row[11],
                "complementary": row[12],
                "department_id": row[13],
                "job_title": row[14],
                "manager_id": row[15],
                "pfp": row[16],
                "office_id": row[17],
                "address": row[18],
                "professional_phone_number": row[19]
            }

            for key, value in employee.items():
                if value is None:
                    employee[key] = ""

            return employee
        else:
            return None

#           -----------------------------
#           If you can read this,
#           you have voided your warranty
#           -----------------------------
#
#           joke :)

def get_hash(employee_id):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""SELECT hash
                       FROM "Employees"
                       WHERE employee_id = %s """, (employee_id,))
        row = cur.fetchone()
        print(row)
        if row:
            hash = row[0]
            return hash
        else:
            return None

def get_salt(employee_id):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""SELECT salt
                       FROM "Employees"
                       WHERE employee_id = %s """, (employee_id,))
        row = cur.fetchone()
        print(row)
        if row:
            salt = row[0]
            return salt
        else:
            return None