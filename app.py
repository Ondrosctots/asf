import streamlit as st
import urllib.parse

# Authentic credentials from your system
SECRET_PASS = "ngochiton"
# Your Cloudflare Worker or Blogger domain
BASE_DEPLOY_URL = "https://your-worker-or-blog.com" 

st.set_page_config(page_title="Twitter Viral Poster", page_icon="🐦")

st.title("🐦 Twitter Viral Video Poster")
st.markdown("Generate full-width 'Amplify' style video posts without summary boxes.")

# Simple Authentication
password = st.sidebar.text_input("Access Password", type="password")

if password == SECRET_PASS:
    with st.form("generator_form"):
        video_url = st.text_input("1. Video URL (.mp4 direct link)", 
                                placeholder="https://amplify.videotwimg.live/...")
        affiliate_link = st.text_input("2. Affiliate / Destination Link", 
                                     placeholder="https://omg10.com/...")
        
        submit = st.form_submit_button("Generate Posting Link")

    if submit:
        if video_url and affiliate_link:
            # Create a 'Cache Buster' to ensure X sees a fresh version
            cache_buster = urllib.parse.quote(video_url[-8:])
            final_link = f"{BASE_DEPLOY_URL}/?vid={video_url}&dest={affiliate_link}&v={cache_buster}"
            
            st.success("✅ Ready to Post!")
            st.code(final_link)
            
            st.info("""
            **How to Post:**
            1. Copy the link above.
            2. Paste it into X (Twitter).
            3. **Wait 20 seconds** for the large black video box to appear.
            4. Delete the link text from the post box.
            5. Hit **Post**.
            """)
        else:
            st.error("Both links are required.")
else:
    st.warning("Enter the password to unlock the tool.")
