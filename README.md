# Calliope Converter 
A small python program to convert music files into mp3 for someone looking to standardize an audio library. This is a simple, very hands-on converter. It will only search for files within its own folder one format at a time and replace them with an mp3 at 192k sampling bitrate. 

This is a personal project built to solve one of my own digital problems so I look forward if it can be some value for you as well. With some tinkering, the patterns can be applied to convert more formats and at diffrent qualities. 

---
## Dependencies


-This uses the libraries of [pydub](https://github.com/jiaaro/pydub) and [ffmpeg](https://github.com/FFmpeg/FFmpeg) to perform its tasks.

-[Tinytag](https://github.com/devsnd/tinytag) is used to keep the metadata on each conversion. 

-[Tqdm](https://github.com/devsnd/tinytag) is used to display a progress bar when performing conversions on each format. Purely for display, so you know its working!

---

## How to Use
As I stated this is a very hands-on apporach to converting your music library into mp3. 

-Move or Copy your audio files into the "project" folder with the converter.py program. 

-Activate the venv in the "environments" folder through cmd prompt or your CLI of choice

-In the "project" folder run converter.py and it will **replace** the music files that are alongside the program.

-Move your new audio files back into your music library.

---
### Notes

I found it difficult to get ffmpeg to work on my windows machine, it looks easier for Macs and Linux but for windows I followed [this process](https://www.youtube.com/watch?v=IECI72XEox0&t=1s) to get things going right. 

Tinytag had some minor issues getting accepted by pylance and loading their library. Focusing the python interpreter on the selected enviornment has resolved the issue which is a strat I picked up [here](https://www.youtube.com/watch?v=5ud9Y2uB4PY&t=1s). The album artwork is not transferred in conversion but important the essential metadata makes it through thanks to Tinytag.

