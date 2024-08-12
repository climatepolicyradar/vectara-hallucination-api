from flask import Flask, request, jsonify
from typing import Optional
import torch
from transformers import AutoModelForSequenceClassification

app = Flask(__name__)

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

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    context = data.get('context')
    response = data.get('response')

    if not context or not response:
        return jsonify({"error": "Both context and response are required"}), 400

    score = vectara.evaluate(context, response)

    if score is None:
        return jsonify({"error": "Evaluation failed"}), 500

    return jsonify({
        "score": score
    })
    
    
@app.get("/health")
async def get_health():
    """ Get application health.  """
    return {"status": "OK"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)