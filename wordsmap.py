# 生成词图
from scipy.misc import imread
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt
from os import path
 
cloud = WordCloud(
        #设置字体，不指定就会出现乱码，文件名不支持中文
        font_path="C:/simfang.ttf", 
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色，默认为黑，可根据需要自定义为颜色
        background_color='black', 
        #词云形状，
        #mask=color_mask,
        #允许最大词汇
        max_words=400,
        #最大号字体，如果不指定则为图像高度
        max_font_size=100,
        #画布宽度和高度，如果设置了msak则不会生效
        width=1200,
        height = 800,
        margin = 2,
        #词语水平摆放的频率，默认为0.9.即竖直摆放的频率为0.1
        prefer_horizontal = 0.8
    )
result = position_data.sum().sort_values(ascending=False)
_labels = [row for row in result.index]
_frequency = [row for row in result.values]
_data = { _labels[index]:_frequency[index] for index in range(len(_labels))}
wc = cloud.generate_from_frequencies(_data)
 
wc.to_file("cloud.jpg") #保存图片
#显示词云图片
plt.imshow(wc)
#不现实坐标轴
plt.axis('off')
plt
