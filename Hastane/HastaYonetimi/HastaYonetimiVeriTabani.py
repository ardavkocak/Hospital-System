import sqlite3 as sql
from django.db import connection
from django import db

class HastaClass(): 
    def __init__(self, patient_id, patient_name, patient_last_name, p_birth_date, p_gender, phone_number, p_adress):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_last_name = patient_last_name
        self.p_birth_date = p_birth_date
        self.p_gender = p_gender
        self.phone_number = phone_number
        self.p_adress = p_adress


#Hasta Ekleme
def add_patient(patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()
    
    addPatient_command = """ INSERT INTO HastaYonetimi_patient(patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address) VALUES {%s,%s,%s,%s,%s,%s,%s}"""
    data = (patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address)

    cursor.execute(addPatient_command , data)

    conn.commit()
    conn.close()

#Randevu Ekleme
def add_appointment(appointment_id,appointment_date,appointment_time,doctor_id,patient_id):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    addAppointment_command = """ INSERT INTO RandevuYonetimi_appointment (appointment_id,appointment_date,appointment_time,doctor_id,patient_id) VALUES {%s,%s,%s,%s,%s}"""
    data = (appointment_id,appointment_date,appointment_time,doctor_id,patient_id)

    cursor.execute(addAppointment_command.format(data))

    conn.commit()
    conn.close()


#Randevu Görüntüleme
def search_appointment(patient_id):
    conn = sql.connect('sb.sqlite3')
    cursor = conn.cursor()

    searchAppointment_command = """ SELECT * from RandevuYonetimi_appointment WHERE patient_id = '{%s}' """
    cursor.execute(searchAppointment_command.format(patient_id))

    appointment = cursor.fetchone()

    conn.close()
    return appointment


#Randevu Silme
def delete_appointment(appointment_id):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    deleteAppointment_command = """ DELETE from RandevuYonetimi_appointment WHERE appointment_id = '{%s}' """
    cursor.execute(deleteAppointment_command.format(appointment_id))

    conn.commit()
    conn.close()


#Bilgileri Güncelleme
def update_info(patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()
    
    updateInfo_command = """ UPDATE HastaYonetimi_patient SET 
    patient_id = '{%s}',
    patient_name = '{%s}',
    patient_last_name = '{%s}',
    p_birth_date = '{%s}',
    p_gender = '{%s}',
    phone_number = '{%s}',
    p_address = '{%s}'

    """

    cursor.execute(updateInfo_command.format(patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address))
    conn.commit()
    conn.close()






#Tüm Hastaları Yazdırma
def print_all():
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    cursor.execute(""" SELECT * from HastaYonetimi_patient """)
    list_all = cursor.fetchall()
    
    conn.close()


#Belli Bir Hastayı Yazdırma
def search_patient(patient_name):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    searchPatient_command = """ SELECT * from HastaYonetimi_patient WHERE patient_name = '{%s}' """
    cursor.execute(searchPatient_command.format(patient_name))

    patient = cursor.fetchone()

    conn.close()
    return patient


#Hasta Silme
def delete_patient(patient_name):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    deletePatient_command = """ DELETE from HastaYonetimi_patient WHERE patient_name = '{%s}' """
    cursor.execute(deletePatient_command.format(patient_name))

    conn.commit()
    conn.close()