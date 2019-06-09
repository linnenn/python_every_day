#! /usr/local/bin/python3
#coding=utf-8

from moviepy.editor import *
from moviepy.video.tools.credits import credits1
import os,math
'''
    视频转换分辨率
'''
def reSizeVideo(file):
    video = VideoFileClip(file)
    s_d = 0
    #视频长度
    v_d = video.duration
    v_w, v_h = video.size #视频长宽
    h__w = v_h / v_w
    if v_h == v_w:
        #正方形的剪成规定尺寸
        video = video.subclip(s_d, v_d + s_d).resize((1376, 768))
        video = video.crop(y_center=640, height=720)
    elif h__w == 0.5625:
        video = video.subclip(s_d, v_d + s_d).resize((1280, 720))
    elif v_h / v_w < 0.5625:
        #不符合比例的，先resize，然后再crop裁剪
        video = video.subclip(s_d, v_d + s_d).resize(height=720)
        video = video.crop(x1=0,width=1280, y1=0,height=720)
    elif v_h / v_w > 0.5625:
        video = video.subclip(s_d, v_d + s_d).resize(width=1280)
        video = video.crop(y_center=video.size[1]/2, height=720)
    return video

'''
    剪切视频，并完成视频剪切
    videoPath 视频目录
    start 截取开始时间
    end 截取结束时间
    pre_name 被截取前缀名字，用于文件命名
'''

def cutVideo(videoPath,start,end,pre_name):
    # if end is None:
    #    video = VideoFileClip(videoPath) 
    #    end = video.duration
    # video = VideoFileClip(videoPath).subclip(start,end).resize((1920, 1080))
    video = reSizeVideo(reSizeVideo)
    global path
    video.write_videofile(path + pre_name + str(start) + str(end) + ".mp4")

'''
    合并视频
    filename 合成的视频名字
    *video 合成的视频列表，需要保证顺序
'''
def concrate(filename,*videos):
    video_clip = []
    for video in videos:
        video_clip.append(reSizeVideo(video))
    handler = concatenate_videoclips(video_clip)
    global path
    handler.write_videofile(path + filename + ".mp4")

if  __name__ == "__main__":
    path = os.getcwd() + '/'
    #传参方式，暂时不用，需要的时候去调整
    if len(sys.argv) >= 5:
        filename = sys.argv[1]
        video = sys.argv[1:]

    video1 = path + 'b/aa19.mp4'
    video2 = path + 'b/con_1.mp4'
    video3 = path + 'b/aa1124.mp4'
    concrate('new_concate_1',video1,video2,video3)