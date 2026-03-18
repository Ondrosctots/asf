import streamlit as st
import urllib.parse
import time

# --- CONFIG ---
WORKER_URL = "https://morning-tree-6df0.arabiribiaa.workers.dev"
PASSWORD = "ngochiton"

st.set_page_config(page_title="X Video Gen", layout="centered")

st.title("🎬 X Native Video Link Generator")

with st.form("link_gen"):
    video_link = st.text_input("Direct MP4 URL", placeholder="https://example.com/video.mp4")
    target_link = st.text_input("Affiliate/Destination URL", placeholder="https://target.com/page")
    pass_input = st.text_input("Password", type="password")
    
    submit = st.form_submit_button("Generate Link")

if submit:
    if pass_input == PASSWORD:
        if video_link and target_link:
            # Encoding prevents the "broken link" issue seen in your screenshots
            enc_vid = urllib.parse.quote(video_link)
            enc_dest = urllib.parse.quote(target_link)
            
            # Use a timestamp as a version to kill X's cache
            v_token = int(time.time())
            
            final_url = f"{WORKER_URL}/?vid={enc_vid}&dest={enc_dest}&v={v_token}"
            
            st.success("✅ Link Generated!")
            st.code(final_url)
            st.info("Paste this on X and wait 5 seconds for the preview to load.")
        else:
            st.error("Please fill in all fields.")
    else:
        st.error("Invalid Password.")
