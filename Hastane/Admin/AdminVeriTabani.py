import sqlite3 as sql

from django import db


#Hasta Ekleme
def add_patient(patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    addPatient_command = """ INSERT INTO HastaYonetimi_patient(patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address) VALUES {}"""
    data = (patient_id,patient_name,patient_last_name,p_birth_date,p_gender,phone_number,p_address)

    cursor.execute(addPatient_command.format(data))

    conn.commit()
    conn.close()


#Bütün hastaları görüntüleme
def print_allPatients():
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    cursor.execute(""" SELECT * from HastaYonetimi_patient """)
    list_all = cursor.fetchall()
    
    conn.close()


#Belli Bir Hastayı Aratma
def search_patient(patient_name):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    searchPatient_command = """ SELECT * from HastaYonetimi_patient WHERE patient_name = '{}' """
    cursor.execute(searchPatient_command.format(patient_name))

    patient = cursor.fetchone()

    conn.close()
    return patient


#Hasta Silme
def delete_patient(patient_name):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    deletePatient_command = """ DELETE from HastaYonetimi_patient WHERE patient_name = '{}' """
    cursor.execute(deletePatient_command.format(patient_name))

    conn.commit()
    conn.close()

#----------------------------------------------------------------------------------------------

#Tıbbi Rapor Ekleme
def add_report(report_id,report_date,report_content):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    addReport_command = """ INSERT INTO RaporYonetimi_medicalreport(report_id,report_date,report_content) VALUES {}"""
    data = ()

    cursor.execute(addReport_command.format(data))

    conn.commit()
    conn.close()


#Tıbbi Rapor Görüntüleme
def search_report(report_id):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    searchReport_command = """ SELECT * from RaporYonetimi_medicalreport WHERE report_id = '{}' """
    cursor.execute(searchReport_command.format(report_id))

    report = cursor.fetchone()

    conn.close()
    return 



#Rıbbi Rapor Silme
def delete_report(report_id):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    deleteReport_command = """ DELETE from RaporYonetimi_medicalreport WHERE report_id = '{}' """
    cursor.execute(deleteReport_command.format(report_id))

    conn.commit()
    conn.close()



#--------------------------------------------------------------------------------------------


#Randevu Görüntüleme(hasta id'sine göre)
def search_appointment(patient_id):
    conn = sql.connect('sb.sqlite3')
    cursor = conn.cursor()

    searchAppointment_command = """ SELECT * from RandevuYonetimi_appointment WHERE patient_id = '{}' """
    cursor.execute(searchAppointment_command.format(patient_id))

    appointment = cursor.fetchone()

    conn.close()
    return appointment



#Randevu Ekleme
def add_appointment(appointment_id,appointment_date,appointment_time,doctor_id,patient_id):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    addAppointment_command = """ INSERT INTO RandevuYonetimi_appointment(appointment_id,appointment_date,appointment_time,doctor_id,patient_id) VALUES {}"""
    data = (appointment_id,appointment_date,appointment_time,doctor_id,patient_id)

    cursor.execute(addAppointment_command.format(data))

    conn.commit()
    conn.close()


#Randevu Silme
def delete_appointment(appointment_id):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    deleteAppointment_command = """ DELETE from RandevuYonetimi_appointment WHERE appointment_id = '{}' """
    cursor.execute(deleteAppointment_command.format(appointment_id))

    conn.commit()
    conn.close()



#----------------------------------------------------------------------------------------------


#Doktor Ekleme
def add_doctor(doctor_id,doctor_name,doctor_last_name,speciality,hospital_works_in):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    addDoctor_command = """ INSERT INTO DoktorYonetimi_doctor(doctor_id,doctor_name,doctor_last_name,speciality,hospital_works_in) VALUES {}"""
    data = (doctor_id,doctor_name,doctor_last_name,speciality,hospital_works_in)

    cursor.execute(addDoctor_command.format(data))

    conn.commit()
    conn.close()


#Bütün Doktorları Görüntüleme
def print_allDoctors():
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    cursor.execute(""" SELECT * from DoktorYonetimi_doctor """)
    list_all = cursor.fetchall()
    
    conn.close()


#Belirli Bir Doktoru Görüntüleme
def search_Doctor(doctor_name):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    searchDoctor_command = """ SELECT * from DoktorYonetimi_doctor WHERE doctor_name = '{}' """
    cursor.execute(searchDoctor_command.format(doctor_name))

    doctor = cursor.fetchone()

    conn.close()
    return doctor


#Doktor Silme
def delete_doctor(doctor_name):
    conn = sql.connect('db.sqlite3')
    cursor = conn.cursor()

    deleteDoctor_command = """ DELETE from DoktorYonetimi_doctor WHERE doctor_name = '{}' """
    cursor.execute(deleteDoctor_command.format(doctor_name))

    conn.commit()
    conn.close()