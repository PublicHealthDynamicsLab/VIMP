from ollama import chat, pull
from ollama import ChatResponse

pulled={}
def req(model, messages, max_tokens = None, seed = None):
    if not model in pulled:
        pull(model)
    response: ChatResponse = chat(model=model, messages=messages,options={"max_tokens":max_tokens,"seed":seed})
    return response

def proc(text):
    if type(text) is str:
        return text
    else:
        try:
            return text.message.content
        except:
            print(text,type(text))
            exit()

if __name__ == "__main__":
    pull("gemma3:270m")
    print(proc(req("gemma3:270m",[{'role':"user","content":"How are you?"}],seed=10000)))
    