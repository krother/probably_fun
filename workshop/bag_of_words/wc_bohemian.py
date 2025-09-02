
import wordcloud

text = "galileo"

cloud = wordcloud.WordCloud(
        max_words=20,
        scale=4,
        collocations=False,
        contour_color='steelblue',
).generate(text)
im = cloud.to_image()
im.save("yesterday.png")
