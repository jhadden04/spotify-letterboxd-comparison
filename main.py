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
                        'https://letterboxd.com/film/the-godfather/', 'https://letterboxd.com/film/harakiri/',
                        'https://letterboxd.com/film/the-godfather-part-ii/',
                        'https://letterboxd.com/film/seven-samurai/', 'https://letterboxd.com/film/12-angry-men/',
                        'https://letterboxd.com/film/a-dogs-will/',
                        'https://letterboxd.com/film/the-human-condition-iii-a-soldiers-prayer/',
                        'https://letterboxd.com/film/spirited-away/', 'https://letterboxd.com/film/high-and-low/',
                        'https://letterboxd.com/film/a-brighter-summer-day/',
                        'https://letterboxd.com/film/the-shawshank-redemption/', 'https://letterboxd.com/film/yi-yi/',
                        'https://letterboxd.com/film/portrait-of-a-lady-on-fire/',
                        'https://letterboxd.com/film/spider-man-into-the-spider-verse/',
                        'https://letterboxd.com/film/the-human-condition-i-no-greater-love/',
                        'https://letterboxd.com/film/the-dark-knight/', 'https://letterboxd.com/film/goodfellas/',
                        'https://letterboxd.com/film/schindlers-list/', 'https://letterboxd.com/film/central-station/',
                        'https://letterboxd.com/film/the-empire-strikes-back/',
                        'https://letterboxd.com/film/the-good-the-bad-and-the-ugly/',
                        'https://letterboxd.com/film/ikiru/', 'https://letterboxd.com/film/stalker/',
                        'https://letterboxd.com/film/satantango/', 'https://letterboxd.com/film/there-will-be-blood/',
                        'https://letterboxd.com/film/persona/',
                        'https://letterboxd.com/film/the-passion-of-joan-of-arc/',
                        'https://letterboxd.com/film/city-of-god/',
                        'https://letterboxd.com/film/the-lord-of-the-rings-the-return-of-the-king/',
                        'https://letterboxd.com/film/sunset-boulevard/', 'https://letterboxd.com/film/andrei-rublev/',
                        'https://letterboxd.com/film/tokyo-story/', 'https://letterboxd.com/film/woman-in-the-dunes/',
                        'https://letterboxd.com/film/apocalypse-now/',
                        'https://letterboxd.com/film/neon-genesis-evangelion-the-end-of-evangelion/',
                        'https://letterboxd.com/film/ran/', 'https://letterboxd.com/film/in-the-mood-for-love/',
                        'https://letterboxd.com/film/pulp-fiction/', 'https://letterboxd.com/film/the-handmaiden/',
                        'https://letterboxd.com/film/paths-of-glory/',
                        'https://letterboxd.com/film/the-human-condition-ii-road-to-eternity/',
                        'https://letterboxd.com/film/grave-of-the-fireflies/', 'https://letterboxd.com/film/la-haine/',
                        'https://letterboxd.com/film/do-the-right-thing/', 'https://letterboxd.com/film/whiplash-2014/',
                        'https://letterboxd.com/film/2001-a-space-odyssey/', 'https://letterboxd.com/film/close-up/',
                        'https://letterboxd.com/film/fanny-and-alexander/', 'https://letterboxd.com/film/rear-window/',
                        'https://letterboxd.com/film/paris-texas/', 'https://letterboxd.com/film/the-world-of-apu/',
                        'https://letterboxd.com/film/le-trou/', 'https://letterboxd.com/film/princess-mononoke/',
                        'https://letterboxd.com/film/psycho/', 'https://letterboxd.com/film/the-silence-of-the-lambs/',
                        'https://letterboxd.com/film/scenes-from-a-marriage/',
                        'https://letterboxd.com/film/cinema-paradiso/',
                        'https://letterboxd.com/film/a-woman-under-the-influence/',
                        'https://letterboxd.com/film/the-apartment/', 'https://letterboxd.com/film/the-given-word/',
                        'https://letterboxd.com/film/autumn-sonata/',
                        'https://letterboxd.com/film/mishima-a-life-in-four-chapters/',
                        'https://letterboxd.com/film/sansho-the-bailiff/',
                        'https://letterboxd.com/film/once-upon-a-time-in-the-west/',
                        'https://letterboxd.com/film/perfect-blue/', 'https://letterboxd.com/film/the-shining/',
                        'https://letterboxd.com/film/pather-panchali/',
                        'https://letterboxd.com/film/the-lord-of-the-rings-the-fellowship-of-the-ring/',
                        'https://letterboxd.com/film/before-sunrise/', 'https://letterboxd.com/film/ordet/',
                        'https://letterboxd.com/film/alien/', 'https://letterboxd.com/film/eternity-and-a-day/',
                        'https://letterboxd.com/film/the-thing/', 'https://letterboxd.com/film/oldboy/',
                        'https://letterboxd.com/film/its-such-a-beautiful-day/', 'https://letterboxd.com/film/macario/',
                        'https://letterboxd.com/film/before-sunset/',
                        'https://letterboxd.com/film/its-a-wonderful-life/', 'https://letterboxd.com/film/mirror/',
                        'https://letterboxd.com/film/the-red-shoes/', 'https://letterboxd.com/film/city-lights/',
                        'https://letterboxd.com/film/one-flew-over-the-cuckoos-nest/',
                        'https://letterboxd.com/film/the-lord-of-the-rings-the-two-towers/',
                        'https://letterboxd.com/film/barry-lyndon/',
                        'https://letterboxd.com/film/werckmeister-harmonies/',
                        'https://letterboxd.com/film/memories-of-murder/',
                        'https://letterboxd.com/film/the-cranes-are-flying/', 'https://letterboxd.com/film/the-ascent/',
                        'https://letterboxd.com/film/nights-of-cabiria/',
                        'https://letterboxd.com/film/the-seventh-seal/', 'https://letterboxd.com/film/late-spring/',
                        'https://letterboxd.com/film/no-country-for-old-men/', 'https://letterboxd.com/film/m/',
                        'https://letterboxd.com/film/8-half/', 'https://letterboxd.com/film/inglourious-basterds/',
                        'https://letterboxd.com/film/singin-in-the-rain/',
                        'https://letterboxd.com/film/the-battle-of-algiers/',
                        'https://letterboxd.com/film/sherlock-jr/', 'https://letterboxd.com/film/war-and-peace-1966/',
                        'https://letterboxd.com/film/love-exposure/', 'https://letterboxd.com/film/i-am-cuba/',
                        'https://letterboxd.com/film/a-man-escaped/', 'https://letterboxd.com/film/bicycle-thieves/',
                        'https://letterboxd.com/film/the-400-blows/', 'https://letterboxd.com/film/se7en/',
                        'https://letterboxd.com/film/fight-club/', 'https://letterboxd.com/film/incendies/',
                        'https://letterboxd.com/film/army-of-shadows/',
                        'https://letterboxd.com/film/the-best-of-youth/', 'https://letterboxd.com/film/all-about-eve/',
                        'https://letterboxd.com/film/lawrence-of-arabia/',
                        'https://letterboxd.com/film/chungking-express/', 'https://letterboxd.com/film/taxi-driver/',
                        'https://letterboxd.com/film/casablanca/',
                        'https://letterboxd.com/film/dr-strangelove-or-how-i-learned-to-stop-worrying-and-love-the-bomb/',
                        'https://letterboxd.com/film/the-second-mother/', 'https://letterboxd.com/film/a-separation/',
                        'https://letterboxd.com/film/mommy-2014/', 'https://letterboxd.com/film/wild-strawberries/',
                        'https://letterboxd.com/film/modern-times/',
                        'https://letterboxd.com/film/children-of-paradise/',
                        'https://letterboxd.com/film/three-colors-red/',
                        'https://letterboxd.com/film/jeanne-dielman-23-quai-du-commerce-1080-bruxelles/',
                        'https://letterboxd.com/film/yojimbo/', 'https://letterboxd.com/film/napoleon/',
                        'https://letterboxd.com/film/star-wars/', 'https://letterboxd.com/film/landscape-in-the-mist/',
                        'https://letterboxd.com/film/the-sacrifice/',
                        'https://letterboxd.com/film/the-night-of-the-hunter/',
                        'https://letterboxd.com/film/citizen-kane/', 'https://letterboxd.com/film/the-lion-king/',
                        'https://letterboxd.com/film/red-beard/', 'https://letterboxd.com/film/a-special-day/',
                        'https://letterboxd.com/film/fargo/', 'https://letterboxd.com/film/the-wages-of-fear/',
                        'https://letterboxd.com/film/the-great-dictator/',
                        'https://letterboxd.com/film/brief-encounter/', 'https://letterboxd.com/film/la-dolce-vita/',
                        'https://letterboxd.com/film/funeral-parade-of-roses/',
                        'https://letterboxd.com/film/still-walking/', 'https://letterboxd.com/film/back-to-the-future/',
                        'https://letterboxd.com/film/rocco-and-his-brothers/', 'https://letterboxd.com/film/tampopo/',
                        'https://letterboxd.com/film/howls-moving-castle/', 'https://letterboxd.com/film/chinatown/',
                        'https://letterboxd.com/film/the-third-man/',
                        'https://letterboxd.com/film/the-young-girls-of-rochefort/',
                        'https://letterboxd.com/film/aparajito/', 'https://letterboxd.com/film/the-pianist/',
                        'https://letterboxd.com/film/the-big-city/', 'https://letterboxd.com/film/vertigo/',
                        'https://letterboxd.com/film/children-of-men/',
                        'https://letterboxd.com/film/to-be-or-not-to-be/',
                        'https://letterboxd.com/film/eternal-sunshine-of-the-spotless-mind/',
                        'https://letterboxd.com/film/wings-of-desire/',
                        'https://letterboxd.com/film/the-life-and-death-of-colonel-blimp/',
                        'https://letterboxd.com/film/terminator-2-judgment-day/',
                        'https://letterboxd.com/film/we-all-loved-each-other-so-much/',
                        'https://letterboxd.com/film/where-is-my-friends-house/',
                        'https://letterboxd.com/film/moonlight-2016/', 'https://letterboxd.com/film/dog-day-afternoon/',
                        'https://letterboxd.com/film/the-father-2020/', 'https://letterboxd.com/film/amadeus/',
                        'https://letterboxd.com/film/la-notte/',
                        'https://letterboxd.com/film/once-upon-a-time-in-america/',
                        'https://letterboxd.com/film/an-elephant-sitting-still/',
                        'https://letterboxd.com/film/raging-bull/', 'https://letterboxd.com/film/your-name/',
                        'https://letterboxd.com/film/sunrise-a-song-of-two-humans/',
                        'https://letterboxd.com/film/metropolis/', 'https://letterboxd.com/film/coco-2017/',
                        'https://letterboxd.com/film/shoplifters/', 'https://letterboxd.com/film/mulholland-drive/',
                        'https://letterboxd.com/film/ugetsu/', 'https://letterboxd.com/film/z/',
                        'https://letterboxd.com/film/an-autumn-afternoon/', 'https://letterboxd.com/film/paper-moon/',
                        'https://letterboxd.com/film/raise-the-red-lantern/', 'https://letterboxd.com/film/toy-story/',
                        'https://letterboxd.com/film/the-young-and-the-damned/',
                        'https://letterboxd.com/film/nostalgia-1983/',
                        'https://letterboxd.com/film/sweet-smell-of-success/',
                        'https://letterboxd.com/film/a-matter-of-life-and-death/',
                        'https://letterboxd.com/film/make-way-for-tomorrow/',
                        'https://letterboxd.com/film/il-sorpasso/',
                        'https://letterboxd.com/film/raiders-of-the-lost-ark/',
                        'https://letterboxd.com/film/my-neighbor-totoro/', 'https://letterboxd.com/film/minari/',
                        'https://letterboxd.com/film/akira/', 'https://letterboxd.com/film/the-departed/',
                        'https://letterboxd.com/film/marketa-lazarova/', 'https://letterboxd.com/film/solaris/',
                        'https://letterboxd.com/film/the-grand-budapest-hotel/',
                        'https://letterboxd.com/film/rashomon/', 'https://letterboxd.com/film/double-indemnity/',
                        'https://letterboxd.com/film/throne-of-blood/',
                        'https://letterboxd.com/film/life-is-beautiful/',
                        'https://letterboxd.com/film/the-treasure-of-the-sierra-madre/',
                        'https://letterboxd.com/film/opening-night/', 'https://letterboxd.com/film/all-that-jazz/',
                        'https://letterboxd.com/film/witness-for-the-prosecution-1957/',
                        'https://letterboxd.com/film/little-women-2019/', 'https://letterboxd.com/film/early-summer/',
                        'https://letterboxd.com/film/inception/',
                        'https://letterboxd.com/film/manila-in-the-claws-of-light/',
                        'https://letterboxd.com/film/umberto-d/', 'https://letterboxd.com/film/the-hunt-2012/',
                        'https://letterboxd.com/film/rififi/', 'https://letterboxd.com/film/nobody-knows/',
                        'https://letterboxd.com/film/mad-max-fury-road/',
                        'https://letterboxd.com/film/a-face-in-the-crowd/',
                        'https://letterboxd.com/film/a-moment-of-innocence/',
                        'https://letterboxd.com/film/le-samourai/', 'https://letterboxd.com/film/paddington-2/',
                        'https://letterboxd.com/film/once-upon-a-time-in-anatolia/',
                        'https://letterboxd.com/film/life-and-nothing-more/', 'https://letterboxd.com/film/network/',
                        'https://letterboxd.com/film/ace-in-the-hole/',
                        'https://letterboxd.com/film/a-clockwork-orange/', 'https://letterboxd.com/film/boogie-nights/',
                        'https://letterboxd.com/film/saving-private-ryan/', 'https://letterboxd.com/film/winter-light/',
                        'https://letterboxd.com/film/the-iron-giant/', 'https://letterboxd.com/film/rosemarys-baby/',
                        'https://letterboxd.com/film/tokyo-twilight/',
                        'https://letterboxd.com/film/the-red-light-bandit/',
                        'https://letterboxd.com/film/good-will-hunting/', 'https://letterboxd.com/film/get-out-2017/',
                        'https://letterboxd.com/film/cleo-from-5-to-7/', 'https://letterboxd.com/film/taste-of-cherry/',
                        'https://letterboxd.com/film/gangs-of-wasseypur-part-2/',
                        'https://letterboxd.com/film/samurai-rebellion/', 'https://letterboxd.com/film/grand-illusion/',
                        'https://letterboxd.com/film/pans-labyrinth/', 'https://letterboxd.com/film/in-a-lonely-place/',
                        'https://letterboxd.com/film/underground-1995/', 'https://letterboxd.com/film/hope-2013/',
                        'https://letterboxd.com/film/whos-afraid-of-virginia-woolf/',
                        'https://letterboxd.com/film/time-of-the-gypsies/', 'https://letterboxd.com/film/pixote/',
                        'https://letterboxd.com/film/the-face-of-another/',
                        'https://letterboxd.com/film/the-shop-on-main-street/',
                        'https://letterboxd.com/film/some-like-it-hot/', 'https://letterboxd.com/film/heat-1995/',
                        'https://letterboxd.com/film/the-devils/', 'https://letterboxd.com/film/invisible-life/',
                        'https://letterboxd.com/film/eureka-2000/',
                        'https://letterboxd.com/film/the-best-years-of-our-lives/']
    """for i in range(100):
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
        letterboxd_links.append(film_link)"""
    return letterboxd_links


def imdb_link():
    imdb_links = []
    res = requests.get('https://www.imdb.com/chart/top?ref_=tt_awd')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    imdb_links = ['https://imdb.com/title/tt0111161/', 'https://imdb.com/title/tt0068646/',
                  'https://imdb.com/title/tt0071562/', 'https://imdb.com/title/tt0468569/',
                  'https://imdb.com/title/tt0050083/', 'https://imdb.com/title/tt0108052/',
                  'https://imdb.com/title/tt0167260/', 'https://imdb.com/title/tt0110912/',
                  'https://imdb.com/title/tt0060196/', 'https://imdb.com/title/tt0120737/',
                  'https://imdb.com/title/tt0137523/', 'https://imdb.com/title/tt0109830/',
                  'https://imdb.com/title/tt1375666/', 'https://imdb.com/title/tt0167261/',
                  'https://imdb.com/title/tt0080684/', 'https://imdb.com/title/tt0133093/',
                  'https://imdb.com/title/tt0099685/', 'https://imdb.com/title/tt0073486/',
                  'https://imdb.com/title/tt0047478/', 'https://imdb.com/title/tt0114369/',
                  'https://imdb.com/title/tt0118799/', 'https://imdb.com/title/tt0317248/',
                  'https://imdb.com/title/tt0102926/', 'https://imdb.com/title/tt0038650/',
                  'https://imdb.com/title/tt0076759/', 'https://imdb.com/title/tt0120815/',
                  'https://imdb.com/title/tt0120689/', 'https://imdb.com/title/tt0245429/',
                  'https://imdb.com/title/tt0816692/', 'https://imdb.com/title/tt6751668/',
                  'https://imdb.com/title/tt0110413/', 'https://imdb.com/title/tt0056058/',
                  'https://imdb.com/title/tt0114814/', 'https://imdb.com/title/tt0110357/',
                  'https://imdb.com/title/tt0253474/', 'https://imdb.com/title/tt0103064/',
                  'https://imdb.com/title/tt0088763/', 'https://imdb.com/title/tt0120586/',
                  'https://imdb.com/title/tt0027977/', 'https://imdb.com/title/tt0172495/',
                  'https://imdb.com/title/tt0054215/', 'https://imdb.com/title/tt0407887/',
                  'https://imdb.com/title/tt0021749/', 'https://imdb.com/title/tt1675434/',
                  'https://imdb.com/title/tt2582802/', 'https://imdb.com/title/tt0095327/',
                  'https://imdb.com/title/tt0482571/', 'https://imdb.com/title/tt0064116/',
                  'https://imdb.com/title/tt0034583/', 'https://imdb.com/title/tt0095765/',
                  'https://imdb.com/title/tt0047396/', 'https://imdb.com/title/tt0078748/',
                  'https://imdb.com/title/tt0078788/', 'https://imdb.com/title/tt0209144/',
                  'https://imdb.com/title/tt0032553/', 'https://imdb.com/title/tt0082971/',
                  'https://imdb.com/title/tt1853728/', 'https://imdb.com/title/tt0405094/',
                  'https://imdb.com/title/tt8503618/', 'https://imdb.com/title/tt0050825/',
                  'https://imdb.com/title/tt0910970/', 'https://imdb.com/title/tt7286456/',
                  'https://imdb.com/title/tt0081505/', 'https://imdb.com/title/tt4154756/',
                  'https://imdb.com/title/tt0043014/', 'https://imdb.com/title/tt0051201/',
                  'https://imdb.com/title/tt0364569/', 'https://imdb.com/title/tt4633694/',
                  'https://imdb.com/title/tt0119698/', 'https://imdb.com/title/tt0057012/',
                  'https://imdb.com/title/tt1345836/', 'https://imdb.com/title/tt0087843/',
                  'https://imdb.com/title/tt5311514/', 'https://imdb.com/title/tt0090605/',
                  'https://imdb.com/title/tt2380307/', 'https://imdb.com/title/tt4154796/',
                  'https://imdb.com/title/tt8267604/', 'https://imdb.com/title/tt0169547/',
                  'https://imdb.com/title/tt0112573/', 'https://imdb.com/title/tt0057565/',
                  'https://imdb.com/title/tt0082096/', 'https://imdb.com/title/tt0114709/',
                  'https://imdb.com/title/tt1187043/', 'https://imdb.com/title/tt0086879/',
                  'https://imdb.com/title/tt0361748/', 'https://imdb.com/title/tt0119217/',
                  'https://imdb.com/title/tt0086190/', 'https://imdb.com/title/tt0986264/',
                  'https://imdb.com/title/tt0105236/', 'https://imdb.com/title/tt0062622/',
                  'https://imdb.com/title/tt0180093/', 'https://imdb.com/title/tt2106476/',
                  'https://imdb.com/title/tt0052357/', 'https://imdb.com/title/tt0022100/',
                  'https://imdb.com/title/tt0338013/', 'https://imdb.com/title/tt0033467/',
                  'https://imdb.com/title/tt5074352/', 'https://imdb.com/title/tt0045152/',
                  'https://imdb.com/title/tt0012349/', 'https://imdb.com/title/tt0040522/',
                  'https://imdb.com/title/tt0093058/', 'https://imdb.com/title/tt0091251/',
                  'https://imdb.com/title/tt0208092/', 'https://imdb.com/title/tt0044741/',
                  'https://imdb.com/title/tt0053125/', 'https://imdb.com/title/tt0086250/',
                  'https://imdb.com/title/tt0066921/', 'https://imdb.com/title/tt8579674/',
                  'https://imdb.com/title/tt0075314/', 'https://imdb.com/title/tt1255953/',
                  'https://imdb.com/title/tt1832382/', 'https://imdb.com/title/tt0435761/',
                  'https://imdb.com/title/tt0070735/', 'https://imdb.com/title/tt0056172/',
                  'https://imdb.com/title/tt0211915/', 'https://imdb.com/title/tt0017136/',
                  'https://imdb.com/title/tt0053604/', 'https://imdb.com/title/tt0059578/',
                  'https://imdb.com/title/tt0036775/', 'https://imdb.com/title/tt0056592/',
                  'https://imdb.com/title/tt1049413/', 'https://imdb.com/title/tt0097576/',
                  'https://imdb.com/title/tt0113277/', 'https://imdb.com/title/tt0119488/',
                  'https://imdb.com/title/tt6966692/', 'https://imdb.com/title/tt0095016/',
                  'https://imdb.com/title/tt0372784/', 'https://imdb.com/title/tt0055630/',
                  'https://imdb.com/title/tt0071853/', 'https://imdb.com/title/tt0042876/',
                  'https://imdb.com/title/tt0363163/', 'https://imdb.com/title/tt0118849/',
                  'https://imdb.com/title/tt0089881/', 'https://imdb.com/title/tt0105695/',
                  'https://imdb.com/title/tt0053291/', 'https://imdb.com/title/tt0347149/',
                  'https://imdb.com/title/tt0042192/', 'https://imdb.com/title/tt0112641/',
                  'https://imdb.com/title/tt0268978/', 'https://imdb.com/title/tt0993846/',
                  'https://imdb.com/title/tt0057115/', 'https://imdb.com/title/tt0457430/',
                  'https://imdb.com/title/tt0469494/', 'https://imdb.com/title/tt1305806/',
                  'https://imdb.com/title/tt0120735/', 'https://imdb.com/title/tt0055031/',
                  'https://imdb.com/title/tt0081398/', 'https://imdb.com/title/tt0096283/',
                  'https://imdb.com/title/tt0040897/', 'https://imdb.com/title/tt0046912/',
                  'https://imdb.com/title/tt1130884/', 'https://imdb.com/title/tt5027774/',
                  'https://imdb.com/title/tt0015864/', 'https://imdb.com/title/tt0476735/',
                  'https://imdb.com/title/tt0071315/', 'https://imdb.com/title/tt0477348/',
                  'https://imdb.com/title/tt0434409/', 'https://imdb.com/title/tt2096673/',
                  'https://imdb.com/title/tt0084787/', 'https://imdb.com/title/tt0080678/',
                  'https://imdb.com/title/tt0050976/', 'https://imdb.com/title/tt0167404/',
                  'https://imdb.com/title/tt1291584/', 'https://imdb.com/title/tt0107290/',
                  'https://imdb.com/title/tt4729430/', 'https://imdb.com/title/tt0117951/',
                  'https://imdb.com/title/tt0120382/', 'https://imdb.com/title/tt0031381/',
                  'https://imdb.com/title/tt0266543/', 'https://imdb.com/title/tt0079944/',
                  'https://imdb.com/title/tt12361974/', 'https://imdb.com/title/tt0050986/',
                  'https://imdb.com/title/tt0353969/', 'https://imdb.com/title/tt0266697/',
                  'https://imdb.com/title/tt0083658/', 'https://imdb.com/title/tt0050212/',
                  'https://imdb.com/title/tt0116282/', 'https://imdb.com/title/tt3011894/',
                  'https://imdb.com/title/tt0046438/', 'https://imdb.com/title/tt3170832/',
                  'https://imdb.com/title/tt1205489/', 'https://imdb.com/title/tt0041959/',
                  'https://imdb.com/title/tt0047296/', 'https://imdb.com/title/tt0077416/',
                  'https://imdb.com/title/tt0107207/', 'https://imdb.com/title/tt0978762/',
                  'https://imdb.com/title/tt0112471/', 'https://imdb.com/title/tt2278388/',
                  'https://imdb.com/title/tt0264464/', 'https://imdb.com/title/tt2267998/',
                  'https://imdb.com/title/tt2119532/', 'https://imdb.com/title/tt1392214/',
                  'https://imdb.com/title/tt0060827/', 'https://imdb.com/title/tt8108198/',
                  'https://imdb.com/title/tt0015324/', 'https://imdb.com/title/tt0118715/',
                  'https://imdb.com/title/tt0035446/', 'https://imdb.com/title/tt0072684/',
                  'https://imdb.com/title/tt0017925/', 'https://imdb.com/title/tt1950186/',
                  'https://imdb.com/title/tt0892769/', 'https://imdb.com/title/tt2024544/',
                  'https://imdb.com/title/tt0116231/', 'https://imdb.com/title/tt0077711/',
                  'https://imdb.com/title/tt0031679/', 'https://imdb.com/title/tt1392190/',
                  'https://imdb.com/title/tt0066763/', 'https://imdb.com/title/tt0097165/',
                  'https://imdb.com/title/tt0405159/', 'https://imdb.com/title/tt1201607/',
                  'https://imdb.com/title/tt0092005/', 'https://imdb.com/title/tt0074958/',
                  'https://imdb.com/title/tt0052618/', 'https://imdb.com/title/tt1028532/',
                  'https://imdb.com/title/tt4016934/', 'https://imdb.com/title/tt0061512/',
                  'https://imdb.com/title/tt3315342/', 'https://imdb.com/title/tt0091763/',
                  'https://imdb.com/title/tt0046268/', 'https://imdb.com/title/tt0758758/',
                  'https://imdb.com/title/tt1979320/', 'https://imdb.com/title/tt0113247/',
                  'https://imdb.com/title/tt0053198/', 'https://imdb.com/title/tt0079470/',
                  'https://imdb.com/title/tt0019254/', 'https://imdb.com/title/tt1895587/',
                  'https://imdb.com/title/tt7060344/', 'https://imdb.com/title/tt0395169/',
                  'https://imdb.com/title/tt1954470/', 'https://imdb.com/title/tt0245712/',
                  'https://imdb.com/title/tt2948372/', 'https://imdb.com/title/tt0060107/',
                  'https://imdb.com/title/tt0198781/', 'https://imdb.com/title/tt0075148/',
                  'https://imdb.com/title/tt0087544/', 'https://imdb.com/title/tt0032976/',
                  'https://imdb.com/title/tt0097223/', 'https://imdb.com/title/tt0381681/',
                  'https://imdb.com/title/tt0118694/', 'https://imdb.com/title/tt0048021/',
                  'https://imdb.com/title/tt0405508/', 'https://imdb.com/title/tt0087884/',
                  'https://imdb.com/title/tt8613070/', 'https://imdb.com/title/tt3417422/',
                  'https://imdb.com/title/tt0025316/', 'https://imdb.com/title/tt2991224/',
                  'https://imdb.com/title/tt5323662/', 'https://imdb.com/title/tt0169858/',
                  'https://imdb.com/title/tt4430212/', 'https://imdb.com/title/tt0058946/']

    """for i in range(250):
        imdb = "https://imdb.com"
        soupy = soup.select(
            f'#main > div > span > div > div > div.lister > table > tbody > tr:nth-child({i + 1}) > td.titleColumn > a ')
        link = str((soupy[0]))
        index1 = link.index("/")
        index2 = link.index("\" title")
        link = (link[index1:index2])
        imdb += link
        link = imdb
        imdb_links.append(link)"""
    return imdb_links


def letterboxdimdblinks():
    letterboxd_imdb_links = []
    links = letterboxd_link()
    """for i in range(len(links)):
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
            continue"""
    letterboxd_imdb_links = ['http://www.imdb.com/title/tt6751668/maindetails',
                             'http://www.imdb.com/title/tt0091251/maindetails',
                             'http://www.imdb.com/title/tt0068646/maindetails',
                             'http://www.imdb.com/title/tt0056058/maindetails',
                             'http://www.imdb.com/title/tt0071562/maindetails',
                             'http://www.imdb.com/title/tt0047478/maindetails',
                             'http://www.imdb.com/title/tt0050083/maindetails',
                             'http://www.imdb.com/title/tt0271383/maindetails',
                             'http://www.imdb.com/title/tt0055233/maindetails',
                             'http://www.imdb.com/title/tt0245429/maindetails',
                             'http://www.imdb.com/title/tt0057565/maindetails',
                             'http://www.imdb.com/title/tt0101985/maindetails',
                             'http://www.imdb.com/title/tt0111161/maindetails',
                             'http://www.imdb.com/title/tt0244316/maindetails',
                             'http://www.imdb.com/title/tt8613070/maindetails',
                             'http://www.imdb.com/title/tt4633694/maindetails',
                             'http://www.imdb.com/title/tt0053114/maindetails',
                             'http://www.imdb.com/title/tt0468569/maindetails',
                             'http://www.imdb.com/title/tt0099685/maindetails',
                             'http://www.imdb.com/title/tt0108052/maindetails',
                             'http://www.imdb.com/title/tt0140888/maindetails',
                             'http://www.imdb.com/title/tt0080684/maindetails',
                             'http://www.imdb.com/title/tt0060196/maindetails',
                             'http://www.imdb.com/title/tt0044741/maindetails',
                             'http://www.imdb.com/title/tt0079944/maindetails',
                             'http://www.imdb.com/title/tt0111341/maindetails',
                             'http://www.imdb.com/title/tt0469494/maindetails',
                             'http://www.imdb.com/title/tt0060827/maindetails',
                             'http://www.imdb.com/title/tt0019254/maindetails',
                             'http://www.imdb.com/title/tt0317248/maindetails',
                             'http://www.imdb.com/title/tt0167260/maindetails',
                             'http://www.imdb.com/title/tt0043014/maindetails',
                             'http://www.imdb.com/title/tt0060107/maindetails',
                             'http://www.imdb.com/title/tt0046438/maindetails',
                             'http://www.imdb.com/title/tt0058625/maindetails',
                             'http://www.imdb.com/title/tt0078788/maindetails',
                             'http://www.imdb.com/title/tt0169858/maindetails',
                             'http://www.imdb.com/title/tt0089881/maindetails',
                             'http://www.imdb.com/title/tt0118694/maindetails',
                             'http://www.imdb.com/title/tt0110912/maindetails',
                             'http://www.imdb.com/title/tt4016934/maindetails',
                             'http://www.imdb.com/title/tt0050825/maindetails',
                             'http://www.imdb.com/title/tt0053115/maindetails',
                             'http://www.imdb.com/title/tt0095327/maindetails',
                             'http://www.imdb.com/title/tt0113247/maindetails',
                             'http://www.imdb.com/title/tt0097216/maindetails',
                             'http://www.imdb.com/title/tt2582802/maindetails',
                             'http://www.imdb.com/title/tt0062622/maindetails',
                             'http://www.imdb.com/title/tt0100234/maindetails',
                             'http://www.imdb.com/title/tt0083922/maindetails',
                             'http://www.imdb.com/title/tt0047396/maindetails',
                             'http://www.imdb.com/title/tt0087884/maindetails',
                             'http://www.imdb.com/title/tt0052572/maindetails',
                             'http://www.imdb.com/title/tt0054407/maindetails',
                             'http://www.imdb.com/title/tt0119698/maindetails',
                             'http://www.imdb.com/title/tt0054215/maindetails',
                             'http://www.imdb.com/title/tt0102926/maindetails',
                             'http://www.imdb.com/title/tt6725014/maindetails',
                             'http://www.imdb.com/title/tt0095765/maindetails',
                             'http://www.imdb.com/title/tt0072417/maindetails',
                             'http://www.imdb.com/title/tt0053604/maindetails',
                             'http://www.imdb.com/title/tt0056322/maindetails',
                             'http://www.imdb.com/title/tt0077711/maindetails',
                             'http://www.imdb.com/title/tt0089603/maindetails',
                             'http://www.imdb.com/title/tt0047445/maindetails',
                             'http://www.imdb.com/title/tt0064116/maindetails',
                             'http://www.imdb.com/title/tt0156887/maindetails',
                             'http://www.imdb.com/title/tt0081505/maindetails',
                             'http://www.imdb.com/title/tt0048473/maindetails',
                             'http://www.imdb.com/title/tt0120737/maindetails',
                             'http://www.imdb.com/title/tt0112471/maindetails',
                             'http://www.imdb.com/title/tt0048452/maindetails',
                             'http://www.imdb.com/title/tt0078748/maindetails',
                             'http://www.imdb.com/title/tt0156794/maindetails',
                             'http://www.imdb.com/title/tt0084787/maindetails',
                             'http://www.imdb.com/title/tt0364569/maindetails',
                             'http://www.imdb.com/title/tt2396224/maindetails',
                             'http://www.imdb.com/title/tt0054042/maindetails',
                             'http://www.imdb.com/title/tt0381681/maindetails',
                             'http://www.imdb.com/title/tt0038650/maindetails',
                             'http://www.imdb.com/title/tt0072443/maindetails',
                             'http://www.imdb.com/title/tt0040725/maindetails',
                             'http://www.imdb.com/title/tt0021749/maindetails',
                             'http://www.imdb.com/title/tt0073486/maindetails',
                             'http://www.imdb.com/title/tt0167261/maindetails',
                             'http://www.imdb.com/title/tt0072684/maindetails',
                             'http://www.imdb.com/title/tt0249241/maindetails',
                             'http://www.imdb.com/title/tt0353969/maindetails',
                             'http://www.imdb.com/title/tt0050634/maindetails',
                             'http://www.imdb.com/title/tt0075404/maindetails',
                             'http://www.imdb.com/title/tt0050783/maindetails',
                             'http://www.imdb.com/title/tt0050976/maindetails',
                             'http://www.imdb.com/title/tt0041154/maindetails',
                             'http://www.imdb.com/title/tt0477348/maindetails',
                             'http://www.imdb.com/title/tt0022100/maindetails',
                             'http://www.imdb.com/title/tt0056801/maindetails',
                             'http://www.imdb.com/title/tt0361748/maindetails',
                             'http://www.imdb.com/title/tt0045152/maindetails',
                             'http://www.imdb.com/title/tt0058946/maindetails',
                             'http://www.imdb.com/title/tt0015324/maindetails',
                             'http://www.imdb.com/title/tt0063794/maindetails',
                             'http://www.imdb.com/title/tt1128075/maindetails',
                             'http://www.imdb.com/title/tt0058604/maindetails',
                             'http://www.imdb.com/title/tt0049902/maindetails',
                             'http://www.imdb.com/title/tt0040522/maindetails',
                             'http://www.imdb.com/title/tt0053198/maindetails',
                             'http://www.imdb.com/title/tt0114369/maindetails',
                             'http://www.imdb.com/title/tt0137523/maindetails',
                             'http://www.imdb.com/title/tt1255953/maindetails',
                             'http://www.imdb.com/title/tt0064040/maindetails',
                             'http://www.imdb.com/title/tt0346336/maindetails',
                             'http://www.imdb.com/title/tt0042192/maindetails',
                             'http://www.imdb.com/title/tt0056172/maindetails',
                             'http://www.imdb.com/title/tt0109424/maindetails',
                             'http://www.imdb.com/title/tt0075314/maindetails',
                             'http://www.imdb.com/title/tt0034583/maindetails',
                             'http://www.imdb.com/title/tt0057012/maindetails',
                             'http://www.imdb.com/title/tt3742378/maindetails',
                             'http://www.imdb.com/title/tt1832382/maindetails',
                             'http://www.imdb.com/title/tt3612616/maindetails',
                             'http://www.imdb.com/title/tt0050986/maindetails',
                             'http://www.imdb.com/title/tt0027977/maindetails',
                             'http://www.imdb.com/title/tt0037674/maindetails',
                             'http://www.imdb.com/title/tt0111495/maindetails',
                             'http://www.imdb.com/title/tt0073198/maindetails',
                             'http://www.imdb.com/title/tt0055630/maindetails',
                             'http://www.imdb.com/title/tt0018192/maindetails',
                             'http://www.imdb.com/title/tt0076759/maindetails',
                             'http://www.imdb.com/title/tt0096288/maindetails',
                             'http://www.imdb.com/title/tt0091670/maindetails',
                             'http://www.imdb.com/title/tt0048424/maindetails',
                             'http://www.imdb.com/title/tt0033467/maindetails',
                             'http://www.imdb.com/title/tt0110357/maindetails',
                             'http://www.imdb.com/title/tt0058888/maindetails',
                             'http://www.imdb.com/title/tt0076085/maindetails',
                             'http://www.imdb.com/title/tt0116282/maindetails',
                             'http://www.imdb.com/title/tt0046268/maindetails',
                             'http://www.imdb.com/title/tt0032553/maindetails',
                             'http://www.imdb.com/title/tt0037558/maindetails',
                             'http://www.imdb.com/title/tt0053779/maindetails',
                             'http://www.imdb.com/title/tt0064068/maindetails',
                             'http://www.imdb.com/title/tt1087578/maindetails',
                             'http://www.imdb.com/title/tt0088763/maindetails',
                             'http://www.imdb.com/title/tt0054248/maindetails',
                             'http://www.imdb.com/title/tt0092048/maindetails',
                             'http://www.imdb.com/title/tt0347149/maindetails',
                             'http://www.imdb.com/title/tt0071315/maindetails',
                             'http://www.imdb.com/title/tt0041959/maindetails',
                             'http://www.imdb.com/title/tt0062873/maindetails',
                             'http://www.imdb.com/title/tt0048956/maindetails',
                             'http://www.imdb.com/title/tt0253474/maindetails',
                             'http://www.imdb.com/title/tt0057277/maindetails',
                             'http://www.imdb.com/title/tt0052357/maindetails',
                             'http://www.imdb.com/title/tt0206634/maindetails',
                             'http://www.imdb.com/title/tt0035446/maindetails',
                             'http://www.imdb.com/title/tt0338013/maindetails',
                             'http://www.imdb.com/title/tt0093191/maindetails',
                             'http://www.imdb.com/title/tt0036112/maindetails',
                             'http://www.imdb.com/title/tt0103064/maindetails',
                             'http://www.imdb.com/title/tt0075793/maindetails',
                             'http://www.imdb.com/title/tt0093342/maindetails',
                             'http://www.imdb.com/title/tt4975722/maindetails',
                             'http://www.imdb.com/title/tt0072890/maindetails',
                             'http://www.imdb.com/title/tt10272386/maindetails',
                             'http://www.imdb.com/title/tt0086879/maindetails',
                             'http://www.imdb.com/title/tt0054130/maindetails',
                             'http://www.imdb.com/title/tt0087843/maindetails',
                             'http://www.imdb.com/title/tt8020896/maindetails',
                             'http://www.imdb.com/title/tt0081398/maindetails',
                             'http://www.imdb.com/title/tt5311514/maindetails',
                             'http://www.imdb.com/title/tt0018455/maindetails',
                             'http://www.imdb.com/title/tt0017136/maindetails',
                             'http://www.imdb.com/title/tt2380307/maindetails',
                             'http://www.imdb.com/title/tt8075192/maindetails',
                             'http://www.imdb.com/title/tt0166924/maindetails',
                             'http://www.imdb.com/title/tt0046478/maindetails',
                             'http://www.imdb.com/title/tt0065234/maindetails',
                             'http://www.imdb.com/title/tt0056444/maindetails',
                             'http://www.imdb.com/title/tt0070510/maindetails',
                             'http://www.imdb.com/title/tt0101640/maindetails',
                             'http://www.imdb.com/title/tt0114709/maindetails',
                             'http://www.imdb.com/title/tt0042804/maindetails',
                             'http://www.imdb.com/title/tt0086022/maindetails',
                             'http://www.imdb.com/title/tt0051036/maindetails',
                             'http://www.imdb.com/title/tt0038733/maindetails',
                             'http://www.imdb.com/title/tt0029192/maindetails',
                             'http://www.imdb.com/title/tt0056512/maindetails',
                             'http://www.imdb.com/title/tt0082971/maindetails',
                             'http://www.imdb.com/title/tt0096283/maindetails',
                             'http://www.imdb.com/title/tt10633456/maindetails',
                             'http://www.imdb.com/title/tt0094625/maindetails',
                             'http://www.imdb.com/title/tt0407887/maindetails',
                             'http://www.imdb.com/title/tt0063278/maindetails',
                             'http://www.imdb.com/title/tt0069293/maindetails',
                             'http://www.imdb.com/title/tt2278388/maindetails',
                             'http://www.imdb.com/title/tt0042876/maindetails',
                             'http://www.imdb.com/title/tt0036775/maindetails',
                             'http://www.imdb.com/title/tt0050613/maindetails',
                             'http://www.imdb.com/title/tt0118799/maindetails',
                             'http://www.imdb.com/title/tt0040897/maindetails',
                             'http://www.imdb.com/title/tt0079672/maindetails',
                             'http://www.imdb.com/title/tt0078754/maindetails',
                             'http://www.imdb.com/title/tt0051201/maindetails',
                             'http://www.imdb.com/title/tt3281548/maindetails',
                             'http://www.imdb.com/title/tt0043313/maindetails',
                             'http://www.imdb.com/title/tt1375666/maindetails',
                             'http://www.imdb.com/title/tt0073363/maindetails',
                             'http://www.imdb.com/title/tt0045274/maindetails',
                             'http://www.imdb.com/title/tt2106476/maindetails',
                             'http://www.imdb.com/title/tt0048021/maindetails',
                             'http://www.imdb.com/title/tt0408664/maindetails',
                             'http://www.imdb.com/title/tt1392190/maindetails',
                             'http://www.imdb.com/title/tt0050371/maindetails',
                             'http://www.imdb.com/title/tt0117214/maindetails',
                             'http://www.imdb.com/title/tt0062229/maindetails',
                             'http://www.imdb.com/title/tt4468740/maindetails',
                             'http://www.imdb.com/title/tt1827487/maindetails',
                             'http://www.imdb.com/title/tt0105888/maindetails',
                             'http://www.imdb.com/title/tt0074958/maindetails',
                             'http://www.imdb.com/title/tt0043338/maindetails',
                             'http://www.imdb.com/title/tt0066921/maindetails',
                             'http://www.imdb.com/title/tt0118749/maindetails',
                             'http://www.imdb.com/title/tt0120815/maindetails',
                             'http://www.imdb.com/title/tt0057358/maindetails',
                             'http://www.imdb.com/title/tt0129167/maindetails',
                             'http://www.imdb.com/title/tt0063522/maindetails',
                             'http://www.imdb.com/title/tt0051093/maindetails',
                             'http://www.imdb.com/title/tt0144782/maindetails',
                             'http://www.imdb.com/title/tt0119217/maindetails',
                             'http://www.imdb.com/title/tt5052448/maindetails',
                             'http://www.imdb.com/title/tt0055852/maindetails',
                             'http://www.imdb.com/title/tt0120265/maindetails',
                             'http://www.imdb.com/title/tt0061847/maindetails',
                             'http://www.imdb.com/title/tt0028950/maindetails',
                             'http://www.imdb.com/title/tt0457430/maindetails',
                             'http://www.imdb.com/title/tt0042593/maindetails',
                             'http://www.imdb.com/title/tt0114787/maindetails',
                             'http://www.imdb.com/title/tt3153634/maindetails',
                             'http://www.imdb.com/title/tt0061184/maindetails',
                             'http://www.imdb.com/title/tt0097223/maindetails',
                             'http://www.imdb.com/title/tt0082912/maindetails',
                             'http://www.imdb.com/title/tt0061065/maindetails',
                             'http://www.imdb.com/title/tt0059527/maindetails',
                             'http://www.imdb.com/title/tt0053291/maindetails',
                             'http://www.imdb.com/title/tt0113277/maindetails',
                             'http://www.imdb.com/title/tt0066993/maindetails',
                             'http://www.imdb.com/title/tt6390668/maindetails',
                             'http://www.imdb.com/title/tt0243889/maindetails',
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
#print(scraper(abc, "#titleDetails > div:nth-child(5) > a:nth-child(2)")) # finds the language
#print(scraper(abc, "#titleDetails > div:nth-child(23) > time")) # finds the length
#print(scraper(abc, "#titleDetails > div:nth-child(12)")) # budget, needs indexing/appending
#print(scraper(abc, "#title-overview-widget > div.plot_summary_wrapper > div.titleReviewBar > div:nth-child(1) > a > div > span")) # metacritic score
#print(scraper(abc, "#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > div.subtext > a:nth-child(4)")) # first tag line
#print(scraper(abc, "#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > div.imdbRating > a > span")) # total imdb ratings
#print(scraper(abc, "#title-overview-widget > div.plot_summary_wrapper > div.titleReviewBar > div:nth-child(5) > div.titleReviewBarSubItem > div:nth-child(2) > span")) # imdb popularity
# print(scraper(abc, "#titleDetails > div:nth-child(6)")) # release date

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
