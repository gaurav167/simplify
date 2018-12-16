from filmstrip import find_transcript , get_toc
import os 


def simplify_video(video_path , srt_path , temp_dir , output_dir) : 

    # Generate Transcript from File
    f_name = os.path.split(srt_path)[1].split('.')[0]
    out_file = os.path.join(output_dir, "output_" + f_name+".mp4")
    # srt_path = os.path.join(path, srt_path)
    find_transcript(video_path , srt_path , out_file , output_dir)
    
    video = {
		"name": "speaker_name",
		"original": video_path,
		"frameSkipped": os.path.join(temp_dir, "video_frameskipped.mp4") ,
		# "roid": "video_roid.mp4",
		"outputPath": temp_dir,
		#top left of Region Of Interest
		"x1": 0,
		"y1": 0,
		#bottom right of Region Of Interest
		"x2": 1920,
		"y2": 1080,
		"excludeBefore": 20 #will not consider anything before 20 secodns as a keyframe
	}

    headings = get_toc(video , output_dir, f_name)
    print(headings)




if __name__ == "__main__" :
    simplify_video('dataset/nptel.mp4' , 'dataset/nptel.srt' ,'temp', 'output')