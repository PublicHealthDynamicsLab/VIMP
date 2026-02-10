import pandas as pd


class LoadData:
    def __init__(self, fpath="public_health_messaging/backend/National_Immunization_Survey_Fall_Respiratory_Virus_Module_(NIS-FRVM)__RespVaxView__Data___Centers_for_Disease_Control_and_Prevention_(cdc.gov)_20260203.csv"):
        self.data = pd.read_csv(fpath)
        self.quicks={}
        for loc in self.get_regions():
            for vacc in set(self.data["Vaccine"]):
                for demo in self.get_demographics():
                    for val in self.get_dropdowns(demo):
                        
                        self.quicks[(loc, vacc,demo,val)] =self.__filter(loc, vacc,demo, val)
                        break
                    break
                break
            
    def get_regions(self):
        return set(self.data["Geography"])
    
    def get_demographics(self):
        return set(self.data["Group Name"])
    
    def get_dropdowns(self, demographic):
        data = self.data.where(self.data["Group Name"] == demographic).dropna()
        return set(data["Group Category"])

    def __filter(self, loc=None, vacc=None, demographic=None, val=None):
        if (vacc, demographic, val) in self.quicks:
            return self.quicks[(vacc, demographic, val)]
        else:
            
            data=self.data.where(self.data["Group Name"]==demographic).dropna()
            data = data.where(data["Group Category"] == val).dropna()
            
            data=data.where(data["Geography"] == loc).dropna()
            #print(data["Vaccine"])
            data = data.where(self.data["Vaccine"] == vacc).dropna()
            
            ret = [(row["Group Name"], row["Group Category"], row["Indicator Name "], row["Estimate (%)"]) for i, row in data.iterrows()]
            
            if len(ret) > 0:
                return ret
            else:
                return [(demographic, val, "No survey exists", "n/a")]
    def __call__(self, loc, vacc, filters):
        results = []
        for filter in filters:
            for val in filters[filter]:
                results.append(self.__filter(loc, vacc, filter, val))
        if len(filters) == 0:
            results.append(self.__filter(loc, vacc, demographic="All adults 18+ years", val="All adults 18+ years"))
        
        print(results)
        return results
    
if __name__ == "__main__":
    data= LoadData()
    print(data.quicks)