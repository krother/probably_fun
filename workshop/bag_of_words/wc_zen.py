import re
import wordcloud

text = ' '.join(set([w for w in re.findall(r"[a-z]+", open("zen.txt").read().lower())]))

cloud = wordcloud.WordCloud(
        max_words=50,
        scale=4,
        collocations=False,
        contour_color='steelblue',
        prefer_horizontal=1,
        min_font_size=16,
        max_font_size=16,
).generate(text)
im = cloud.to_image()
im.save("zen.png")
