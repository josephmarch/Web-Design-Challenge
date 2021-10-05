import pandas as pd
df = pd.read_csv("Resources/cities.csv", index_col=0)
html = df.to_html()
text_file = open("Resources/cities.html", "w")
text_file.write(html)
text_file.close()