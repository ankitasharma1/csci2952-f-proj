from constants import CONFIG_FILE
import yaml

class Parser:
    """
    Parser creates a knowledge base for the program based on the configuration file. Its purpose is similar to DNS.
    """
    def __init__(self):
        self.hospitals = dict()
        self.physicians = dict()
        self.physicians_ids = dict()
        self.patients = dict()
        self.patients_ids = dict()
        self.patients_cards = dict()
        self.patients_priv_key_path = dict()
        self.bc_address = None
        self.bc_port = None
        self.parse()
    
    def parse(self):
        with open(CONFIG_FILE, 'r') as f:
            doc = yaml.load(f)
    
        hospitals = doc['hospitals']    
        physicians = doc['physicians']
        patients = doc['patients']
        bc_proxy_server = doc['bc_proxy_server']    

        # BC Proxy Server.
        self.bc_address = bc_proxy_server['address']
        self.bc_port = bc_proxy_server['port']

        # Hospitals.	
        for hospital in hospitals:
            address = hospitals[hospital]['address']
            port = int(hospitals[hospital]['port'])
            self.hospitals.update({hospital: (address, port)}) 

        # Physicians.               
        for physician in physicians:
            address = physicians[physician]['address']
            port = int(physicians[physician]['port'])
            name = physicians[physician]['name']
            phys_id = physicians[physician]['physician_id']
            self.physicians.update({name: (address, port)})
            self.physicians_ids.update({name: phys_id})

        # Patients.
        for patient in patients:
            address = patients[patient]['address']
            port = int(patients[patient]['port'])
            name = patients[patient]['name']
            patient_id = patients[patient]['patient_id']
            card = patients[patient]['card']
            priv_key_path = patients[patient]['priv_key']
            self.patients.update({name: (address, port)})
            self.patients_ids.update({name: patient_id})
            self.patients_cards.update({name: card})
            self.patients_priv_key_path.update({name: priv_key_path})

    # BC Proxy Server.
    def get_bc_contact_info(self):
        return(self.bc_address, self.bc_port)

    # Hospitals.	
    def get_hosp_names(self):
        return self.hospitals.keys()

    def get_hosp_names_string(self):
        hosp_names = ""
        for i, hosp_name in enumerate(self.hospitals.keys()):
            if i == len(self.hospitals.keys()):
                hosp_names += hosp_name
            else:
                hosp_names += hosp_name + ","
        return hosp_names

    def valid_hosp(self, hospital):
        return hospital in self.hospitals

    def get_hosp_contact_info(self, hospital):
        if hospital in self.hospitals:
            return self.hospitals.get(hospital)
        print("NOT FOUND")
        print(hospital)
        print(self.hospitals)
        return None

    # Physicians.               
    def get_phys_names(self):
        return self.physicians.keys()

    def get_phys_names_string(self):
        phys_names = ""
        for i, phys_name in enumerate(self.physicians.keys()):
            if len(self.physicians) == i:
                phys_names += phys_name
            else:
                phys_names += phys_name + ","
        return phys_names

    def valid_phys(self, phys):
        return phys in self.physicians

    def get_phys_id(self, phys):
        if phys in self.physicians_ids:
            return self.physicians_ids.get(phys)
        return None

    def get_phys_contact_info(self, phys):
        if phys in self.physicians:
            return self.physicians.get(phys)
        return None

    # Patients.
    def get_patient_names(self):
        return self.patients.keys()

    def get_patient_names_string(self):
        patient_names = ""
        for patient_name in self.patients.keys():
            if len(patient_names) == 0:
                patient_names = patient_names + "\n" + patient_name + "\n"
            else:
                patient_names = patient_names + patient_name + "\n"
        return patient_names

    def valid_patient(self, patient):
        return patient in self.patients

    def get_patient_id(self, patient):
        if patient in self.patients_ids:
            return self.patients_ids.get(patient)
        return None

    def get_patient_contact_info(self, patient):
        if patient in self.patients:
            return self.patients.get(patient)
        return None

    def get_patient_card(self, patient):
        if patient in self.patients_cards:
            return self.patients_cards.get(patient)
        return None

    def get_patient_priv_key_path(self, patient):
        if patient in self.patients_priv_key_path:
            return self.patients_priv_key_path.get(patient)
        return None
