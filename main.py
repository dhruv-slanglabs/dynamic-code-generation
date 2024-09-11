from fastapi import FastAPI
from gen_code import generate_code
from pydantic import BaseModel
from typing import List


class RequestBody(BaseModel):
    assistant_id: str
    api_key: str
    query_list: List[str]
    capability_names: List[str]
    language: str
    

app = FastAPI()






@app.post("/generate_template")
async def generate_template(request_body: RequestBody):
    code = generate_code(**request_body.model_dump())
    return {"code": code}




