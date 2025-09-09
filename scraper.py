import pandas as pd
import os
import googleapiclient.discovery
from dotenv import load_dotenv
load_dotenv()
def get_comments(video_id):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("API_KEY")
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
    

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=300, #100 is max
        textFormat="plainText",        #html",
        order="relevance",  #"time",
        videoId=video_id
    )
    response = request.execute()

    return response