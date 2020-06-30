import requests
from bs4 import BeautifulSoup




def main():
    URL = 'http://web.archive.org/web/20050923194412/http://www.chara.gsu.edu/RECONS/TOP100.htm'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    text = (soup.get_text())
    a = text.split('\n')
    list_stars = []
    dict_stars = {}
    for i in range(62, (len(a)-85)):
        list_stars.append((a[i]))
    for elements in list_stars:
        a = elements.split("\t")
        b = a[0]
        names = get_names(b)
        if names != None:
            dict_stars[names]
    print(dict_stars.keys())


def get_names(b):
    text = ""
    try:
        if b[5] == "_" or "R TOP" in b:
            pass
        else:
            for i in range(5, 19):
                text = text + b[i]
                text.replace(" ","")
            return(text)
    except:
        pass

if __name__ == "__main__":
    # execute only if run as a script
    main()