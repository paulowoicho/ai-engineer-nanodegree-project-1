from video_indexer import VideoIndexer
import glob, os, sys, time, uuid
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import TrainingStatusType
from msrest.authentication import CognitiveServicesCredentials

FACE_ENDPOINT = "https://my-face-api.cognitiveservices.azure.com/"
FACE_KEY = "a2472dadf481446f9c4f4dfc633b1475"
face_client = FaceClient(FACE_ENDPOINT, CognitiveServicesCredentials(FACE_KEY))


PERSON_GROUP_ID = str(uuid.uuid4())
person_group_name = 'person-paul'
human_face_images = [file for file in glob.glob('../thumbnail_images/*.jpg')]


def build_person_group(client, person_group_id, pgp_name, human_face_images):
    """
    Azure Face SDK sample code
    # https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/Face/DetectIdentifyFace.py
    """
    print('Person group ID:', person_group_id)
    client.person_group.create(person_group_id = person_group_id, name=person_group_id)

    human_person = client.person_group_person.create(person_group_id, pgp_name)

    for image_p in human_face_images:
        with open(image_p, 'rb') as w:
            client.person_group_person.add_face_from_stream(person_group_id, human_person.person_id, w)

    client.person_group.train(person_group_id)

    while (True):
        training_status = client.person_group.get_training_status(person_group_id)
        print("Training status: {}.".format(training_status.status))
        if (training_status.status is TrainingStatusType.succeeded):
            break
        elif (training_status.status is TrainingStatusType.failed):
            client.person_group.delete(person_group_id=PERSON_GROUP_ID)
            sys.exit('Training the person group has failed.')
        time.sleep(5)

def detect_faces(client, query_images_list):
    print('Detecting faces in query images list...')

    face_ids = {}
    for image_name in query_images_list:
        image = open(image_name, 'rb')
        print("Opening image: ", image.name)
        time.sleep(24)

        faces = client.face.detect_with_stream(image)  

        for face in faces:
            print('Face ID', face.face_id, 'found in image', os.path.splitext(image.name)[0]+'.jpg')
            face_ids[image.name] = face.face_id

    return face_ids


build_person_group(face_client, PERSON_GROUP_ID, person_group_name, human_face_images)
ids = detect_faces(face_client, human_face_images)
print(ids)