import streamlit as st
import urllib.parse
import time

# 🔧 CONFIG
WORKER_URL = "https://morning-tree-6df0.arabiribiaa.workers.dev"
PASSWORD = "ngochiton"

st.set_page_config(page_title="X Video Generator", layout="centered")

st.title("🎬 X Native Video Link Generator")

with st.form("generator"):
    video_link = st.text_input("🎥 Direct MP4 URL", placeholder="https://example.com/video.mp4")
    target_link = st.text_input("🔗 Destination URL", placeholder="https://offer.com")
    password = st.text_input("🔐 Password", type="password")

    submit = st.form_submit_button("Generate Link")

if submit:
    if password != PASSWORD:
        st.error("❌ Wrong password")
    elif not video_link or not target_link:
        st.error("❌ Fill all fields")
    else:
        # 🔥 FIXED ENCODING
        enc_vid = urllib.parse.quote(video_link, safe='')
        enc_dest = urllib.parse.quote(target_link, safe='')

        # 🔥 CACHE BUSTER (VERY IMPORTANT)
        v = int(time.time())

        final_url = f"{WORKER_URL}/?vid={enc_vid}&dest={enc_dest}&v={v}"

        st.success("✅ Link Generated!")
        st.code(final_url)

        st.info("👉 Paste into X (Twitter) and wait ~5–10 seconds for preview")
