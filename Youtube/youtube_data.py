from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
import pprint 
import matplotlib.pyplot as pd

DEVELOPER_KEY = "....."
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results=1000,order="relevance", token=None, location=None, location_radius=None):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet", # Part signifies the different types of data you want 
    maxResults=max_results,
    location=location,
    locationRadius=location_radius).execute()

def read_youtube(list_title, start_year, end_year):
    tests = []

    for i in range(start_year, end_year+1):
        for title in list_title:
            tests.append(youtube_search("social " + title + ", Africa, "+str(i)))

    return tests


test = read_youtube(["concern", "problem", "challenge", "worry", "issue", "question"], 2020, 2020)


df_test = []
for t in test:

    t.keys()
    df_test.append(pd.DataFrame(data=t))
df = pd.concat(df_test)
# save to excel sheet
df.to_excel("concerns120202020.xlsx")

#     videos=channelId=channelTitle=categoryId=videoId=viewCount=likeCount=dislikeCount=commentCount=favoriteCount=category=tags  = []
    title = []
    channelId = []
    channelTitle = []
    categoryId = []
    videoId = []
    viewCount = []
    #likeCount = []
    #dislikeCount = []
    commentCount = []
    favoriteCount = []
    category = []
    tags = []
    videos = []
    #publishedAt = []
    
    for search_result in search_response.get("items", []):
        #pprint.pprint(search_result)
  
  
        if search_result["id"]["kind"] == "youtube#video":

            title.append(search_result['snippet']['title']) 

            videoId.append(search_result['id']['videoId'])

            response = youtube.videos().list(
                part='statistics, snippet',
                id=search_result['id']['videoId']).execute()

            channelId.append(response['items'][0]['snippet']['channelId'])
            channelTitle.append(response['items'][0]['snippet']['channelTitle'])
            categoryId.append(response['items'][0]['snippet']['categoryId'])
            favoriteCount.append(response['items'][0]['statistics']['favoriteCount'])
            viewCount.append(response['items'][0]['statistics']['viewCount'])
            #likeCount.append(response['items'][0]['statistics']['likeCount'])
            #publishedAt.append(response['items'][0]['statistics']['publishedAt'])
            #dislikeCount.append(response['items'][0]['statistics']['dislikeCount'])
 
        if 'commentCount' in response['items'][0]['statistics'].keys():
            commentCount.append(response['items'][0]['statistics']['commentCount'])
        else:
            commentCount.append([])
	  
        if 'tags' in response['items'][0]['snippet'].keys():
            tags.append(response['items'][0]['snippet']['tags'])
        else:
            tags.append([])
#     pprint.pprint(response)
    youtube_dict = {'tags':tags,'channelId':channelId,'channelTitle':channelTitle,'categoryId':categoryId,'title':title,'videoId':videoId,'viewCount':viewCount,'commentCount':commentCount,'favoriteCount':favoriteCount}

    return youtube_dict


