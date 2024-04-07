from typing import Dict
from collections import OrderedDict
import copy
from client_model import Message
from datetime import datetime



def update_chat_history(current_chat_id: int, initial_history:Dict[float, dict], prompt:str, role:str='user')-> dict:
    
    current_chat = copy.deepcopy(initial_history[current_chat_id])
    if not current_chat['title']:
        new_message = Message(id=datetime.timestamp(datetime.now()),role=role, content= prompt)
        current_chat['messages'].append(dict(new_message))
        title = current_chat['messages'][0]['content'][0:20] + '...'
        current_chat['title'] = title
    
    del initial_history[current_chat_id]
    history_updated = OrderedDict()
    history_updated[current_chat_id] = current_chat
    history_updated.update(initial_history)
    return history_updated
        
