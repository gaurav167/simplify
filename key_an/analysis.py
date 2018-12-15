import os
import requests
import json


# OCR-Vid
# ac4ffd7480c8488db2447123d8f78904
# ba5c362bfa91428aad7a5d4cc8c881d5

def give_headings(dirpath):

	headers = {
	    'Content-Type': 'application/octet-stream',
	    'Ocp-Apim-Subscription-Key': 'ac4ffd7480c8488db2447123d8f78904',
	}
	body = {
		'url' : 'speaker_name-0163',
	}
	params = {
		'language' : 'en',
		'detectOrientation ': 'true',
	}

	headings = {}

	for _, _, files in os.walk(dirpath):
		# print(file)
		for file in files:
			img = os.path.join(dirpath, file)
			image = open(img, "rb").read()
			r = requests.post("https://southeastasia.api.cognitive.microsoft.com/vision/v2.0/ocr", headers=headers, params=params, data=image)
			try:
				words = json.loads(r.text)['regions']
				if len(words) > 0:
					words = words[0]['lines'][0]['words']
					w = []
					for word in words:
						w.append(word['text'])

					text = ' '.join(w)
					headings[file.split('-')[-1].split('.')[0]] = text
				else:
					pass
			except:
				pass

	return headings



# path = os.path.dirname(os.path.realpath(__file__))
# print(give_headings(os.path.join(path, "filmstrip/output/full")))