import streamlit as st
import urllib.parse

# Config
BASE_WORKER_URL = "https://floral-waterfall-f02a.arabiribiaa.workers.dev"
SECRET_PASS = "ngochiton"

st.set_page_config(page_title="Twitter Viral Poster", page_icon="🐦")
st.title("🐦 Twitter Viral Video Poster")

# Sidebar Auth
password = st.sidebar.text_input("Access Password", type="password")

if password == SECRET_PASS:
    with st.form("viral_form"):
        st.subheader("Generate 'Amplify' Style Link")
        video_url = st.text_input("1. Video URL (.mp4 direct link)")
        affiliate_link = st.text_input("2. Affiliate / Destination Link")
        
        submit = st.form_submit_button("Generate Link")

    if submit:
        if video_url and affiliate_link:
            # Encode URLs so they don't break the main link
            encoded_video = urllib.parse.quote(video_url, safe='')
            encoded_dest = urllib.parse.quote(affiliate_link, safe='')
            
            # Use the last part of the video URL as a cache-buster
            v_tag = video_url[-6:] if len(video_url) > 6 else "101"
            
            # The Final URL to paste on X
            final_link = f"{BASE_WORKER_URL}/?vid={encoded_video}&dest={encoded_dest}&v={v_tag}"
            
            st.success("✅ Link Generated!")
            st.code(final_link)
            
            st.warning("""
            **Posting Steps:**
            1. Paste link into X.
            2. **WAIT 20 SECONDS** for the black video box to appear.
            3. Delete the blue link text.
            4. Post.
            """)
        else:
            st.error("Please fill in both fields.")
else:
    st.info("Enter password to unlock.")
