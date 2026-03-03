import requests

# url = "https://www.ukr.net/"
#
# response = requests.get(url)
# # print(response.content)
# print(response.text)
# with open("ukr.html", mode="w", encoding="utf-8") as file:
#     file.write(response.text)


# url = "https://img.ukr.bio/data/articles/av/9916.jpg"
# response = requests.get(url)
# content = response.content
# with open("spring.jpg", mode="bw") as file:
#     file.write(content)

# with open("spring.jpg", mode="br") as file, open("spring2.jpg", mode="bw") as file2:
#     content = file.read()
#     file2.write(content + b"hello")

with open("spring2.jpg", mode="br") as file2:
    content = file2.read()
    print(content)
