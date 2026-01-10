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


# ========== DreamHome  ===  until 02/14/2025, at 5:00 p.m. ET  ===  hgtv === foodnetwork

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


# ========== Smart Home  ===  until 05/23/2025, at 17:00 p.m. ET  ===  hgtv === foodnetwork

def get_smart():
    return \
        [
            get_users(),
            ("ngxFrame284943", "ngxFrame284945"),
            ("https://www.hgtv.com/sweepstakes/hgtv-smart-home/sweepstakes?ocid=direct&xp=sistersite",
             "https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-smart-home-sweepstakes?ocid=sistersite&xp=sistersite"),
            "smart",
            "2025-05-23 17:00:00",
            "https://www.hgtv.com/sweepstakes/hgtv-smart-home/sweepstakes?ocid=direct&xp=sistersite"
        ]


# ========== Halloween Baking Giveaway  ===  until 27/27/2025, at 10:00 p.m. ET  ===  foodnetwork === SINGLE

def get_baking():
    return \
        [
            get_users(),
            ("ngxFrame290730", "ngxFrame290730"),
            ("https://www.foodnetwork.com/shows/halloween-baking-championship/giveaway",
             "https://www.foodnetwork.com/shows/halloween-baking-championship/giveaway"),
            "baking",
            "2025-10-27 22:00:00",
            "https://www.foodnetwork.com/shows/halloween-baking-championship/giveaway"
        ]

# ========== New Year, New Look  ===  until 02/13/2026, at 8:59 a.m. ET  ===  hgtv === foodnetwork

def get_newyear():
    return \
        [
            get_users(),
            ("ngxFrame293641", "ngxFrame293645"),
            ("https://www.hgtv.com/sweepstakes/new-year--new-look",
             "https://www.foodnetwork.com/sponsored/sweepstakes/new-year--new-look?xp=sistersite?ocid=direct"),
            "newyear",
            "2026-02-13 08:59:00",
            "https://www.hgtv.com/sweepstakes/new-year--new-look"
        ]

# ========== Bite Into 2026  ===  until 03/10/2026, at 8:59 a.m. ET === foodnetwork  ===  hgtv

def get_bite():
    return \
        [
            get_users(),
            ("ngxFrame293637", "ngxFrame294176"),
            ("https://www.foodnetwork.com/sponsored/sweepstakes/bite-into-2026?xp=sistersite_hgtv_sweeps_page",
             "https://www.hgtv.com/sweepstakes/bite-into-2026?xp=sistersite?ocid=sistersite_hgtv_sweeps_page"),
            "bite",
            "2026-03-10 08:59:00",
            "https://www.foodnetwork.com/sponsored/sweepstakes/bite-into-2026?xp=sistersite_hgtv_sweeps_page"
        ]

# ========== Dream Big  ===  until 03/10/2026, at 8:59 a.m. ET === tlc  ===  hgtv

def get_big():
    return \
        [
            get_users(),
            ("ngxFrame294314", "ngxFrame294317"),
            ("https://www.tlc.com/sweepstakes/dream-big?xp=sistersite_hgtv_sweeps_page",
             "https://www.hgtv.com/sweepstakes/dream-big?ocid=sistersite_hgtv_sweeps_page&xp=sistersite"),
            "big",
            "2026-03-26 08:59:00",
            "https://www.tlc.com/sweepstakes/dream-big?xp=sistersite_hgtv_sweeps_page"
        ]


class EntriesClass:
    pass
