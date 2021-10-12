import re

def re_weather(weather):
    # usunięcie separatora
    weather = re.sub(r"[OSD]|I(?![A-Z])", "", weather)
    # usunięcie spacji
    weather = re.sub(r" +", " ", weather)
    # usunięcie połączonych napisów z danymi
    weather = re.sub(r"(?<=[A-Z])\-", " -", weather)
    
    return weather