import pandas as pd


class LoadData:
    def __init__(self, fpath="public_health_messaging/backend/National_Immunization_Survey_Fall_Respiratory_Virus_Module_(NIS-FRVM)__RespVaxView__Data___Centers_for_Disease_Control_and_Prevention_(cdc.gov)_20260203.csv"):
        self.data = pd.read_csv(fpath)
    
    def get_demographics(self):
        return set(self.data["Group Name"])
    
    def get_dropdowns(self, demographic):
        data = self.data.where(self.data["Group Name"] == demographic).dropna()
        return set(data["Group Category"])

    def __call__(self, filters):
        return "people",[]