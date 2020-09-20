import requests
from bs4 import BeautifulSoup
import math
import matplotlib.pyplot as plt

def main():
    URL = 'http://web.archive.org/web/20050923194412/http://www.chara.gsu.edu/RECONS/TOP100.htm'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    text = (soup.get_text())
    a = text.split('\n')
    raw_data = []
    list_stars = []
    dict_stars = {}
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(28, (len(a)-85)):
        raw_data.append((a[i]))
    for elements in raw_data:
        a = elements.split("\t")
        b = a[0]
        names = get_names(b)
        if names != None:
            list_stars.append(names)
    for elements in list_stars:
        dict ={}
        a=elements.split(";")
        if len(a) == 5:
            name = a[4]
        else:
            name = a[0]
        ar = convert_ar(a[1])
        dec = convert_deg(a[2])
        dist = a[3]
        y = float(dist) * math.sin(dec) * math.sin(ar)
        x = float(dist) * math.sin(dec) * math.cos(ar)
        z = float(dist) * math.sin(dec)
        print(x, y, z)
        ax.scatter(x, y, z)

        dict ={"ar": ar, "dec":dec, "dist":dist}
        dict_stars[name] = dict
    print(dict_stars)
    print(len(dict_stars))

    ax.scatter(x, y, z, color= "b")
    ax.scatter(0,0,0, color= "red")
    plt.show()

def convert_deg(data):
    a = data.split(" ")
    if len(a) == 3:
        grad = float(a[0])
        minute = float(a[1])
        sec = float(a[2])
        minute = minute / 60
        sec = sec / 3600
        grad = grad + minute + sec
    else:
        grad = float(a[0])
        minute = float(a[1])
        minute = minute / 60
        grad = grad + minute
    return(grad)

def convert_ar(data):
    a = data.split(" ")
    if len(a) == 3:
        grad = float(a[0]) * 15
        minute = float(a[1])
        sec = float(a[2])
        minute = minute / 60
        sec = sec / 3600
        grad = grad + minute + sec
    else:
        grad = float(a[0]) * 15
        minute = float(a[1])
        minute = minute / 60
        grad = grad + minute
    return(grad)


def get_names(b):
    name = ""
    ra = ""
    dec = ""
    al = ""
    paralax = ""
    given_name = ""
    try:
        if b[5] == "_____" or "R TOP" in b:
            pass
        else:
            for i in range(5, 17):
                name = name + b[i]
            for i in range(32, 42):
                ra = ra + b[i]
            for i in range(43, 52):
                dec = dec + b[i]
            for i in range(73, 80):
                paralax = paralax + b[i]
            paralax = float(paralax)
            al = 3.26/paralax
            al = str(al)
            if len(b) > 151:
                for i in range(152, len(b)):
                    given_name = given_name + b[i]
                text = (name + ";" + ra + ";" + dec + ";" + al + ";" + given_name)
            else:
                text = (name + ";" + ra + ";" + dec + ";" + al)
            return(text)
    except:
        pass

if __name__ == "__main__":
    # execute only if run as a script
    main()