from ollamawrap import req, proc
from LoadData import LoadData


def makePrompt(prompt, loc, vacc, data):
    #print(data)
    demo_text = f"Generate a mission targeted towards people in {loc} about {vacc}. Use the following survey responses:\n"
    for group in data:
        for row in group:
            #print(row)
            demo, spec, survey, val,desc = row
            demo_text += demo+f"({spec})\n"
            demo_text+=survey
            demo_text +=": "
            demo_text += str(val)+"\n"
        
    
    return [{"role":"user","content":demo_text},
        #{"role":"system","content":"Generate an appropriate announcement that will be released by public health officials."},
            #{"role":"user","content":data},
            #{"role":"user","content":f"Your announcement should be targeted toward the following group: {demographics}."},
{"role":"user","content":f"""{prompt}"""}]


class LlmBackbone:
    def __init__(self, data:LoadData, model:str="gemma3:270m"):
        self.data=data
        self.model=model
        self.last = "No previous query"
        
    def run(self,prompt, loc, vacc, filters):
        
        data = self.data(loc, vacc, filters)
        self.last = data
        for group in self.last:
            for row in group:
                demo, spec, survey, val = row
                if (loc, vacc, demo) in self.data.explanations:
                    
                    row.append(self.data.explanations[loc, vacc, demo])
                else:
                    print(list(self.data.explanations.keys()[0]), "=check=",(loc, vacc, demo))
                    print(len([i for i in list(self.data.explanations.keys()) if i[0] == loc]))
                    print(len([i for i in list(self.data.explanations.keys()) if i[1] == vacc]))
                    print(len([i for i in list(self.data.explanations.keys()) if i[2] == demo]))
                    
                    row.append("N/A")
        genprompt=makePrompt(prompt, loc, vacc, data)
        #print(genprompt)
        resp=req(self.model,genprompt)
        #print(resp)
        return proc(resp)
        #except Exception as e:
        #    return str(e)
    def prep_explanation(self, loc, vacc, demo, val):
        prompt  = f"""Restate the following statistic as a statement (i.e. People in this area have low confidence in vaccinations):

Demographic group:{demo} 
Vaccine: {vacc}
Percentage: {val}/100"""
        return proc(req(self.model, [{"role":"user","content":prompt}]))
        
if __name__ == "__main__":
    import LoadData
    
    back=LlmBackbone(lambda x:(None,None))
    print(back.run("1 sentence response that tells people to visit the doctor",None))