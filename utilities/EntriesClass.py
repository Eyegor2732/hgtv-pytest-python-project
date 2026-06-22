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

# ========== Summer Flavors  ===  until 07/14/2026, at 8:59 a.m. ET === foodnetwork  ===  hgtv

def get_summer():
    return \
        [
            get_users(),
            ("ngxFrame298052", "ngxFrame298054"),
            ("https://www.foodnetwork.com/sponsored/sweepstakes/summer-flavors?xp=sistersite_hgtv_sweeps_page",
             "https://www.tlc.com/sweepstakes/summer-flavors"),
            "summer",
            "2026-07-14 08:59:00",
            "https://www.foodnetwork.com/sponsored/sweepstakes/summer-flavors?xp=sistersite_hgtv_sweeps_page"
        ]

# ========== Summer Cash  ===  until 08/20/2026, at 8:59 a.m. ET === tlc  ===  foodnetwork

def get_cash():
    return \
        [
            get_users(),
            ("ngxFrame299131", "ngxFrame299133"),
            ("https://www.tlc.com/sweepstakes/summer-cash?xp=sistersite_hgtv_sweeps_page",
             "https://www.foodnetwork.com/sponsored/sweepstakes/summer-cash?ocid=sistersite_hgtv_sweeps_page&xp=sistersite"),
            "cash",
            "2026-08-20 08:59:00",
            "https://www.tlc.com/sweepstakes/summer-cash?xp=sistersite_hgtv_sweeps_page"
        ]

# ========== Home Sweet Home  ===  until 08/12/2026, at 8:59 a.m. ET === hgtv  ===  tlc

def get_sweet():
    return \
        [
            get_users(),
            ("ngxFrame299125", "ngxFrame299128"),
            ("https://www.hgtv.com/sweepstakes/home-sweet-home",
             "https://www.tlc.com/sweepstakes/home-sweet-home?xp=sistersite?ocid=direct"),
            "sweet",
            "2026-08-12 08:59:00",
            "https://www.hgtv.com/sweepstakes/home-sweet-home"
        ]


class EntriesClass:
    pass
