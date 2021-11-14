import aiohttp
from .settings import settings
from http import HTTPStatus

from PIL import Image
import base64
import io

async def get_result_from_azure(data):
	headers = {
		"Content-Type": "application/octet-stream",
		"Prediction-Key": settings.AZURE_CLASSIFICATION_API_KEY
	}
	try:
		async with aiohttp.ClientSession(headers=headers) as session:
			async with session.post(settings.AZURE_CLASSIFICATION_ENDPOINT, data=data) as response:
				if response.status == HTTPStatus.OK:				
					json_response = await response.json()
					return json_response.get("predictions", [])
	except:
		pass
	
	return None

async def get_predictions_above_threshold(predictions):
	predictions_above_threshold = []

	for prediction in predictions:
		if prediction.get("probability", 0) >= settings.CLASSIFICATION_THRESHOLD:
			prepared_prediction_obj = {
				"letter": prediction["tagName"],
				"value": _round_probability(prediction["probability"])
			}

			predictions_above_threshold.append(prepared_prediction_obj)

	return predictions_above_threshold


def prepare_photo(photo_bytes):
	# im = Image.open(photo_bytes)
	# data = io.BytesIO()
	# im.save(data, "JPEG")
	encoded_img_data = base64.b64encode(photo_bytes).decode("utf-8")
	return encoded_img_data
			
def _round_probability(prediction_probability):
	return f"{float(prediction_probability) * 100:.2f}"

