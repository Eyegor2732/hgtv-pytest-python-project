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


class EntriesClass:
    pass
