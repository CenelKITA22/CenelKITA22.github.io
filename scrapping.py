# Import Package requests and beautifulsoup
import requests
from bs4 import BeautifulSoup

# Request from website 
page = requests.get("https://www.republika.co.id/")

# Extract content to object
obj = BeautifulSoup(page.text,"html.parser")


# FILE
# # Extract Data from div class="bungkus_txt_headline"
# headline = obj.find_all("div",class_="bungkus_txt_headline")
# f=open("D:\KAZUNO\Web\Project\Project-BETHREE\headline.txt","w")
# # print("===== Menampilkan Data Scrapping =====")
# # print()
# for title in headline:
#     single = title.find("h2")
#     cat = title.find("h1")
#     high = title.find("p")
#     f.write(single.text)
#     f.write(cat.text)
#     f.write(high.text)
#     f.write("\n")
# #     print("Kategori : ",cat.text)
# #     print("Judul : ",single.text)
# #     print("Highlight : ",high.text)
# #     print()
# # print("======================================")
# f.close()

# JSON

import json

data = []

f=open("D:\KAZUNO\Python\modul python\scrapping\headline.json","w")
for headline in obj.find_all("div",class_="bungkus_txt_headline_center"):
    data.append({"judul":headline.find('h2').text})

jdump=json.dumps(data)
f.writelines(jdump)
f.close()
