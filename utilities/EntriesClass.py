import os
from dotenv import load_dotenv

load_dotenv()


def get_users():
    email1 = os.getenv("email1")
    email2 = os.getenv("email2")
    email3 = os.getenv("email3")
    email4 = os.getenv("email4")

    return email1, email2, email3, email4

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

# ========== DreamHome  ===  until 02/13/2026, at 5:00 p.m. ET  ===  hgtv === foodnetwork

def get_dream():
    return \
        [
            get_users(),
            ("ngxFrame294623", "ngxFrame294625"),
            ("https://www.hgtv.com/sweepstakes/hgtv-dream-home/sweepstakes",
             "https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-dream-home-sweepstakes?xp=sistersite"),
            "dream",
            "2026-02-13 17:00:00",
            "https://www.hgtv.com/sweepstakes/hgtv-dream-home/sweepstakes"
        ]

# ========== Smart Home  ===  until 06/19/2026, at 17:00 p.m. ET  ===  hgtv === foodnetwork

def get_smart():
    return \
        [
            get_users(),
            ("ngxFrame298070", "ngxFrame298072"),
            ("https://www.hgtv.com/sweepstakes/hgtv-smart-home/sweepstakes",
             "https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-smart-home-sweepstakes?ocid=direct&xp=sistersite"),
            "smart",
            "2026-06-19 17:00:00",
            "https://www.hgtv.com/sweepstakes/hgtv-smart-home/sweepstakes"
        ]

# ========== Valspar Made for More  ===  until 05/28/2026, at 5:00 p.m. ET  ===  hgtv === SINGLE

def get_valspar():
    return \
        [
            get_users(),
            ("ngxFrame297290", "ngxFrame297290"),
            ("https://www.hgtv.com/sponsored/sweeps/valspar-made-for-more-sweepstakes",
             "https://www.hgtv.com/sponsored/sweeps/valspar-made-for-more-sweepstakes"),
            "valspar",
            "2026-05-28 17:00:00",
            "https://www.hgtv.com/sponsored/sweeps/valspar-made-for-more-sweepstakes"
        ]

# ========== Summer Flavors  ===  until 09/08/2026, at 8:59 a.m. ET === foodnetwork  ===  food

def get_grill():
    return \
        [
            get_users(),
            ("ngxFrame299802", "ngxFrame299138"),
            ("https://www.foodnetwork.com/sponsored/sweepstakes/grill-master?xp=sistersite_hgtv_sweeps_page",
             "https://www.food.com/sweepstakes/grill-master-5k?xp=sistersite?ocid=sistersite_hgtv_sweeps_page"),
            "grill",
            "2026-09-08 08:59:00",
            "https://www.foodnetwork.com/sponsored/sweepstakes/grill-master?xp=sistersite_hgtv_sweeps_page"
        ]

# ========== Dream it, Win it  ===  until 10/29/2026, at 8:59 a.m. ET === tlc  ===  food

def get_win():
    return \
        [
            get_users(),
            ("ngxFrame300752", "ngxFrame300748"),
            ("https://www.tlc.com/sweepstakes/dream-it--win-it?xp=sistersite_hgtv_sweeps_page",
             "https://www.food.com/sweepstakes/dream-it-win-it?ocid=sistersite_hgtv_sweeps_page&xp=sistersite"),
            "win",
            "2026-10-29 08:59:00",
            "https://www.tlc.com/sweepstakes/dream-it--win-it?xp=sistersite_hgtv_sweeps_page"
        ]

# ========== Trick or Treat  ===  until 10/28/2026, at 8:59 a.m. ET === hgtv  ===  food

def get_trick():
    return \
        [
            get_users(),
            ("ngxFrame300024", "ngxFrame300021"),
            ("https://www.hgtv.com/sweepstakes/trick-or-treat-yourself",
             "https://www.food.com/sweepstakes/trick-or-treat-yourself?ocid=direct&xp=sistersite"),
            "trick",
            "2026-10-28 08:59:00",
            "https://www.hgtv.com/sweepstakes/trick-or-treat-yourself"
        ]


class EntriesClass:
    pass
