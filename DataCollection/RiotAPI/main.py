from riotwatcher import LolWatcher, ApiError
from typing import Dict
lol_watcher = LolWatcher('RGAPI-c32fd404-5d2e-4780-8d1b-144d1dac38a4')

my_region = 'na1'

me = lol_watcher.summoner.by_name(my_region, 'Sparysgah')
print(me)

my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
match_history = lol_watcher.match.matchlist_by_puuid("americas", me['puuid'])
timeline = lol_watcher.match.timeline_by_match("americas", match_history[0])
data = lol_watcher.match.by_id("americas", match_history[0])


def get_champion_id(match: Dict):
    for i in range(10):
        print(match['info']['participants'][i]['championId'])


def get_player_name(timeline: Dict):
    for player in timeline['metadata']['participants']:
        # print(lol_watcher.league.by_id('NA1', player))
        # print(player)
        print(lol_watcher.summoner.by_puuid('na1', player)['name'])


def get_frame(timeline: Dict):
    for i in timeline["info"]["frames"]:
        print(i["timestamp"])
        for j in i["participantFrames"]:
            print(j, i["participantFrames"][j]["position"])
            print(j, i["participantFrames"][j]["totalGold"])
            print(j, i["participantFrames"][j]["xp"])
            print(j, i["participantFrames"][j]["damageStats"]["totalDamageDoneToChampions"])





versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']

# Lets get some champions
current_champ_list = lol_watcher.data_dragon.champions(champions_version)


if __name__ == "__main__":
    pass


# bronze 1-4 1200-1270



