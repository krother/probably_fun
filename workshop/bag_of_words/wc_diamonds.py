
import wordcloud

text = open("diamonds.txt").read().lower()

cloud = wordcloud.WordCloud(
        max_words=40,
        scale=4,
        collocations=False,
        stopwords={"none"},
        contour_color='steelblue',
        max_font_size=80,
).generate(text)
im = cloud.to_image()
im.save("diamonds.png")
