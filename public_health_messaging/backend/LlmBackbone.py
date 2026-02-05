from ollamawrap import req, proc
from pandas import DataFrame


def makePrompt(prompt, demographics, data):
    return [#{"role":"system","content":"Generate an appropriate announcement that will be released by public health officials."},
            #{"role":"user","content":data},
            #{"role":"user","content":f"Your announcement should be targeted toward the following group: {demographics}."},
{"role":"user","content":f"""{prompt}"""}]


class LlmBackbone:
    def __init__(self, data:DataFrame, model:str="gemma3:270m"):
        self.data=data
        self.model=model
        
    def run(self,prompt, filters):
        demographics, curdata = self.data(filters)
        #try:
        demographics=""
        curdata=""
        genprompt=makePrompt(prompt, demographics, curdata)
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