import requests


class Hero:
    hero_url = "https://www.superheroapi.com/api.php/2619421814940190/search/"

    def __init__(self, hero_name):
        self.hero_url = self.hero_url + hero_name
        hero_request = requests.get(self.hero_url)
        self.hero_info = hero_request.json()
        return


def get_heroes_list():
    heroes = []
    heroes += [Hero("Thanos")]
    heroes += [Hero("Hulk")]
    heroes += [Hero("Captain America")]
    return heroes


def get_heroes_info_dictionary(heroes_list):
    hero_intelligence_dict = {}
    for super_hero in heroes_list:
        hero_intelligence_dict[super_hero.hero_info['results'][0]['name']] = \
        super_hero.hero_info['results'][0]['powerstats']['intelligence']
    return hero_intelligence_dict


def determine_smartest_hero(hero_intelligence_dict_local):
    global smartest_hero_name
    hero_intelligence_max = 0
    for key, value in hero_intelligence_dict_local.items():
        value = int(value)
        if value > hero_intelligence_max:
            hero_intelligence_max = value
            smartest_hero_name = key
    print(u"Самый умный герой:", smartest_hero_name)
    return


if __name__ == "__main__":
    hero_list = get_heroes_list()
    hero_dict = get_heroes_info_dictionary(hero_list)
    determine_smartest_hero(hero_dict)
