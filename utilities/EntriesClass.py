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

# ========== Cartload of Cash  ===  until 05/12/2026, at 8:59 a.m. ET === foodnetwork  ===  hgtv

def get_cartload():
    return \
        [
            get_users(),
            ("ngxFrame296582", "ngxFrame296580"),
            ("https://www.foodnetwork.com/sponsored/sweepstakes/cartload-of-cash?xp=sistersite_hgtv_sweeps_page",
             "https://www.hgtv.com/sweepstakes/cartload-of-cash?ocid=sistersite_hgtv_sweeps_page&xp=sistersite"),
            "cartload",
            "2026-05-12 08:59:00",
            "https://www.foodnetwork.com/sponsored/sweepstakes/cartload-of-cash?xp=sistersite_hgtv_sweeps_page"
        ]

# ========== Let it Grow  ===  until 06/11/2026, at 8:59 a.m. ET === tlc  ===  hgtv

def get_grow():
    return \
        [
            get_users(),
            ("ngxFrame296905", "ngxFrame296907"),
            ("https://www.tlc.com/sweepstakes/let-it-grow?xp=sistersite_hgtv_sweeps_page",
             "https://www.hgtv.com/sweepstakes/let-it-grow?xp=sistersite?ocid=sistersite_hgtv_sweeps_page"),
            "grow",
            "2026-06-11 08:59:00",
            "https://www.tlc.com/sweepstakes/let-it-grow?xp=sistersite_hgtv_sweeps_page"
        ]

# ========== Ultimate Backyard Oasis  ===  until 06/03/2026, at 8:59 a.m. ET === hgtv  ===  foodnetwork

def get_backyard():
    return \
        [
            get_users(),
            ("ngxFrame296898", "ngxFrame296900"),
            ("https://www.hgtv.com/sweepstakes/ultimate-backyard-oasis",
             "https://www.foodnetwork.com/sponsored/sweepstakes/ultimate-backyard-oasis?ocid=direct&xp=sistersite"),
            "backyard",
            "2026-06-03 08:59:00",
            "https://www.hgtv.com/sweepstakes/ultimate-backyard-oasis"
        ]


class EntriesClass:
    pass
