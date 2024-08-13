from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from typing import Optional
import torch
from transformers import AutoModelForSequenceClassification


class EvaluationRequest(BaseModel):
    context: str
    response: str

class EvaluationResponse(BaseModel):
    score: float


class Vectara:
    TYPE = "faithfulness"
    NAME = "vectara"
    MODEL_NAME = "vectara/hallucination_evaluation_model"
    MODEL_REVISION = "ade58fc7b0eeb92bac9bf2be0bbafdb1fd51d04a"

    def __init__(self):
        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.MODEL_NAME,
            revision=self.MODEL_REVISION,
            trust_remote_code=True,
        )

    def evaluate(self, context: str, response: str) -> float:
        pairs = zip([context], [response])
        with torch.no_grad():
            scores = self.model.predict(pairs).detach().cpu().numpy()
        return float(scores[0])



vectara = Vectara()

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/evaluate")
async def evaluate(request: EvaluationRequest):

    result = vectara.evaluate(request.context, request.response)
    if result is None:
        raise HTTPException(status_code=500, detail="Evaluation failed")

    return {
        "score": result
    }
    
@app.get("/")
async def get_health():
    """ Get application health.  """
    return {"status": "OK"}
