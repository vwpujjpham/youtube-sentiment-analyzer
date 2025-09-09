import streamlit as st
from scraper import get_comments
from commentparserforcsv import predict_sentiment
import pandas as pd
from sentiment import styled_sentiment_label, overall_sentiment
# import matplotlib.pyplot as plt

#Create virtual environment (place for just the project, 1 time only)
#python -m venv myenv
#To Activate virtual environment (myenv), run this on windows:
#.\myenv\Scripts\activate
#streamlit run app.py
#Run by in terminal doing streamlit run <file name>
st.set_page_config(
    page_title="Youtube Comment Sentiment Analyzer",
    #layout="wide"
)
st.title("Youtube Comment Sentiment Analyzer")
st.caption("Created by Jacob Pham using Streamlit, Pandas, Google Cloud")
video_link = st.text_input(label="Paste a Youtube Video Link to get Started!",placeholder="EX: https://www.youtube.com/watch?v=<video_id>",max_chars=256,icon="🔗")
comments = []
likes = []
sentiments =[]
url = None
# percpositive,percneutral,percnegative = (0.33,0.33,0.33)
#Parsing user given link
#FIND WAY TO GRACEFULLY HANDLE INVALID LINK
if video_link and "www.youtube.com/watch?v=" in video_link:
    st.write(f"Current Video: {video_link}")
    video_id = video_link.split("?v=")[1]
    timestamp_index = video_id.find("&")
    if timestamp_index != -1:
        video_id = video_id[:timestamp_index]
    response = get_comments(video_id)
    for item in response.get("items", []):
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        like_count = item["snippet"]["topLevelComment"]["snippet"]["likeCount"]
        sentiment = predict_sentiment(comment)
        comments.append(comment)
        likes.append(like_count)
        sentiments.append(sentiment)
    url = f"https://www.youtube.com/watch?v={video_id}"
else:
    if video_link:
        st.error("Please enter a valid Youtube video URL.")
st.video(url)
st.write(comments)
weighted_score, overall = overall_sentiment(likes,sentiments)
df = pd.DataFrame({
    "Comment": comments,
    "Like Count": likes,
    "Sentiment": sentiments
})

comments_tab, analysis_tab = st.tabs(["Top Comments", "Analysis"])
with comments_tab:
    with st.container(height=850):
        for i in range(len(comments)):
            #border:1px solid #ddd; border-radius:10px;
            st.markdown(f"""
                <div style="padding:10px;margin-bottom:10px;"> 
                    <b>Comment:</b> {comments[i]}<br>
                    <b>Likes:</b> {likes[i]}&nbsp;&nbsp;&nbsp;<b>Predicted Sentiment:</b> {styled_sentiment_label(sentiments[i])}
                </div>
            """, unsafe_allow_html=True)
with analysis_tab:
    with st.container():
        st.write("hello")
        # st.subheader(f"Weighted Sentiment Score: {weighted_score}   ->  Overall Sentiment: {overall}")
        # colors = ["#33d074","#bdc3c7","#f56555"]
        # sizes=[percpositive,percneutral,percnegative]
        # fig, ax = plt.subplots()
        # ax.pie(
        #     sizes,
        #     labels=["Positive","Neutral","Negative"],
        #     colors=["#33d074","#bdc3c7","#f56555"],
        # )
        # ax.axis("equal")
        # st.pyplot(fig)