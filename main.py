from fastapi import FastAPI

import templates
from pydantic import BaseModel
from typing import List
import random

class RequestBody(BaseModel):
    assistant_id: str
    api_key: str
    query_list: List[str]
    capability_names: List[str]
    language: str
    

app = FastAPI()



def generate_code(assistant_id: str, api_key: str, query_list: List[str], capability_names: List[str], language: str) -> str:
    chosen_query = random.choice(query_list)
    generated_code = templates.BASE_TEMPLATE_MAP[language].format(assistant_id=assistant_id, api_key=api_key, chosen_query=chosen_query)

    for index, capability_name in enumerate(capability_names):
        if index == 0:
            generated_code += templates.IF_SYNTAX_MAP[language].format(capability_name=capability_name)
        else:
            generated_code += templates.ELIF_SYNTAX_MAP[language].format(capability_name=capability_name)
        generated_code += templates.COMMENT_SYNTAX_MAP[language].format(capability_name=capability_name)
    
    generated_code += templates.END_SYNTAX_MAP[language]




    return generated_code




@app.post("/generate_template")
async def generate_template(request_body: RequestBody):
    code = generate_code(**request_body.model_dump())
    return {"code": code}




