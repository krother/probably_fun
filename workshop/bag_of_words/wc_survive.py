import wordcloud

text = open("survive.txt").read().lower()

cloud = wordcloud.WordCloud(
        max_words=40,
        scale=4,
        collocations=False,
        contour_color='steelblue',
        max_font_size=30
).generate(text)
im = cloud.to_image()
im.save("survive.png")
