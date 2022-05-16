from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import os

FACE_ENDPOINT = "https://my-face-api.cognitiveservices.azure.com/"
FACE_KEY = "a2472dadf481446f9c4f4dfc633b1475"
face_client = FaceClient(FACE_ENDPOINT, CognitiveServicesCredentials(FACE_KEY))

for licence in os.listdir("../licences"):
    with open(f"../licences/{licence}", "rb") as licence_png:
        faces = face_client.face.detect_with_stream(licence_png)
        for face in faces:
            print(f'Found Face ID {face.face_id} in {licence}')