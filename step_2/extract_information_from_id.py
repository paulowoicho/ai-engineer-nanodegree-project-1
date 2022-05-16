from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient
import os

endpoint = "https://my-kiosk-form-recognizer.cognitiveservices.azure.com/"
credential = AzureKeyCredential("5dae340eca0e4c52b0d31d7f8d0f2d95")
form_recognizer_client = FormRecognizerClient(endpoint, credential)

for file in os.listdir("../licences"):
    with open(f"../licences/{file}", "rb") as licence_file:
        license = licence_file.read()

    id_content = form_recognizer_client.begin_recognize_identity_documents(license, content_type="image/png")
    id_content_result = id_content.result()

    id_content_result_dict = id_content_result[0].to_dict()

    # print extracted information
    print(f"Extracted information for {file}")
    for field_name, values in id_content_result_dict["fields"].items():
        print(values["name"], values["value"], values["confidence"])
    print("------------")
