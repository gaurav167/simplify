import pysrt
import re, os
from sumy_example import summarise_doc

from moviepy.editor import VideoFileClip, TextClip, ImageClip, concatenate_videoclips
import sys
import requests
import json
from analysis import give_headings
import cv2


path = os.path.dirname(os.path.realpath(__file__))


def getDiction(subs):
	wordDictionary={}
	wordEndDictionary={}

	current_text=None
	current_time=-1
	for sub in subs:
		# remove all those font tags in each subtitle
		text=sub.text
		cleanr = re.compile('<.*?>')
		text = re.sub(cleanr, '', text)

		mytime=sub.start.hours*3600+sub.start.minutes*60+sub.start.seconds
		my_time_end=sub.end.hours*3600+sub.end.minutes*60+sub.end.seconds

		if(current_time==-1):
			current_time=mytime

		if("." in text):
			lines=text.split(".")
			# print(lines, len(lines))
			if current_text is not None:
				current_text=current_text+" "+lines[0]
			else:
				current_text=lines[0]
			
			current_text = current_text.replace('\n', ' ')
			wordDictionary[current_text.strip()+"."]=current_time
			wordEndDictionary[current_text.strip()+"."]=my_time_end

			lines.pop(0)
			# last sentence
			if(len(lines)==1 and lines[0]==''):
				current_time=-1
				current_text=None
				continue

			for index in range(0,len(lines)-1):
				line=lines[index]
				line = line.replace('\n', ' ')
				wordDictionary[line.strip()+"."]=mytime
				wordEndDictionary[line.strip()+"."]=my_time_end

			if(lines[len(lines)-1]==''):
				current_text=None
				current_time=-1
			else:
				current_text=lines[len(lines)-1]
				current_time=mytime

		else:
			if current_text is not None:
				current_text=current_text+" "+text
			else:
				current_text=text
	if current_time!=-1:
		current_text = current_text.replace('\n', ' ')
		wordDictionary[current_text.strip()+"."]=current_time
		wordEndDictionary[line.strip()+"."]=my_time_end

	return wordDictionary, wordEndDictionary




def create_summary(filename, regions):
	subclips = []
	input_video = VideoFileClip(filename)
	last_end = 0
	for (start, end) in regions:
	    subclip = input_video.subclip(start, end)
	    subclips.append(subclip)
	    last_end = end
	return concatenate_videoclips(subclips)


# out_file = os.path.join(path, "outfile.mp4")
# video_file = os.path.join(path, "nptel.mp4")
# filename=os.path.join(path, "nptel.srt")
def find_transcript(out_file, video_file, filename):
	transcriptfile=os.path.join(path, "transcript.txt")

	transcript=open(transcriptfile, "w")
	subs=pysrt.open(filename)

	wordDictionary, wordEndDictionary=getDiction(subs)

	for item in wordDictionary:
		# print(item, wordDictionary[item])
		transcript.write(item+"\n")

	transcript.close()
	print("Sentences counted: ", len(wordDictionary)) 
	chosen_sentences=summarise_doc(transcriptfile, len(wordDictionary)*2,len(wordDictionary)//5)
	regions = []
	for sentence in chosen_sentences:
		# print(sentence)
		if(sentence in wordDictionary):
			my_time=wordDictionary[sentence]
			my_time_end=wordEndDictionary[sentence]
			regions.append((my_time, my_time_end))
	summary = create_summary(video_file, regions)
	summary.to_videofile(
        out_file, 
        codec="libx264", 
        temp_audiofile="temp.m4a",
        remove_temp=True,
        audio_codec="aac",)






videos = [
	{
		"name": "speaker_name",
		#the paths can be whatever you want, but the containing
		#folders should already exist
		# "original" : "../nptel.mp4",
		"original": "../code/nptel.mp4",
		"frameSkipped": "video_frameskipped.mp4",
		"roid": "video_roid.mp4",
		"outputPath": "output/",
		#top left of Region Of Interest
		"x1": 0,
		"y1": 0,
		#bottom right of Region Of Interest
		"x2": 1920,
		"y2": 1080,
		"excludeBefore": 20 #will not consider anything before 20 secodns as a keyframe
	}
]


def processAll(videos):
	for video in videos:
		os.system("python preprocess.py --command shrink --source {0} --dest {1}".format(video["original"], video["frameSkipped"]))

		# os.system("python preprocess.py --command roi --source {0} --dest {1} --rect {2},{3},{4},{5}"
		# 	.format(video["frameSkipped"], video["roid"], video["x1"], video["y1"], video["x2"], video["y2"]))

		os.system("python scene_detection.py -s {0} -d {1} -n {2} -a {3}"
			.format(video["frameSkipped"], video["outputPath"], video["name"], video["excludeBefore"]))

		sys.stdout.write('.')
		sys.stdout.flush()



def is_present(word_string):
	if(word_string in my_map.keys()):
		return True
	else:
		return False

def get_toc():
	processAll(videos)
	#Make sure to set this to the output folder used in the video objects above
	#(the folder) above the one for individual speakers.
	outputPath = videos[0]['outputPath']
	os.system("python postprocess.py -s {0} -d {0}".format(outputPath, outputPath))

	headings = give_headings(os.path.join(path, 'output/images/full'))
	# print(headings)

	for root, dirs, files in os.walk(os.path.join(path, outputPath), topdown=False):
		for name in files:
			os.remove(os.path.join(root, name))
		for name in dirs:
			os.rmdir(os.path.join(root, name))
	os.rmdir(outputPath)
	os.remove('video_frameskipped.mp4')

	my_map={}

	transcript_file_name=os.path.join(path, "../code/transcript.txt")
	file=open(transcript_file_name, "r")

	for line in file:
		for word in line.split():
			my_map[word]=1

	file.close()


	cap = cv2.VideoCapture(videos[0]["original"])
	fps = cap.get(cv2.CAP_PROP_FPS)
	cap.release()

	# print(headings)
	ToC = {}
	for (key, val) in headings.items():
		# print(key, val)
		words = val.split(' ')
		cnt = len(words)
		# print(words)
		for word in words:
			# print(word)
			if is_present(word):
				# print(int(key)//fps, val)
				# ToC[int(key)//fps] = val
				cnt-=1
		if(cnt <= 3*len(words)//4):
			ToC[int(int(key)*1.85)] = val

	return ToC