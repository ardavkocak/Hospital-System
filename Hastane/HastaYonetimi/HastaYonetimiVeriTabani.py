import sqlite3 as sql

from django import db

def add_appointment(appointment_id,appointment_date,appointment_time,doctor_id,patient_id):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    addAppointment_command = """ INSERT INTO appointment (appointment_id,appointment_date,appointment_time,doctor_id,patient_id) VALUES {}"""
    data = (appointment_id,appointment_date,appointment_time,doctor_id,patient_id)

    cursor.execute(addAppointment_command.format(data))

    conn.commit()
    conn.close()


def search_appointment(patient_id):
    conn = sql.connect('sb.sqlite3')
    cursor = conn.cursor()

    searchAppointment_command = """ SELECT * from appointment WHERE patient_id = '{}' """
    cursor.execute(searchAppointment_command.format(patient_id))

    appointment = cursor.fetchone()

    conn.close()
    return appointment


def delete_appointment(appointment_id):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    deleteAppointment_command = """ DELETE from appointment WHERE appointment_id = '{}' """
    cursor.execute(deleteAppointment_command.format(appointment_id))

    conn.commit()
    conn.close()


def update_info(patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()
    
    updateInfo_command = """ UPDATE patient SET 
    patient_id = '{}',
    patient_name = '{}',
    patient_last_name = '{}',
    p_birth_date = '{}',
    p_gender = '{}',
    phone_number = '{}',
    p_address = '{}'

    """

    cursor.execute(updateInfo_command.format(patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address))
    conn.commit()
    conn.close()
    