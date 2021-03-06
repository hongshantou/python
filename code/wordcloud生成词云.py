#coding:utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
from PIL import Image

#读入背景图片
abel_mask = np.array(Image.open("G:\\test\\text.jpg"))

#读取要生成词云的文件
text_from_file_with_apath = open('G:\\test\\text2.txt').read()

#通过jieba分词进行分词并通过空格分隔
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
#my_wordcloud = WordCloud().generate(wl_space_split) 默认构造函数
my_wordcloud = WordCloud(
            background_color='white',    # 设置背景颜色
            mask = abel_mask,        # 设置背景图片
            max_words = 200,            # 设置最大现实的字数
            stopwords = STOPWORDS,        # 设置停用词
            font_path = 'G:\test\hbyy.ttf',# 设置字体格式，如不设置显示不了中文
            max_font_size = 50,            # 设置字体最大值
            random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
                scale=.5
                ).generate(wl_space_split)

# 根据图片生成词云颜色
image_colors = ImageColorGenerator(abel_mask)
#my_wordcloud.recolor(color_func=image_colors)

# 以下代码显示图片
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()