from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-04d043f6-dbbc-4e6b-819c-73f3c02ca08e')

my_region = 'na1'

me = lol_watcher.summoner.by_name(my_region, 'Sparysgah')
print(me)

my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
match_history = lol_watcher.match.matchlist_by_puuid("americas", me['puuid'])
print()

timeline = lol_watcher.match.timeline_by_match("americas", match_history[0])

for i in timeline["info"]["frames"]:
    print(i["timestamp"])
    for j in i["participantFrames"]:

        print(j, i["participantFrames"][j]["position"])


# print(my_ranked_stats)

# First we get the latest version of the game from data dragon
versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']

# Lets get some champions
current_champ_list = lol_watcher.data_dragon.champions(champions_version)




if __name__ == "__main__":
    # print_newest_match(name="Sparysgah", region="NA")

    pass


# bronze 1-4 1200-1270



