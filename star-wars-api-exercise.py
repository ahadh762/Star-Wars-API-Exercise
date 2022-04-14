from dataclasses import dataclass, field
import requests


@dataclass
class Star_Wars_Film:
    def __init__(self, episode_ID):
        self.__episodeID = episode_ID
    title: str
    opening_crawl: str
    director: str
    producer: str
    release_date: str
    characters: list
    plot: str
    rating: int
    box_office_gross: int = field(metadata={"units":"dollars"})
    def __gt__(self,other):
        return self.__episodeID > other.__episodeID
    def __eq__(self,other):
        return self.__episodeID == other.__episodeID
    def __ge__(self,other):
        return self.__episodeID >= other.__episodeID


@dataclass
class Character:
    name: str
    height: str = field(metadata={"units":"meters"})
    mass: int = field(metadata={"units":"kilograms"})
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    def __str__(self):
        return f"\n{self.name}, {self.height}, {self.mass}, {self.hair_color},{self.skin_color},{self.eye_color},{self.gender}"


@dataclass
class Star_Wars_Library:
    films_list: list
    shows_list: list
    last_updated_date: str




def getJSON(url): # Function makes a get request for a URL and returns a JSON Dict
    response = requests.get(url)
    return response.json()


def Emoji_List (url, class_name):
    json = getJSON(url)
    emoji_list = []
    for i in range(len(json)):
        emoji = class_name(json[i]["name"],json[i]["group"],''.join(json[i]["htmlCode"]),''.join(json[i]["unicode"]))
        emoji_list.append(emoji)
    return emoji_list

