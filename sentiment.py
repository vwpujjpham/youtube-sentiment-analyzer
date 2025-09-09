import numpy as np

def get_sentiment_key(s):
        if isinstance(s, (list, np.ndarray)):
            return s[0]
        return s
def overall_sentiment(like_counts, sentiments):
    if len(like_counts) != len(sentiments):
        return ValueError("Number of like_counts and number of sentiments do not match.")
    #for weighted_score, overall
    mapping = {
        "positive" : 1.0,
        "neutral" : 0.5,
        "negative" : 0.0
    }
    sentiment_scores = np.array([mapping[get_sentiment_key(sentiment)] for sentiment in sentiments])
    like_counts = np.array(like_counts)
    total_likes = np.sum(like_counts)
    if total_likes == 0:
        weighted_score = np.mean(sentiment_scores)
    else:
        weighted_score = np.sum(sentiment_scores * like_counts) / total_likes
    
    if weighted_score > 0.66:
        overall = "Positive"
    elif weighted_score < 0.33:
        overall = "Negative"
    else:
        overall = "Neutral"
    return weighted_score, overall

def weighted_percentages(like_counts, sentiments):
    if len(like_counts) == 0:
        return 0.33,0.33,0.33
    sentiments = [get_sentiment_key(s) for s in sentiments]
    sentiments = np.array(sentiments)
    like_counts = np.array(like_counts)

    positive_likes,neutral_likes,negative_likes = 0,0,0
    for count,sentiment in zip(like_counts, sentiments):
        if sentiment == "positive":
            positive_likes += count + 1
        elif sentiment == "neutral":
            neutral_likes += count + 1
        else:
            negative_likes += count + 1

    total_weight = positive_likes + neutral_likes + negative_likes + 100 #scraper maxResults=100
    return positive_likes/total_weight, neutral_likes/total_weight, negative_likes/total_weight

def styled_sentiment_label(sentiment):
    sentiment = sentiment[0]  # if predict_sentiment returns an array
    color_map = {
        "positive": "#33d074",
        "neutral": "#bdc3c7",
        "negative": "#f56555"
    }
    color = color_map.get(sentiment, "#bdc3c7")
    return f'<span style="background-color:{color}; color:white; padding:3px 5px; border-radius:10px;">{sentiment}</span>'

