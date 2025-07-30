import random
import pandas as pd
from moviepy import *
import os
from datetime import datetime

# =============== CONFIG ===============
QUOTES_CSV = "quotes.csv"
CLIPS_DIR = "clips/"
MUSIC_DIR = "music/"
OUTPUT_DIR = "output/"

VIDEO_DURATION = 15  # seconds for shorts
RESOLUTION = (1080, 1920)  # 9:16 vertical
FONT = None  # Use default font
FONT_SIZE = 70
TEXT_COLOR = "white"
# ======================================

# Make sure output folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1) Pick a random quote
df = pd.read_csv(QUOTES_CSV)
quote = random.choice(df['quote'])

# 2) Pick a random image clip
image_files = os.listdir(CLIPS_DIR)
image_file = random.choice(image_files)
image_clip = ImageClip(os.path.join(CLIPS_DIR, image_file)).with_duration(VIDEO_DURATION)
image_clip = image_clip.resized(new_size=RESOLUTION)

# 3) Optional: add background music
music_files = os.listdir(MUSIC_DIR)
if music_files:
    music_file = random.choice(music_files)
    music = AudioFileClip(os.path.join(MUSIC_DIR, music_file)).with_volume_scaled(0.1)
    if music.duration > VIDEO_DURATION:
        music = music.subclipped(0, VIDEO_DURATION)
    else:
        # For looping, we'll use a simple approach - repeat the audio
        import numpy as np
        loops_needed = int(np.ceil(VIDEO_DURATION / music.duration))
        music_clips = [music] * loops_needed
        music = concatenate_audioclips(music_clips).subclipped(0, VIDEO_DURATION)
    image_clip = image_clip.with_audio(music)

# 4) Add text overlay
text_clip = TextClip(
    text=quote,
    font_size=FONT_SIZE,
    font=FONT,
    color=TEXT_COLOR,
    size=(900, None),
    method='caption'
).with_position(('center', 'center')).with_duration(VIDEO_DURATION)

# 5) Combine image + text
final = CompositeVideoClip([image_clip, text_clip])

# 6) Save to output folder with today's date
today = datetime.now().strftime("%Y-%m-%d")
output_file = os.path.join(OUTPUT_DIR, f"motivational_short_{today}.mp4")

print(f"Rendering video... This may take a minute.")
final.write_videofile(output_file, fps=30, codec="libx264")

print(f"✅ Done! Saved to: {output_file}")
