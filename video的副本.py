from moviepy.editor import *
local = '/Users/yanglei/Desktop/a.mp4'
clip = VideoFileClip(local).subclip(5,15)
txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')
txt_clip = txt_clip.set_pos('center').set_duration(10)
video = CompositeVideoClip([clip, txt_clip])
video.write_videofile("myHolidays_new.mp4")
