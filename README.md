# Simplify

## Introduction
Massive Open Online Courses (MOOCs) and other online learning resources have added many good quality educational videos on the Internet. The number, already in tens of thousands, is increasing by the day. Tools for search and recommendation are therefore indispensable for finding relevant content online. 

## Problem
* The overwhelming number of videos presents challenges of finding the most appropriate video and consuming the content effectively.
* Lecture recordings are often long videos with duration of upto several hours. Learners may be interested in only certain topics in the video or may need to review specific sections within the video. But since these videos are generally quite long they are bound to see the whole video despite of their needs.

## Solution
* We attempt to provide an integrated platform , "**Simplify**" , through which we summarize and extract the important concepts of the video. 
* We further present the user with Table of Contents and Textual Summary of the specified video to enable the user to quickly perceive the content of a video without having to watch it.

## Features
These are the features that we offer to serve to the users as a part of our integrated platform.
* Transcript Summarization
* Video Summarization
* Table of Contents
* Video Page

## Process
**Transcript Summarization** : We have applied Latent Semantic Analysis [LSA](https://en.wikipedia.org/wiki/Latent_semantic_analysis) for the purpose of text summarization which inturn extracts the important information from the transcripts and prepare a crisp and short summary of the whole video.
**Key Frame Detection** : We select frames which have minimum overlaps, thus helping us find the frames with maximum information. These keyframes are further used in the preparation of video slides and Table of Content.
**Video Slides** :  We send the selected key frames to Azure OCR and get text for each of these frames. We select the best frames from this set and prepare a presentation for the same.
**Table of Content** : Table of content for a video can be thought of as an index for the video. The text obtained from the keyframes is further analysed on various metrics such as font_size, boldness etc. to extract the essential headings for each group of keyframes. 
These are then mapped to the video and serve as an index for quick navigation.

<br><br>
<img src = "https://user-images.githubusercontent.com/22594194/50050319-3700f600-011d-11e9-8c2e-f049e884df93.png"/>




