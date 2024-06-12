import sqlite3 as sql

from django import db

def add_patient(patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    addPatient_command = """ INSERT INTO USERS(patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address) VALUES {}"""
    data = (patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address)

    cursor.execute(addPatient_command.format(data))

    conn.commit()
    conn.close()


def print_all():
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    cursor.execute(""" SELECT * from patient """)
    list_all = cursor.fetchall()
    
    conn.close()



def search_patient(patient_name):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    searchPatient_command = """ SELECT * from patient WHERE patient_name = '{}' """
    cursor.execute(searchPatient_command.format(patient_name))

    patient = cursor.fetchone()

    conn.close()
    return patient



def delete_patient(patient_name):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    deletePatient_command = """ DELETE from patient WHERE patient_name = '{}' """
    cursor.execute(deletePatient_command.format(patient_name))

    conn.commit()
    conn.close()
    


def add_report(report_id,report_date,report_content):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    addReport_command = """ INSERT INTO medicalreport (report_id,report_date,report_content) VALUES {}"""
    data = ()

    cursor.execute(addReport_command.format(data))

    conn.commit()
    conn.close()



def search_report(report_id):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    searchReport_command = """ SELECT * from medicalreport WHERE report_id = '{}' """
    cursor.execute(searchReport_command.format(report_id))

    report = cursor.fetchone()

    conn.close()
    return report




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
