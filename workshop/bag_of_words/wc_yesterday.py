
import wordcloud

text = open("yesterday.txt").read().lower()

cloud = wordcloud.WordCloud(
        max_words=20,
        scale=4,
        collocations=False,
        contour_color='steelblue',
        max_font_size=35
).generate(text)
im = cloud.to_image()
im.save("yesterday.png")
