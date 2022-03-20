from riotwatcher import LolWatcher, ApiError
from typing import Dict
# lol_watcher = LolWatcher('RGAPI-9d17f8eb-6f44-42a4-b925-2e0c9bfc89f5')
#
# my_region = 'na1'
#
# me = lol_watcher.summoner.by_name(my_region, 'Sparysgah')
# print(me)
#
# # my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
# match_history = lol_watcher.match.matchlist_by_puuid("americas", me['puuid'])
# timeline = lol_watcher.match.timeline_by_match("americas", match_history[0])
# data = lol_watcher.match.by_id("americas", match_history[0])
#

def get_champion_id(match: Dict):
    l = []
    for i in range(10):
        l.append(match['info']['participants'][i]['championId'])
    return l


def get_player_name(timeline: Dict, lol_watcher):
    l = []
    for player in timeline['metadata']['participants']:
        l.append(lol_watcher.summoner.by_puuid('na1', player)['name'])
    return l


def get_frame(timeline: Dict):
    l = []
    for i in timeline["info"]["frames"]:
        # print(i["timestamp"])
        k = []
        for j in i["participantFrames"]:
            k.append(i["participantFrames"][j]["position"]['x'])
            k.append(i["participantFrames"][j]["position"]['y'])
            k.append(i["participantFrames"][j]["totalGold"])
            k.append(i["participantFrames"][j]["xp"])
            k.append(i["participantFrames"][j]["damageStats"]["totalDamageDoneToChampions"])
        l.append(k)
    return l


# versions = lol_watcher.data_dragon.versions_for_region(my_region)
# champions_version = versions['n']['champion']

# Lets get some champions
# current_champ_list = lol_watcher.data_dragon.champions(champions_version)


# bronze 1-4 1200-1270



