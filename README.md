# Motivational Video Automator

This project automatically generates short, motivational videos (like YouTube Shorts or Instagram Reels) by combining a random quote with a random background video clip and background music.

## How it Works

The script, `daily_creator.py`, performs the following steps:

1.  **Picks a Random Quote:** It reads a list of quotes from `quotes.csv` and selects one at random.
2.  **Picks a Random Video Clip:** It selects a random video clip from the `clips/` directory.
3.  **Adds Background Music:** It picks a random music file from the `music/` directory, adjusts the volume, and loops or trims it to match the video duration.
4.  **Creates a Text Overlay:** It creates a text overlay of the selected quote with a specified font, size, and color.
5.  **Combines and Renders:** It combines the video clip and text overlay into a final video.
6.  **Saves the Video:** The final video is saved in the `output/` directory with a filename based on the current date (e.g., `motivational_short_2025-07-30.mp4`).

## Project Structure

```
.
├── clips/
│   └── (your video clips)
├── music/
│   └── (your music files)
├── output/
│   └── (generated videos)
├── quotes.csv
├── daily_creator.py
└── requirements.txt
```

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Add your content:**
    *   Add your background video clips (e.g., `.mp4`, `.mov`) to the `clips/` directory.
    *   Add your background music files (e.g., `.mp3`) to the `music/` directory.
    *   Add your quotes to the `quotes.csv` file, with each quote on a new line.

4.  **Run the script:**
    ```bash
    python daily_creator.py
    ```

    The script will render the video and save it in the `output/` directory.

## Configuration

You can customize the video settings by modifying the variables at the top of `daily_creator.py`:

*   `VIDEO_DURATION`: The duration of the video in seconds.
*   `RESOLUTION`: The video resolution (e.g., `(1080, 1920)` for vertical video).
*   `FONT`: The font to use for the text overlay. You can specify the path to a `.ttf` file or use `None` for the default font.
*   `FONT_SIZE`: The font size of the text.
*   `TEXT_COLOR`: The color of the text.

## Sample Quote Format

The `quotes.csv` file should follow this format:

```csv
quote
"Success is not final, failure is not fatal: it is the courage to continue that counts."
"Believe you can and you're halfway there."
"Your limitation—it's only your imagination."
"Push yourself, because no one else is going to do it for you."
"Great things never come from comfort zones."
```

## Supported File Formats

### Video Clips (`clips/` directory)
- `.mp4`
- `.mov`
- `.avi`
- `.mkv`
- `.webp` (static images)
- `.jpg`, `.jpeg`, `.png` (static images)

### Audio Files (`music/` directory)
- `.mp3`
- `.wav`
- `.m4a`
- `.aac`

## Dependencies

This project uses the following Python libraries:

*   **`moviepy`** - Video editing and processing
*   **`pandas`** - Data manipulation for reading CSV files
*   **`Pillow`** - Image processing
*   **`numpy`** - Numerical operations
*   **`imageio`** - Image I/O operations
*   **`imageio-ffmpeg`** - FFmpeg integration for video processing

You can install them using the `requirements.txt` file as described above.

## Troubleshooting

### Common Issues

1. **Font Error**: If you get a font-related error, make sure to either:
   - Set `FONT = None` to use the default font
   - Or provide a valid path to a `.ttf` font file

2. **Missing FFmpeg**: MoviePy requires FFmpeg for video processing. It's usually installed automatically with `imageio-ffmpeg`, but if you encounter issues:
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install ffmpeg
   
   # macOS
   brew install ffmpeg
   
   # Windows
   # Download from https://ffmpeg.org/download.html
   ```

3. **No clips/music found**: Make sure you have files in both the `clips/` and `music/` directories before running the script.

## Customization Ideas

- **Themes**: Organize clips by themes (motivation, success, nature) and select based on quote category
- **Branding**: Add your logo or watermark to the videos
- **Transitions**: Add fade-in/fade-out effects for text
- **Multiple Text Styles**: Use different fonts or colors based on quote sentiment
- **Scheduling**: Set up a cron job to automatically generate videos daily

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source. Please make sure you have the rights to use any media files (clips, music) you add to the project.

