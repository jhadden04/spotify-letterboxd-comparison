import bs4
import requests
import matplotlib.pyplot as plt


def letterboxd_link():
    letterboxd_links = []
    res_letterboxd = requests.get('https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/')
    res_letterboxd.raise_for_status()
    soup_letterboxd = bs4.BeautifulSoup(res_letterboxd.text, 'html.parser')
    # makes the code quicker and easier to do
    letterboxd_links = ['https://letterboxd.com/film/parasite-2019/', 'https://letterboxd.com/film/come-and-see/',
                        
                        'https://letterboxd.com/film/the-best-years-of-our-lives/']
    for i in range(100):
        letterboxd = "https://letterboxd.com"
        soupy_letterboxd = soup_letterboxd.select(f"#content > div > div > section > ul > li:nth-child({i + 1}) > div")
        film_link = str(soupy_letterboxd[0])
        index = (film_link.index("data-film-slug"))
        film_link = film_link[index:]
        index1 = film_link.index("/")
        film_link = film_link[index1:]
        index2 = film_link.index("\"")
        film_link = film_link[:index2]
        letterboxd += film_link
        film_link = letterboxd
        letterboxd_links.append(film_link)
    res_letterboxd = requests.get('https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/page/2/')
    res_letterboxd.raise_for_status()
    soup_letterboxd = bs4.BeautifulSoup(res_letterboxd.text, 'html.parser')
    for i in range(100):
        letterboxd = "https://letterboxd.com"
        soupy_letterboxd = soup_letterboxd.select(f"#content > div > div > section > ul > li:nth-child({i + 1}) > div")
        film_link = str(soupy_letterboxd[0])
        index = (film_link.index("data-film-slug"))
        film_link = film_link[index:]
        index1 = film_link.index("/")
        film_link = film_link[index1:]
        index2 = film_link.index("\"")
        film_link = film_link[:index2]
        letterboxd += film_link
        film_link = letterboxd
        letterboxd_links.append(film_link)
    res_letterboxd = requests.get('https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/page/3/')
    res_letterboxd.raise_for_status()
    soup_letterboxd = bs4.BeautifulSoup(res_letterboxd.text, 'html.parser')
    for i in range(50):
        letterboxd = "https://letterboxd.com"
        soupy_letterboxd = soup_letterboxd.select(f"#content > div > div > section > ul > li:nth-child({i + 1}) > div")
        film_link = str(soupy_letterboxd[0])
        index = (film_link.index("data-film-slug"))
        film_link = film_link[index:]
        index1 = film_link.index("/")
        film_link = film_link[index1:]
        index2 = film_link.index("\"")
        film_link = film_link[:index2]
        letterboxd += film_link
        film_link = letterboxd
        letterboxd_links.append(film_link)
    return letterboxd_links


def imdb_link():
    imdb_links = []
    res = requests.get('https://www.imdb.com/chart/top?ref_=tt_awd')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    imdb_links = ['https://imdb.com/title/tt0111161/', 'https://imdb.com/title/tt0068646/',
                 
                  'https://imdb.com/title/tt4430212/', 'https://imdb.com/title/tt0058946/']

    for i in range(250):
        imdb = "https://imdb.com"
        soupy = soup.select(
            f'#main > div > span > div > div > div.lister > table > tbody > tr:nth-child({i + 1}) > td.titleColumn > a ')
        link = str((soupy[0]))
        index1 = link.index("/")
        index2 = link.index("\" title")
        link = (link[index1:index2])
        imdb += link
        link = imdb
        imdb_links.append(link)
    return imdb_links


def letterboxdimdblinks():
    letterboxd_imdb_links = []
    links = letterboxd_link()
    for i in range(len(links)):
        try:
            res = requests.get(links[i])
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            soupy = soup.select(
                "#film-page-wrapper > div.col-17 > section.section.col-10.col-main > p > a:nth-child(1)")
            link = str(soupy[0])
            index1 = link.index("f=\"")
            index2 = link.index("\">I")
            link = link[index1 + 3:index2]
            letterboxd_imdb_links.append(link)
        except:
            continue
    letterboxd_imdb_links = ['http://www.imdb.com/title/tt6751668/maindetails',
                             
                             'http://www.imdb.com/title/tt0036868/maindetails']
    return letterboxd_imdb_links


def letterboxdtitles():
    letterboxd_titles = []
    links = letterboxd_link()
    for i in range(len(links)):
        res = requests.get(letterboxd_link()[i])
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        soupy = soup.select("#featured-film-header > h1")
        title = soupy[0].getText()
        letterboxd_titles.append(title)
    return letterboxd_titles


def imdbtitles():
    imdb_titles = []
    links = imdb_link()
    for i in range(len(links)):
        res = requests.get(imdb_link()[i])
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        soupy = soup.select("#title-overview-widget > div.vital > div.title_block > div > div.titleBar > "
                            "div.title_wrapper > h1")
        title = soupy[0].getText()
        index = title.index("(")
        title = title[:index - 1]
        imdb_titles.append(title)
    return imdb_titles


def imdbratings():
    imdb_ratings = []
    links = imdb_link()
    imdb_ratings = ['9.3', '9.2', '9.0', '9.0', '9.0', '8.9', '8.9', '8.9', '8.8', '8.8', '8.8', '8.8', '8.8', '8.7',
                    '8.7', '8.7', '8.7', '8.7', '8.6', '8.6', '8.6', '8.6', '8.6', '8.6', '8.6', '8.6', '8.6', '8.6',
                    '8.6', '8.6', '8.5', '8.6', '8.5', '8.5', '8.5', '8.5', '8.5', '8.5', '8.5', '8.5', '8.5', '8.5',
                    '8.5', '8.5', '8.5', '8.5', '8.5', '8.5', '8.5', '8.5', '8.4', '8.4', '8.4', '8.4', '8.4', '8.4',
                    '8.4', '8.4', '8.5', '8.4', '8.4', '8.4', '8.4', '8.4', '8.4', '8.4', '8.4', '8.4', '8.4', '8.4',
                    '8.4', '8.4', '8.4', '8.3', '8.4', '8.4', '8.4', '8.3', '8.3', '8.4', '8.3', '8.3', '8.4', '8.3',
                    '8.3', '8.3', '8.3', '8.4', '8.3', '8.3', '8.3', '8.3', '8.3', '8.3', '8.3', '8.3', '8.4', '8.3',
                    '8.3', '8.3', '8.3', '8.3', '8.3', '8.3', '8.3', '8.3', '8.3', '8.3', '8.2', '8.3', '8.3', '8.2',
                    '8.3', '8.3', '8.3', '8.3', '8.3', '8.2', '8.3', '8.2', '8.2', '8.2', '8.2', '8.2', '8.2', '8.2',
                    '8.2', '8.2', '8.2', '8.2', '8.2', '8.3', '8.2', '8.2', '8.2', '8.2', '8.2', '8.2', '8.2', '8.2',
                    '8.2', '8.2', '8.2', '8.2', '8.2', '8.2', '8.2', '8.2', '8.2', '8.2', '8.2', '8.1', '8.2', '8.3',
                    '8.1', '8.1', '8.2', '8.1', '8.1', '8.1', '8.2', '8.1', '8.2', '8.1', '8.2', '8.1', '8.1', '8.1',
                    '8.1', '8.2', '8.2', '8.2', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.2', '8.1', '8.1', '8.1',
                    '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.3', '8.2', '8.1',
                    '8.2', '8.1', '8.1', '8.1', '8.1', '8.1', '8.2', '8.2', '8.1', '8.1', '8.3', '8.1', '8.1', '8.1',
                    '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1',
                    '8.1', '8.1', '8.5', '8.1', '8.2', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.1', '8.2', '8.1',
                    '8.1', '8.1', '8.2', '8.1', '8.1', '8.4', '8.1', '8.2', '8.1', '8.1', '8.2', '8.1']

    """for i in range(len(links)):
        res = requests.get(imdb_link()[i])
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        soupy = soup.select("#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > "
                            "div.imdbRating > div.ratingValue > strong > span")
        title = soupy[0].getText()
        imdb_ratings.append(title)"""

    return imdb_ratings


def letterboxdimdbratings():
    letterboxdratings = []
    # links = letterboxdimdblinks()
    """for i in range(len(links)):
        res = requests.get(links[i])
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        soupy = soup.select("#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > "
                            "div.imdbRating > div.ratingValue > strong > span")
        title = soupy[0].getText()
        letterboxdratings.append(title)"""
    letterboxdratings = ['8.6', '8.3', '9.2', '8.6', '9.0', '8.6', '9.0', '8.6', '8.8', '8.6', '8.4', '8.4', '9.3',
                         '8.2', '8.1', '8.4', '8.5', '9.0', '8.7', '8.9', '8.0', '8.7', '8.8', '8.3', '8.2', '8.4',
                         '8.2', '8.1', '8.1', '8.6', '8.9', '8.4', '8.1', '8.2', '8.5', '8.4', '8.1', '8.2', '8.1',
                         '8.9', '8.1', '8.4', '8.5', '8.5', '8.1', '8.0', '8.5', '8.3', '8.3', '8.1', '8.4', '8.1',
                         '8.5', '8.5', '8.4', '8.5', '8.6', '8.4', '8.5', '8.2', '8.3', '8.3', '8.2', '8.0', '8.4',
                         '8.5', '8.0', '8.4', '8.6', '8.8', '8.1', '8.3', '8.4', '8.0', '8.1', '8.4', '8.3', '8.4',
                         '8.1', '8.6', '8.1', '8.1', '8.5', '8.7', '8.7', '8.1', '8.2', '8.1', '8.3', '8.3', '8.1',
                         '8.2', '8.3', '8.1', '8.3', '8.0', '8.3', '8.3', '8.1', '8.2', '8.3', '8.1', '8.2', '8.3',
                         '8.3', '8.1', '8.6', '8.8', '8.3', '8.2', '8.5', '8.2', '8.3', '8.1', '8.2', '8.5', '8.4',
                         '7.8', '8.3', '8.1', '8.2', '8.5', '8.4', '8.1', '7.8', '8.2', '8.1', '8.6', '8.0', '8.1',
                         '8.0', '8.3', '8.5', '8.4', '8.1', '8.1', '8.1', '8.4', '8.0', '8.0', '7.9', '8.0', '8.5',
                         '8.3', '7.9', '8.2', '8.1', '8.1', '7.7', '8.4', '8.5', '8.3', '8.3', '7.9', '8.2', '8.3',
                         '8.0', '8.1', '8.5', '8.1', '8.1', '7.4', '8.0', '8.3', '8.3', '8.1', '8.4', '7.8', '8.2',
                         '8.4', '8.1', '8.3', '8.4', '7.9', '7.9', '8.3', '8.3', '8.1', '8.1', '8.1', '8.3', '8.3',
                         '8.1', '8.0', '8.1', '8.2', '8.3', '8.4', '8.2', '7.6', '8.0', '8.5', '8.0', '8.1', '8.1',
                         '8.2', '8.3', '8.1', '8.6', '8.2', '8.0', '7.9', '8.4', '7.8', '8.2', '8.8', '7.8', '8.2',
                         '8.3', '8.1', '8.1', '8.1', '8.2', '7.8', '8.1', '7.8', '7.9', '7.9', '8.1', '8.1', '8.3',
                         '7.9', '8.6', '8.1', '8.0', '8.0', '8.1', '7.4', '8.3', '7.7', '7.9', '7.8', '8.4', '8.1',
                         '8.2', '8.0', '8.1', '8.3', '8.0', '8.2', '8.0', '8.0', '8.2', '8.2', '8.2', '7.8', '7.8',
                         '7.8', '8.0']
    return letterboxdratings


def rating_graphs(scraped_rating, website):
    sorted = scraped_rating
    sorted.sort()
    ratings_occurence = {}
    for i in range(len(sorted)):
        if sorted[i] not in ratings_occurence:
            ratings_occurence[sorted[i]] = 1
        else:
            ratings_occurence[sorted[i]] += 1
    rating = []
    times = []
    for key, value in ratings_occurence.items():
        rating.append(key)
        times.append(value)
    plt.bar(rating, times)
    plt.title(f"Ratings of {website} Top 250 on IMDB")
    plt.xlabel("The Film's rating")
    plt.ylabel("No. of times each rating occurs")
    plt.show()


def countrys(link):
    country = []
    links = link
    for i in range(len(links)):
        res = requests.get(links[i])
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        soupy = soup.select("#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > "
                            "div.imdbRating > div.ratingValue > strong > span")
        title = soupy[0].getText()
        country.append(title)
abc = ["https://www.imdb.com/title/tt0068646/?ref_=fn_al_tt_1"]
def scraper(link, selector):
    list_name = []
    links = link
    for i in range(len(links)):
        res = requests.get(links[i])
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        soupy = soup.select(selector)
        item = soupy[0].getText()
        list_name.append(item)
    return list_name


gross_list = (scraper(abc, "#titleDetails > div:nth-child(15)"))
print(gross_list)
for i in range(len(gross_list)):
    index = gross_list[i].index(": ")
    index1 = gross_list[i].index("     ")
    gross_list[i] = gross_list[i][index+3:index1]
    print(gross_list[i])
    for j in range(len(gross_list[i])):
        try:
            if "," == gross_list[i][j]:
                gross_list[i] = (gross_list[i].replace("k", ""))
        except:
            break

print(gross_list)
# rating_graphs(letterboxdimdbratings(), "Letterboxd")
# rating_graphs(imdbratings(), "IMDB")
