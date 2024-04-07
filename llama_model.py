from pydantic import BaseModel

class LlamaModel(BaseModel):
    @property
    def name(self)->str:
        raise NotImplementedError()
    
    @property
    def prompt_prefix(self) ->str:
        raise NotImplementedError()


class Llama7B(LlamaModel):
    
    @property
    def name(self)->str:
        return 'codellama:7b'
    
    @property
    def prompt_prefix(self) ->str:
        return ''
    
class Llama7BPython(LlamaModel):
    
    @property
    def name(self)->str:
        return 'codellama:7b-python'
    
    @property
    def prompt_prefix(self)->str:
        return 'You are an expert python programmer that writes simple, concise code. '
    
class Llama7BInstruct(LlamaModel):
    
    @property
    def name(self)->str:
        return 'codellama:7b-instruct'
    
    @property
    def prompt_prefix(self)->str:
        return 'You are an expert programmer that writes simple, concise code and explanations. '
 

class Llama13B(LlamaModel):
    
    @property
    def name(self)->str:
        return 'codellama:13b'
    
    @property
    def prompt_prefix(self) ->str:
        return ''
    
class Llama13BPython(LlamaModel):
    
    @property
    def name(self)->str:
        return 'codellama:13b-python'
    
    @property
    def prompt_prefix(self)->str:
        return 'You are an expert python programmer that writes simple, concise code. '
    
class Llama13BInstruct(LlamaModel):
    
    @property
    def name(self)->str:
        return 'codellama:13b-instruct'
    
    @property
    def prompt_prefix(self)->str:
        return 'You are an expert programmer that writes simple, concise code and explanations. '
 
    
