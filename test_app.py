import json
import unittest
from app import app, Vectara

class TestHallucinationAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.vectara = Vectara()

    def test_evaluate_endpoint(self):
        payload = {
            "context": "The sky is blue.",
            "response": "The sky appears blue due to atmospheric scattering of sunlight."
        }
        response = self.app.post('/evaluate', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('score', data)
        self.assertIsInstance(data['score'], float)
        self.assertTrue(0 <= data['score'] <= 1)

    def test_evaluate_method(self):
        context = "The Earth orbits the Sun."
        response = "The Earth revolves around the Sun in an elliptical orbit."
        score = self.vectara.evaluate(context, response)
        self.assertIsInstance(score, float)
        self.assertTrue(0 <= score <= 1)

    def test_invalid_input(self):
        payload = {
            "context": "Test context",
            "invalid_key": "This should cause an error"
        }
        response = self.app.post('/evaluate', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
