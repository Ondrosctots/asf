import streamlit as st
import pandas as pd
import urllib.parse

# --- CONFIG ---
WORKER_URL = "https://morning-tree-6df0.arabiribiaa.workers.dev"
PASSWORD = "ngochiton"

st.set_page_config(page_title="Smart Video Link Generator", layout="wide")

st.title("🚀 Smart Video Link Generator")
st.markdown("Generate native-style autoplay video links for X.")

# --- GENERATOR FORM ---
with st.container():
    st.subheader("Create New Link")
    col1, col2 = st.columns(2)
    
    with col1:
        title = st.text_input("Internal Title", placeholder="Campaign A")
        video_url = st.text_input("Direct MP4 Video URL", placeholder="https://site.com/video.mp4")
    
    with col2:
        dest_url = st.text_input("Destination URL (Affiliate)", placeholder="https://amzn.to/...")
        pass_input = st.text_input("Password", type="password")

    if st.button("Generate Link", use_container_width=True):
        if pass_input == PASSWORD:
            if video_url and dest_url:
                # We encode the URLs as parameters so the Worker knows what to show
                encoded_video = urllib.parse.quote(video_url)
                encoded_dest = urllib.parse.quote(dest_url)
                
                # Add a random version v= to bypass X's cache
                import time
                version = int(time.time())
                
                final_link = f"{WORKER_URL}/?vid={encoded_video}&dest={encoded_dest}&v={version}"
                
                st.success("✅ Link Generated Successfully!")
                st.code(final_link, language="text")
                st.info("Paste this link into your X post. Wait a few seconds for the video to appear.")
            else:
                st.error("Please fill in both Video and Destination URLs.")
        else:
            st.error("Incorrect Password.")

st.divider()
st.caption("Note: Ensure your video URL ends in .mp4 and is a direct link (not a landing page).")
