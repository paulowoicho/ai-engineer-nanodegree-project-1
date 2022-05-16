from video_indexer import VideoIndexer
import io, os
from PIL import Image

CONFIG = {
    'SUBSCRIPTION_KEY': 'c89891de6fbe4c9eb5df01f82ca9cb8d',
    'LOCATION': 'trial',
    'ACCOUNT_ID': 'a8b6065d-1aa3-4629-bb96-f2da6890fe6c'
}

video_analysis = VideoIndexer(
    vi_subscription_key=CONFIG['SUBSCRIPTION_KEY'],
    vi_location=CONFIG['LOCATION'],
    vi_account_id=CONFIG['ACCOUNT_ID']
)

info = video_analysis.get_video_info('a7a855ac0a', video_language='English')

images = []
for thumbnail in info['videos'][0]['insights']['faces'][0]['thumbnails']:
    file_name = thumbnail['fileName']
    thumbnail_id = thumbnail['id']
    img_code = video_analysis.get_thumbnail_from_video_indexer('a7a855ac0a',  thumbnail_id)
    img_stream = io.BytesIO(img_code)
    img = Image.open(img_stream)
    images.append(img)

# create directory
if not os.path.exists("../thumbnail_images"):
    os.makedirs("../thumbnail_images")

# save directory
for i, img in enumerate(images):
    img.save('../thumbnail_images/paul-face' + str(i + 1) + '.jpg')