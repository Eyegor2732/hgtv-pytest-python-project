import os
from dotenv import load_dotenv

load_dotenv()


def get_users():
    email1 = os.getenv("email1")
    email2 = os.getenv("email2")
    email3 = os.getenv("email3")
    email4 = os.getenv("email4")

    # return [(email1, email2, email3, email4)]
    return email1, email2, email3, email4

def get_users1():
    email1 = os.getenv("email1")
    email2 = os.getenv("email2")
    email4 = os.getenv("email4")

    return email1, email2, email4   # no Mike

# ========== Urban Oasis  ===  until 11/21/2024, at 8:59 a.m. ET === hgtv  ===  foodnetwork

def get_oasis():
    return \
        [
            get_users(),
            ("ngxFrame277066", "ngxFrame277068"),
            ("https://www.hgtv.com/sweepstakes/hgtv-urban-oasis/sweepstakes?ocid=xp:sistersite&xp=sistersite",
             "https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-urban-oasis-sweepstakes?ocid=xp:sistersite&xp=sistersite"),
            "oasis",
            "2024-11-21 08:59:00",
            "https://www.hgtv.com/sweepstakes/hgtv-urban-oasis/sweepstakes?ocid=xp:sistersite&xp=sistersite"
        ]


#  ========== Holiday Sweets $5k  ===  until 01/07/2025, at 8:59 a.m. ET  ===  foodnetwork === tlc

def get_sweets():
    return \
        [
            get_users(),
            ("ngxFrame279528", "ngxFrame279530"),
            (
                "https://www.foodnetwork.com/sponsored/sweepstakes/holiday-sweets-and-treats?ocid=xp:sistersite&xp=sistersite",
                "https://www.tlc.com/sweepstakes/holiday-sweets-and-treats?ocid=xp:sistersite&xp=sistersite"),
            "sweets",
            "2025-01-07 08:59:00",
            "https://www.foodnetwork.com/sponsored/sweepstakes/holiday-sweets-and-treats?nl=PC-TLC%3ASweeps_112324_box2-FNSweeps&lid=vmefnq3y10e8"
        ]


# ========== $10KHoliday  ===  until 01/08/2025, at 8:59 a.m. ET  ===  hgtv === foodnetwork

def get_10k():
    return \
        [
            get_users(),
            ("ngxFrame278086", "ngxFrame278088"),
            ("https://www.hgtv.com/shows/10k-to-holiday?xp=sistersite",
             "https://www.foodnetwork.com/sponsored/sweepstakes/10k-to-holiday?xp=sistersite"),
            "10k",
            "2025-01-08 08:59:00",
            "https://www.hgtv.com/shows/10k-to-holiday?nl=PC-TLC%3ASweeps_112324_box1-HGSweeps&lid=jaxq67lj8w6l"
        ]


# ========== Holiday Central $5K  ===  until 01/09/2025, at 8:59 a.m. ET  ===  tlc === discovery

def get_central():
    return \
        [
            get_users(),
            ("ngxFrame279580", "ngxFrame279582"),
            ("https://www.tlc.com/sweepstakes/holiday-central-5k-giveaway?xp=sistersite",
             "https://www.discovery.com/sweepstakes/holiday-central?ocid=xp:sistersite&xp=sistersite"),
            "central",
            "2025-01-09 08:59:00",
            "https://www.tlc.com/sweepstakes/holiday-central-5k-giveaway?nl=PC-TLC%3ASweeps_112324_postcard&lid=53bo7n57t64x"
        ]


# ========== DreamHome  ===  until 02/14/2025, at 5:00 p.m. ET  ===  hgtv === foodnetwork

def get_dream():
    return \
        [
            get_users(),
            ("ngxFrame281392", "ngxFrame281394"),
            ("https://www.hgtv.com/sweepstakes/hgtv-dream-home/sweepstakes",
             "https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-dream-home-sweepstakes"),
            "dream",
            "2025-02-14 17:00:00",
            "https://www.hgtv.com/sweepstakes/hgtv-dream-home/sweepstakes"
        ]

# ========== FreshStart  ===  until 02/14/2025, at 8:59 a.m. ET  ===  hgtv === foodnetwork

def get_fresh():
    return \
        [
            get_users(),
            ("ngxFrame281477", "ngxFrame281480"),
            ("https://www.hgtv.com/sweepstakes/fresh-start",
             "https://www.foodnetwork.com/sponsored/sweepstakes/fresh-start"),
            "fresh",
            "2025-02-14 08:59:00",
            "https://www.hgtv.com/sweepstakes/fresh-start"
        ]

# ========== FreshStart  ===  until 03/11/2025, at 8:59 a.m. ET  ===  foodnetwork === tlc

def get_healthy():
    return \
        [
            get_users(),
            ("ngxFrame281472", "ngxFrame281474"),
            ("https://www.foodnetwork.com/sponsored/sweepstakes/healthy-start",
             "https://www.tlc.com/sweepstakes/healthy-start"),
            "healthy",
            "2025-03-11 08:59:00",
            "https://www.foodnetwork.com/sponsored/sweepstakes/healthy-start"
        ]

# ========== SayYesToCash  ===  until 03/20/2025, at 8:59 a.m. ET  ===  tlc === hgtv

def get_yes():
    return \
        [
            get_users(),
            ("ngxFrame281526", "ngxFrame281529"),
            ("https://www.tlc.com/sweepstakes/say-yes-to-cash",
             "https://www.hgtv.com/sweepstakes/say-yes-to-cash"),
            "yes",
            "2025-03-20 08:59:00",
            "https://www.tlc.com/sweepstakes/say-yes-to-cash"
        ]

# ========== Curb  ===  until 04/23/2025, at 8:59 a.m. ET  ===  hgtv === tlc

def get_curb():
    return \
        [
            get_users(),
            ("ngxFrame283194", "ngxFrame283196"),
            ("https://www.hgtv.com/sweepstakes/curb-appeal?ocid=xp:sistersite&xp=sistersite",
             "https://www.tlc.com/sweepstakes/curb-appeal?ocid=xp:sistersite&xp=sistersite"),
            "curb",
            "2025-04-23 08:59:00",
            "https://www.hgtv.com/sweepstakes/curb-appeal"
        ]

# ========== Tournament of Champions  ===  until 04/21/2025, at 09:00 a.m. ET  ===  foodnetwork

def get_champ():
    return \
        [
            get_users(),
            ("ngxFrame283509", "ngxFrame283509"),
            ("https://www.foodnetwork.com/shows/tournament-of-champions/giveaway",
             "https://www.foodnetwork.com/shows/tournament-of-champions/giveaway"),
            "champ",
            "2025-04-21 09:00:00",
            "https://www.foodnetwork.com/shows/tournament-of-champions/giveaway"
        ]

# ========== Valspar Made IT More  ===  until 05/02/2025, at 17:00 p.m. ET  ===  foodnetwork

def get_valspar():
    return \
        [
            get_users(),
            ("ngxFrame283517", "ngxFrame283517"),
            ("https://www.hgtv.com/sponsored/sweeps/valspar-made-for-more-sweepstakes",
             "https://www.hgtv.com/sponsored/sweeps/valspar-made-for-more-sweepstakes"),
            "valspar",
            "2025-05-02 17:00:00",
            "https://www.hgtv.com/sponsored/sweeps/valspar-made-for-more-sweepstakes"
        ]

# ========== $5K Grocery  ===  until 05/13/2025, at 08:59 a.m. ET  ===  foodnetwork === hgtv

def get_groc():
    return \
        [
            get_users(),
            ("ngxFrame283512", "ngxFrame283514"),
            ("https://www.foodnetwork.com/sponsored/sweepstakes/5k-grocery-giveaway",
             "https://www.hgtv.com/sweepstakes/5k-grocery-giveaway?ocid=sistersite&xp=sistersite"),
            "groc",
            "2025-05-13 08:59:00",
            "https://www.foodnetwork.com/sponsored/sweepstakes/5k-grocery-giveaway"
        ]

# ========== Smart Home  ===  until 05/23/2025, at 17:00 p.m. ET  ===  hgtv === foodnetwork

def get_smart():
    return \
        [
            get_users1(),
           ("ngxFrame284943", "ngxFrame284945"),
            ("https://www.hgtv.com/sweepstakes/hgtv-smart-home/sweepstakes?ocid=direct&xp=sistersite",
             "https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-smart-home-sweepstakes?ocid=sistersite&xp=sistersite"),
            "smart",
            "2025-05-23 17:00:00",
            "https://www.hgtv.com/sweepstakes/hgtv-smart-home/sweepstakes?ocid=direct&xp=sistersite"
        ]

# ========== Spring  ===  until 05/22/2025, at 8:59 a.m. ET  ===  TLC === foodnetwork

def get_spring():
    return \
        [
            get_users(),
            ("ngxFrame284413", "ngxFrame284415"),
            ("https://www.tlc.com/sweepstakes/spring-it-forward?xp=sistersite",
             "https://www.foodnetwork.com/sponsored/sweepstakes/spring-it-forward?ocid=sistersite&xp=sistersite"),
            "spring",
            "2025-05-22 08:59:00",
            "https://www.tlc.com/sweepstakes/spring-it-forward?xp=sistersite"
        ]

# ========== Outside  ===  until 06/25/2025, at 8:59 a.m. ET  ===  HGTV === foodnetwork

def get_outside():
    return \
        [
            get_users1(),
            ("ngxFrame285493", "ngxFrame285495"),
            ("https://www.hgtv.com/sweepstakes/get-outside",
             "https://www.foodnetwork.com/sponsored/sweepstakes/get-outside?xp=sistersite?ocid=direct"),
            "outside",
            "2025-06-25 08:59:00",
            "https://www.hgtv.com/sweepstakes/get-outside"
        ]

class EntriesClass:
    pass
