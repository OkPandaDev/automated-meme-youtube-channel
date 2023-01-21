# Automated Meme YouTube Channel
This project scrapes reddit for the newest memes, compiles them into 1 compilation, and then uploads it to YouTube, within 10 minutes. 

# Setup

1. Download the github repository.

2. Download and install [Python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) if necessary.

3. Install the required packages with the following commands:

	Windows:
  
	- `pip install moviepy`
    - `pip install oauth2client`
    - `pip install --upgrade google-api-python-client`
    - `pip install --upgrade google-auth-oauthlib google-auth-httplib2`
    - `pip install gallery-dl`
    
	Mac/Linux:
  
	- `pip3 install moviepy`
    - `pip3 install oauth2client`
    - `pip3 install --upgrade google-api-python-client`
    - `pip3 install --upgrade google-auth-oauthlib google-auth-httplib2`
    - `pip3 install gallery-dl`
    
4. Follow [this](https://www.youtube.com/watch?v=aFwZgth790Q&t=1067s&ab_channel=TonyTeachesTech) link to get your OAuth Credentials.

5. Navigate to the scrape folder via terminal, type `python scrape.py`, and input the name of the subreddit you want to scrape, as well as how many videos to scrape. Go to the gallery-dl folder and drag all the videos to the memes folder in compile.

6. Navigate to the clean folder via terminal, type `python clean.py`, and input the path to the memes folder. This will remove everything in the folder that isn't a video.

7. Go to the compile folder and open `compile.py`. Scroll to the bottom and replace YOUR_AUDIO_PATH with the folder you want to save the audio to. Do NOT remove output_audio.m4a. Do the same with YOUR_OUTPUT_PATH.

8. Edit client_secrets.json in the upload folder and add replace `YOUR_CLIENT_ID` with your client id, and replace `YOUR_CLIENT_SECRET` with your client secret.

9. Navigate to the upload folder via terminal, and type `python shortcut.py`. Fill in the required details for your video. Note that when it asks for the file path, put the video name at the end of the path. For example, if the path is`/users/john/video_to_upload` make it `/users/john/video_to_upload/outputseq.mp4`. outputseq.mp4 is the default file name set in `compile.py`, but it can be changed.

10. Enjoy your automated YouTube channel! To upload public videos, you have to complete an audit for the Youtube API. See the note in the [Google Documentation](https://developers.google.com/youtube/v3/docs/videos/insert). Without this, you can only post private videos, but they approve everyone. 

# Donations

I put a lot of hard work and time into this project, and if you would like to support me and my future projects, please consider donating a small amount to keep me motivated to keep making projects like these.

Bitcoin: `bc1qryssn8f9thvts4r4pq8yzpslpxu2uwjx0vgl3u`

Ethereum: `0x6017DEBB98a58935c656439568A3b3091D613672`
