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
sentiments = info['summarizedInsights']['sentiments']
for sentiment in sentiments:
    print(sentiment['sentimentKey'])

emotions = info['summarizedInsights']['emotions']
for emotion in emotions:
    print(emotion['type'])
