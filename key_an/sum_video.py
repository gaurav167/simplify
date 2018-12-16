from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

import subprocess

path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
video_file = os.path.join(path, "../video/lecture10-360p.mp4")
start_times = [140, 176]
end_times = [149, 187]
out_file = os.path.join(path, "outfile.mp4")


