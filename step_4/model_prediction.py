from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os

ENDPOINT = "https://eastus.api.cognitive.microsoft.com/"
prediction_key = "26f2a89c67504ee185a86aba2b401007"
prediction_resource_id = "/subscriptions/f49e4f3a-a2de-4c88-94d0-30849314b513/resourceGroups/ODL-AIND-195659/providers/Microsoft.CognitiveServices/accounts/my-resource-name"

project_id = '1d0c2327-df49-459f-b5ab-9aeecb539567'
publish_iteration_name = "my-lighter-detection-model"

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

for file in os.listdir("../test_lighter_images"):
    with open(f"../test_lighter_images/{file}", "rb") as image_contents:
        results = predictor.detect_image(project_id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print(f"Found {prediction.tag_name} in {file} with {round(prediction.probability * 100, 2)}% probability")