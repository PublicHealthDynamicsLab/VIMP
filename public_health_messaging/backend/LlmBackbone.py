from ollamawrap import req, proc
from LoadData import LoadData


def makePrompt(prompt, loc, vacc, data):
    print(data)
    demo_text = f"Generate a mission targeted towards people in {loc} about {vacc}. Use the following survey responses:\n"
    for group in data:
        for row in group:
            print(row)
            demo, spec, survey, val = row
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
        
    def run(self,prompt, loc, vacc, filters):
        
        data = self.data(loc, vacc, filters)
        genprompt=makePrompt(prompt, loc, vacc, data)
        print(genprompt)
        resp=req(self.model,genprompt)
        print(resp)
        return proc(resp)
        #except Exception as e:
        #    return str(e)
        
if __name__ == "__main__":
    import LoadData
    
    back=LlmBackbone(lambda x:(None,None))
    print(back.run("1 sentence response that tells people to visit the doctor",None))