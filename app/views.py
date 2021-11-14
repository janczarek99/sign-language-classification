from app import app

from .settings import settings
from .tasks import get_result_from_azure, get_predictions_above_threshold, prepare_photo

from flask import render_template, request, flash


@app.route(settings.BASE_ENDPOINT, methods=["GET", "POST"])
async def main():
	if request.method == "GET":
		return render_template("public/index.html", classification_endpoint=settings.BASE_ENDPOINT, html_upload_field_name=settings.HTML_UPLOAD_FIELD_NAME, error=None)
	
	else:
		photo = request.files.get(settings.HTML_UPLOAD_FIELD_NAME)

		if photo:
			photo_bytes = photo.stream.read()
			predictions = await get_result_from_azure(photo_bytes)
			if predictions:
				predictions_above_threshold = await get_predictions_above_threshold(predictions)
				return render_template("public/predictions.html", base_endpoint=settings.BASE_ENDPOINT, classification_endpoint=settings.BASE_ENDPOINT, html_upload_field_name=settings.HTML_UPLOAD_FIELD_NAME, predictions=predictions_above_threshold, uploaded_photo=prepare_photo(photo_bytes))
			else:
				return render_template("public/index.html", classification_endpoint=settings.BASE_ENDPOINT, html_upload_field_name=settings.HTML_UPLOAD_FIELD_NAME, error="Invalid API endpoint/key or some error with Azure API!")
	
		return render_template("public/index.html", classification_endpoint=settings.BASE_ENDPOINT, html_upload_field_name=settings.HTML_UPLOAD_FIELD_NAME, error="No image provided!")