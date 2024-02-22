import requests

API_URL = "https://api-inference.huggingface.co/models/Falconsai/text_summarization"
headers = {"Authorization": "Bearer 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"}

def get_Falconsai_response(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()