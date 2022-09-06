import os
import pydub
import glob
from tqdm import tqdm
from time import sleep
from tinytag import TinyTag

# converts wave files in the folder
wav_files = glob.glob('./*.wav')

print("WAV Conversion Start")
for wav_file in tqdm(wav_files):
    sleep(0.01)
    w_tag = TinyTag.get(wav_file)
    mp3_file = os.path.splitext(wav_file)[0] + '.mp3'
    sound = pydub.AudioSegment.from_wav(wav_file)
    sound.export(mp3_file, 
        format="mp3",
        bitrate="192k",
        tags={
            "album": w_tag.album,
            "artist": w_tag.artist,
            "album_artist": w_tag.albumartist,
            "title": w_tag.title,
            "track": w_tag.track,
            "genre": w_tag.genre
        })
    os.remove(wav_file)
print("WAV Conversion Completed")



# reduces bitrate to a moderate level for mp3
high_mp3 = glob.glob('./*.mp3')

print("Mp3 Bitrate Adjustment Start")
for mp3_tune in tqdm(high_mp3):
    sleep(0.01)
    tag = TinyTag.get(mp3_tune)
    sound = pydub.AudioSegment.from_file(mp3_tune, format="mp3")
    # os.remove(mp3_tune)
    sound.export(mp3_tune, 
        format="mp3", 
        bitrate="192k",
        tags={
            "album": tag.album,
            "artist": tag.artist,
            "album_artist": tag.albumartist,
            "title": tag.title,
            "track": tag.track,
            "genre": tag.genre
        })
print("Mp3 Bitrate Adjusted")


# converts m4a files in the folder
m4a_files = glob.glob('./*.m4a')

print("Media4 Conversions Start")
for m4a_file in tqdm(m4a_files):
    sleep(0.01)
    tag = TinyTag.get(m4a_file)
    mp3_file = os.path.splitext(m4a_file)[0] + '.mp3'
    sound = pydub.AudioSegment.from_file(m4a_file, format="m4a")
    sound.export(mp3_file, 
        format="mp3", 
        bitrate="192k",
        tags={
            "album": tag.album,
            "artist": tag.artist,
            "album_artist": tag.albumartist,
            "title": tag.title,
            "track": tag.track,
            "genre": tag.genre
        })
    os.remove(m4a_file)
print("Media4 Conversion Completed")

