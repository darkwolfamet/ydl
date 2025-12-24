# ydl
Ydl .A simple Python-based command-line tool that lets you download YouTube videos, audio, or extract audio from videos directly to your Linux machine. Users can choose the output folder, file naming, and download format, making it an easy-to-use terminal downloader powered by yt-dlp.


Features

Download videos in best quality.

.Extract audio as MP3.

.Custom file naming and output folder.

.Simple, interactive terminal interface.

.Works entirely in the terminal — no GUI needed.


Installation

Clone the repository:

git clone https://github.com/<your-username>/ydl.git
cd ydl


Install dependencies:

pip install -r requirements.txt

Usage

Run the tool:

python ydl.py


Follow the prompts:

Enter the URL of the YouTube video.

Choose the format: Video, Audio, or Extract audio.

Select the output folder.

Choose default or custom file naming.

Wait for the download to complete.

Examples

Download a video with default naming to a custom folder:

python ydl.py
# URL: https://www.youtube.com/watch?v=abc123
# Format: Video
# Output folder: /home/user/Downloads
# Naming: default


Extract audio from a music video:

python ydl.py
# URL: https://www.youtube.com/watch?v=xyz789
# Format: Extract
# Output folder: /home/user/Music
# Naming: MyFavoriteSong

Requirements

Python 3.7+

yt-dlp

Install dependencies with:

pip install -r requirements.txt

Contributing

Fork the repository.

Make changes in your fork.

Submit a pull request.

All contributions are welcome, but you must follow coding standards and test your changes.

License

This project is licensed under the MIT License – see the LICENSE
 file for details.

If you want, I can also suggest a visual repo structure with folders and files so you can organize Ydl nicely on GitHub. This makes it easier for others to navigate and use.

Do you want me to do that next?
