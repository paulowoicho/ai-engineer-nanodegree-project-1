from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://my-kiosk-form-recognizer.cognitiveservices.azure.com/"
credential = AzureKeyCredential("5dae340eca0e4c52b0d31d7f8d0f2d95")

form_training_client = FormTrainingClient(endpoint, credential)

# TRAIN
trainingDataUrl = "https://passengerkioskproj.blob.core.windows.net/model-training?sp=racwdli&st=2022-05-15T10:32:06Z&se=2022-05-15T18:32:06Z&spr=https&sv=2020-08-04&sr=c&sig=v0Ybd7L3yOB3OPwnZhidvfPD6goOAfrfXlyxhMCzfS8%3D"
training_process = form_training_client.begin_training(trainingDataUrl, use_training_labels=True)
custom_model = training_process.result()

# TEST
test_url = "https://raw.githubusercontent.com/udacity/cd0461-building-computer-vision-solutions-with-azure-project-starter/master/starter/boarding_pass_template/boarding-radha-s-kumar.pdf"
form_recognizer_client = FormRecognizerClient(endpoint, credential)
boarding_pass_content = form_recognizer_client.begin_recognize_custom_forms_from_url(model_id=custom_model.model_id, form_url=test_url)
boarding_pass_content_dict = boarding_pass_content.result()[0].to_dict()

# print extracted information
for field_name, values in boarding_pass_content_dict["fields"].items():
        print(f"{values['name']}: {values['value']} (Confidence: {values['confidence']})")
print("------------")
