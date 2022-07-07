import pychromecast
def connect():
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Living Room"])
    return chromecasts[0]