#! /usr/local/bin/python3
#coding=utf-8

from moviepy.editor import *
from moviepy.video.tools.credits import credits1


# # 加载山背景的clip，截取，变慢，画面变暗
bgClip = (VideoFileClip('/Users/yanglei/Desktop/b/a.mp4', audio=False)
        .subclip(2, 5)
        .speedx(0.4)
        .fx(vfx.colorx, 0.7))

screensize = (720, 460)
txtClip1 = TextClip('nihaoya1',size=screensize, color='white', font="Amiri-Bold",
                   kerning=5, fontsize=100)

txtClip2 = TextClip('womenzhengshikaishi', color='white', font="Amiri-Bold",
                   kerning=5, fontsize=100)

txtClip3 = TextClip('fdfdfdfdfdfdf', color='white', font="Amiri-Bold",
                   kerning=5, fontsize=100)

txtClip4 = TextClip('zzzzzz', color='white', font="Amiri-Bold",
                   kerning=5, fontsize=100)


scrolling_credits1 = txtClip1.set_pos(lambda t: ('center', -50 * t)).set_duration(5)
scrolling_credits1 = txtClip1.set_position(lambda t: ('center', -50 * t)).set_duration(5)




b1CompositeVideoClip = CompositeVideoClip([scrolling_credits1])


cur_pos = 0
last_min = 0
def movef(f_time):
    if_time = int(f_time)
    print (">>>>>>>>>%d" % f_time)
    # "the length of (%s) is %d" % ('runoob', len('runoob')
    global cur_pos
    global last_min

    if if_time == 2 or if_time == 4:
        cur_pos = cur_pos
    else:
        if last_min == if_time:
            cur_pos = cur_pos
        else:
            cur_pos = -100 + cur_pos

            last_min = if_time


#     return 0, cur_pos


scrolling_credits1 = (
    txtClip1.set_duration(8).set_position(movef)
)

scrolling_credits1s = (
    txtClip1.set_position(lambda t: (0, -50 * t)).set_duration(3)
    )

b1CompositeVideoClip = CompositeVideoClip([scrolling_credits1,scrolling_credits1s])
b1CompositeVideoClip = CompositeVideoClip([scrolling_credits1])

# 让字幕以10像素每秒的速度滚动起来
final = CompositeVideoClip([bgClip,
                            scrolling_credits1.set_pos((300,300)).set_start(0),
                            b1CompositeVideoClip.set_pos((300,300)),
                            ])

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


# final.write_videofile('a21.mp4', fps=25)
video1 = reSizeVideo('./b/aa151080*720.mp4')
# video1.write_videofile('./wang/1_re.mp4')

video2 = reSizeVideo('./b/con_2.mp4')
# video2.write_videofile('./wang/2_re.mp4')

video3 = reSizeVideo('./b/bb191080*720..mp4')
# video3.write_videofile('./wang/3_re.mp4')

# video4 = reSizeVideo('./b/a.mp4')
# video4.write_videofile('./wang/a_re.mp4')
handler = concatenate_videoclips([video1,video2,video3])
handler.write_videofile('./b/con_jj.mp4')

# #视频，截取合成
# #素材1，长度8秒，截取6秒


#视频合成,1秒
# vhandler_a1 = VideoFileClip('a07.mp4')
# vhandler_a2 = VideoFileClip('a_con.mp4')
# vhandler_a3 = VideoFileClip('b18.mp4')
# video1 = concatenate_videoclips([vhandler_a1,vhandler_a2,vhandler_a3],method='compose')
# video1.write_videofile("a_new_1.mp4", fps=25)