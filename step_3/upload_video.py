from video_indexer import VideoIndexer

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

uploaded_video_id = video_analysis.upload_to_video_indexer(
   input_filename='../video/video1771924254.mp4',
   video_name='kiosk-project-video',
   video_language='English'
)

print(uploaded_video_id)