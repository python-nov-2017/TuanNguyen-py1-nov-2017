import random 

class Patient(object):
    patient_id = 0 
    def __init__(self, name, allergy):
        Patient.patient_id+=1
        self.name = name
        self.allergy= allergy
        self.bed_num = 0


class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity

    def Admit(self, patient):
        if len(self.patients) == self.capacity:
            print "Hospital Capacity reached. Cannot accept anymore patients."
        else:
            list_bed = [item.bed_num for item in self.patients]       
            patient.bed_num = random.randint(1, self.capacity)
            while patient.bed_num in list_bed:
                patient.bed_num = random.randint(1, self.capacity)
            self.patients.append(patient)
            print "Successfully admit the patient"                        
        return self

    def Discharge(self, patient):
        for item in self.patients:
            if item.bed_num == patient.bed_num:
                self.patients.remove(item)
                patient.bed_num = 0
        return self

    def displayPatientList(self):
        for item in self.patients:
            print "Patient name:", item.name
            print "Bed number:", item.bed_num
        return self

p1 = Patient("Tuan", "aaa")
p2 = Patient("Minh", "bbb")
p3 = Patient("Nguyen", "ccc")

hospital = Hospital("HCM", 3)
hospital.Admit(p1)
hospital.Admit(p2)
hospital.Admit(p3)
hospital.displayPatientList()
hospital.Discharge(p2)
hospital.displayPatientList()
