import os

def post_to_socials(video_path):
    print(f"🚀 [SOCIAL] Megosztás indítása: {video_path}")
    
    # YouTube feltöltés szimuláció a tokennel
    yt_token = os.getenv('YOUTUBE_API_TOKEN')
    if yt_token:
        print("✅ YouTube Shorts: Feltöltés sikeres (API Token használatával)")
    
    # TikTok feltöltés szimuláció
    tt_token = os.getenv('TIKTOK_ACCESS_TOKEN')
    if tt_token:
        print("✅ TikTok: Videó publikálva")

    # Instagram Reels szimuláció
    ig_token = os.getenv('INSTAGRAM_GRAPH_TOKEN')
    if ig_token:
        print("✅ Instagram Reels: Posztolva a profilra")

if __name__ == "__main__":
    post_to_socials("titanium_promo.mp4")
