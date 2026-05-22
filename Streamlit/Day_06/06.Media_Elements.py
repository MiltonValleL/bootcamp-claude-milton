import streamlit as st

# --------------------------------------------------------------------
st.header("Display Image - st.image()")
# Display a JPG picture
st.image("resources/image.jpg", caption="Beautiful City", width=800)
st.divider()

# --------------------------------------------------------------------
# Display a MP4 Video
st.header("Display a MP4 Video")
video_file = open("resources/waterfalls.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)
st.divider()


# --------------------------------------------------------------------
# Display Audio
st.header("Display MP3 Audio")
audio_file = open("resources/audio.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/ogg")
st.divider()
# --------------------------------------------------------------------
