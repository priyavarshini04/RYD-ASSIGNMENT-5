from bs4 import BeautifulSoupas soup
from urllib.request

# Request from the webpage
myurl = "https://www.indiabix.com/current-affairs/state/"


uClient  = uReq(myurl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, features="html.parser")

# print(soup.prettify(containers[0]))

# This variable held all html of webpage
containers = page_soup.find_all("div",{"class": "bix-div-container"})
# container = containers[0]
# # print(soup.prettify(container))
#
# question = container.find_all("div",{"class": "bix-td-qtxt"})
# print(question[0].text)
#
# options = container.find_all("div",{"class": "bix-tbl-options"})
# print(options[0].text)
# answer = container.find_all("div",{"class": "jq-hdnak mx-bold"})
# print(answer[0].text)
#
# #
# # print(len(containers))
# print(container.div.img["alt"])

# Creating CSV File that will store all data
filename = "product1.csv"
f = open(filename,"w")

headers = "block,question,options,answer\n"
f.write(headers)

for container in containers:
    block_name = container.div.img["alt"]

    question_container = container.find_all("div", {"class": "bix-td-qtxt"})
    question = question_container[0].text.strip()

    options_container = container.find_all("div",{"class":"bix-tbl-options"})
    options = options_container[0].text

# print("block:"+product_name)
    # print("question:"+question)
    # print("options:"+ str(options))
    # print("answer:"+ str(answer))




f.close()
