from fastapi import FastAPI

from templates import BASE_TEMPLATE_MAP, PARAM_TEMPLATE_MAP
from pydantic import BaseModel
from typing import Dict, Any


class RequestBody(BaseModel):
    assistant_id: str
    api_key: str
    language: str
    capability_information: Dict[str, Any]

app = FastAPI()



def generate_code(assistant_id: str, api_key: str,
                         language: str, capability_information: dict,
                         ) -> str:

    generated_code = BASE_TEMPLATE_MAP[language].format(assistant_id=assistant_id, api_key=api_key)

    for param_name in capability_information['parameters']:
        generated_code += PARAM_TEMPLATE_MAP[language].format(param_name=param_name)



    return generated_code




@app.post("/generate_template")
async def generate_template(request_body: RequestBody):
    code = generate_code(request_body.assistant_id, request_body.api_key,
                       request_body.language, request_body.capability_information)
    return {"code": code}


