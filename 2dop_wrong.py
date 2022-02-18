import requests

link = "https://pixabay.com/api/?key=25759553-750fe90e5dc1e5aeba4c4717d&q="

def imagetter():

    imgtype = str(input("IMG_TYPE(all, photo, illustration, vector) - "))

    imgcat = str(input("IMG_CATEGORY\n"
          "backgrounds, fashion, nature, science, education, feelings, health, people, religion,\n"
          "places, animals, industry, computer, food, sports, transportation, travel, buildings, business, music - "))

    imgcolor = str(input("IMG_COLOR\n"
          "grayscale, transparent, red, orange, yellow, green, turquoise,\n"
                         "blue, lilac, pink, white, gray, black, brown - "))

    flink = link + imgcat + "+" + imgcolor + "&image_type=" + imgtype + "per_page=7"

    response = requests.get(flink)

    data = response.json()

    useless1, useless2, useful = data.values()
    useless1 = None
    useless2 = None

    for k in range(1, 6):
        piclink = useful[k].get("largeImageURL")
        picdown = requests.get(piclink)
        open("pic"+str(k)+".jpg", "wb").write(picdown.content)

imagetter()
