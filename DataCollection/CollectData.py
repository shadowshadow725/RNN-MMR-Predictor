from RiotAPI.main import get_champion_id, get_player_name, get_frame
from whatismymmr.APIwrapper import call_api
from riotwatcher import LolWatcher, ApiError
from datetime import datetime
from typing import List, Dict
import os
import json
from random import randint

my_region = 'na1'
area = 'americas'
base_uri = "https://na.whatismymmr.com/api/v1/summoner?name="
lol_watcher = None
data_points = 1000


def collect_agame(playername: str) -> Dict:

    me = lol_watcher.summoner.by_name(my_region, playername)
    match_history = lol_watcher.match.matchlist_by_puuid("americas", me['puuid'])
    for j in range(randint(1, 4), 20):
        data = lol_watcher.match.by_id("americas", match_history[j])
        if data['info']['queueId'] == 420 and '12.5' in data['info']['gameVersion']:
            timeline = lol_watcher.match.timeline_by_match("americas", match_history[j])
            champion_ids = get_champion_id(data)
            player_names = get_player_name(timeline, lol_watcher)
            timeline = get_frame(timeline)
            data_dictionary = {}
            data_dictionary['match_id'] = match_history[j]
            for i in range(10):
                player = {}
                player['timeline'] = timeline[i]
                player['name'] = player_names[i]
                player['champion_id'] = champion_ids[i]
                res = call_api(base_uri + player_names[i]).json()
                if 'ranked' in res:
                    player['elo'] = res['ranked']['avg']
                else:
                    player['elo'] = -1
                data_dictionary[str(i)] = player

            return data_dictionary



if __name__ == "__main__":
    riot_api_key = input('input riot api key: ')
    starting_user = input('input the username of some '
                          'random player that played ranked: ')
    # riot_api_key = 'RGAPI-9d17f8eb-6f44-42a4-b925-2e0c9bfc89f5'
    # starting_user = 'Sparysgah'
    lol_watcher = LolWatcher(riot_api_key)
    if not os.path.exists('data'):
        os.makedirs('data')
    next_user = starting_user
    candidate_users = []
    d = {}
    for _ in range(data_points):

        d_cur = collect_agame(next_user)
        if d_cur:
            d = d_cur
            f = open('data/' + d['match_id'] + '.json', 'w')
            js = json.dumps(d, indent=4)
            for j in range(10):
                if j != next_user:
                    candidate_users.append(d[str(j)]['name'])
            try:
                f.write(js)
            except:
                pass

            f.close()
        next_user = candidate_users.pop(randint(0, len(candidate_users)-1))








