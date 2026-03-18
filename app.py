import streamlit as st
import urllib.parse

# 1. SETUP: Your specific Cloudflare Worker URL
# This is the "Bridge" that handles the Twitter/X bots
BASE_WORKER_URL = "https://floral-waterfall-f02a.arabiribiaa.workers.dev"
SECRET_PASS = "ngochiton"

st.set_page_config(page_title="Twitter Viral Poster", page_icon="🐦")
st.title("🐦 Twitter Viral Video Poster")

# Simple Authentication
password = st.sidebar.text_input("Access Password", type="password")

if password == SECRET_PASS:
    with st.form("viral_form"):
        video_url = st.text_input("1. Video URL (.mp4 direct link)", 
                                placeholder="Example: https://amplify.videotwimg.live/...")
        affiliate_link = st.text_input("2. Affiliate / Destination Link", 
                                     placeholder="Example: https://omg10.com/...")
        
        submit = st.form_submit_button("Generate Viral Link")

    if submit:
        if video_url and affiliate_link:
            # We encode the URLs so the Worker can read them correctly
            encoded_video = urllib.parse.quote(video_url, safe='')
            encoded_dest = urllib.parse.quote(affiliate_link, safe='')
            
            # The Final Link you will paste into Twitter/X
            # We add ?v= at the end to force X to refresh its memory (cache-buster)
            final_link = f"{BASE_WORKER_URL}/?vid={encoded_video}&dest={encoded_dest}&v={video_url[-5:]}"
            
            st.success("✅ Ready to Post!")
            st.code(final_link)
            
            st.info("""
            **How to Post:**
            1. Copy the link above.
            2. Paste it into X (Twitter).
            3. **WAIT 20 SECONDS** for the black video box to appear.
            4. Delete the blue link text.
            5. Hit **Post**.
            """)
        else:
            st.error("Please provide both the video and the destination link.")
else:
    st.warning("Please enter the password to access the tool.")
