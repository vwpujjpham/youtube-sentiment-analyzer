<!DOCTYPE html>
<html lang="en">
<head></head>
<body>

  <h1>YouTube Sentiment Analyzer</h1>

  <p>A personal project that analyzes the sentiment of YouTube video comments using natural language processing (NLP) and presents the results in a user-friendly Streamlit app.</p>

  <p><strong>Try it live on Streamlit Community Cloud:</strong> 
    <a href="https://youtube-sentiment-analyzer-k9hvre3vipgdbqb9hxfrbt.streamlit.app/" target="_blank">
      YouTube Sentiment Analyzer
    </a>
  </p>

  <hr>

  <h2>Features</h2>
  <ul>
    <li>Fetches comments from any public YouTube video.</li>
    <li>Performs sentiment analysis (positive, negative, neutral) on the comments.</li>
    <li>Displays interactive visualizations and summaries of sentiment trends.</li>
    <li>Built with Python, Streamlit, and Google YouTube API.</li>
  </ul>

  <hr>

  <h2>Installation / Running Locally</h2>
  <ol>
    <li><strong>Clone the repository:</strong>
      <pre><code>git clone https://github.com/vwpujjpham/youtube-sentiment-analyzer.git
cd youtube-sentiment-analyzer</code></pre>
    </li>
    <li><strong>Create and activate a virtual environment:</strong>
      <pre><code>python3 -m venv myenv
source myenv/bin/activate  # Mac/Linux
# myenv\Scripts\activate   # Windows</code></pre>
    </li>
    <li><strong>Install dependencies:</strong>
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Set your YouTube API key as an environment variable:</strong>
      <pre><code>export API_KEY="YOUR_YOUTUBE_API_KEY"  # Mac/Linux
# set API_KEY="YOUR_YOUTUBE_API_KEY"          # Windows</code></pre>
    </li>
    <li><strong>Run the Streamlit app:</strong>
      <pre><code>streamlit run app.py</code></pre>
    </li>
  </ol>

  <hr>

  <h2>Usage</h2>
  <ul>
    <li>Enter a YouTube video URL or ID in the input box.</li>
    <li>The app will fetch comments and display:
      <ul>
        <li>Sentiment breakdown (positive, negative, neutral)</li>
        <li>Word cloud of common words</li>
        <li>Interactive charts of sentiment trends</li>
      </ul>
    </li>
  </ul>

  <hr>

  <h2>Technologies</h2>
  <ul>
    <li>Python 3.10+</li>
    <li>Streamlit</li>
    <li>Google API Client (<code>googleapiclient</code>)</li>
    <li>NLP libraries (<code>nltk</code>, <code>textblob</code> or <code>vaderSentiment</code>)</li>
    <li>Pandas & Altair for data processing and visualization</li>
  </ul>

  <hr>

  <h2>Notes</h2>
  <ul>
    <li>Make sure your API key has access to the YouTube Data API v3.</li>
    <li>The app fetches a limited number of comments per video to respect API quotas.</li>
  </ul>

  <hr>

  <h2>License</h2>
  <p>This project is for personal use and learning purposes.</p>

</body>
</html>
