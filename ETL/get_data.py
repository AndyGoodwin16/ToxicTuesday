#Import dependencies.
import pandas as pd
import requests
import sqlite3
from pathlib import Path

#Two functions (getGameData and getPickBanData) each take in a game_id and output data in a list of lists format. Create dataframes from output, then manipulate data into appropriate form.

#UPDATE api_key every 24 hours.
api_key = 'INSERT API KEY HERE'

#List of game_ids, COMMENT OUT below after inital data dump to sqlite file.
#game_id_list = ['4438988683', '4439457855', '4439408609', '4448659747', '4448570106', 
#                '4455711721', '4455812037', '4459118495', '4458958951', '4466078171', 
#                '4466088473', '4465928586', '4478377191', '4478377380', '4491811575',
#                '4491943942', '4498152360', '4498234766', '4499796039', '4499841033', 
#                '4499891862', '4503054772', '4503091285', '4503143936', '4503828531',
#                '4503893875', '4505391396', '4505454449', '4511080568', '4511139321',
#                '4511177733']

#UNCOMMENT OUT below to load new data into sqlite file.
game_id_list = ['INSERT GAMEIDS HERE']

#Empty list to collect data.
total_data_list = []
#Function to take in game_id and output game data for each participant.
def getGameData(game_id):
    #Get json data from game_id.
    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/NA1_{game_id}?api_key={api_key}'
    response = requests.get(url).json()
    
    #Create lists of desired stats, seperate by where in json data structure stats exist.
    info_list = ['gameId', 'gameVersion', 'gameDuration']
    participants_list = ['summonerName', 'teamId', 'individualPosition', 'championName', 'win', 'kills', 'deaths', 'assists', 'totalMinionsKilled', 'neutralMinionsKilled', 'goldEarned',
                    'totalDamageDealtToChampions', 'totalDamageTaken', 'totalHeal', 'totalHealsOnTeammates', 'totalDamageShieldedOnTeammates', 'damageDealtToTurrets',
                    'visionScore', 'wardsPlaced', 'wardsKilled', 'visionWardsBoughtInGame', 'firstBloodKill', 'firstBloodAssist', 'firstTowerKill', 'firstTowerAssist',
                    'doubleKills', 'tripleKills', 'quadraKills', 'pentaKills']
    challenges_list = ['laneMinionsFirst10Minutes', 'jungleCsBefore10Minutes', 'outnumberedKills', 'soloKills',
                   'turretPlatesTaken', 'epicMonsterSteals', 'skillshotsHit', 'skillshotsDodged', 'wardsGuarded', 'abilityUses']
    
    #Iterate through lists of desired stats and append response data to an empty list.
    info_data = []
    for i in range(len(info_list)):
        info_data.append(response['info'][info_list[i]])
    
    participants_data = []
    for i in range(0,10):
        for j in range(len(participants_list)):
            participants_data.append(response['info']['participants'][i][participants_list[j]])
    
    #participants_data is a list of lists, where the lists are the desired rows of the dataframe.
    #Split list of lists into single lists for each player based on the length of the lists (or number of participants_list stats pulled).
    y = len(participants_list)
    player1p = participants_data[0:y]
    player2p = participants_data[y:2*y]
    player3p = participants_data[2*y:3*y]
    player4p = participants_data[3*y:4*y]
    player5p = participants_data[4*y:5*y]
    player6p = participants_data[5*y:6*y]
    player7p = participants_data[6*y:7*y]
    player8p = participants_data[7*y:8*y]
    player9p = participants_data[8*y:9*y]
    player10p = participants_data[9*y:10*y]
    
    challenges_data = []
    for i in range(0,10):
        for j in range(len(challenges_list)):
            challenges_data.append(response['info']['participants'][i]['challenges'][challenges_list[j]])
    
    z = len(challenges_list)
    player1c = challenges_data[0:z]
    player2c = challenges_data[z:2*z]
    player3c = challenges_data[2*z:3*z]
    player4c = challenges_data[3*z:4*z]
    player5c = challenges_data[4*z:5*z]
    player6c = challenges_data[5*z:6*z]
    player7c = challenges_data[6*z:7*z]
    player8c = challenges_data[7*z:8*z]
    player9c = challenges_data[8*z:9*z]
    player10c = challenges_data[9*z:10*z]
    
    #List concat to get all stats for one player in a single list.
    player1 = info_data + player1p + player1c
    player2 = info_data + player2p + player2c
    player3 = info_data + player3p + player3c
    player4 = info_data + player4p + player4c
    player5 = info_data + player5p + player5c
    player6 = info_data + player6p + player6c
    player7 = info_data + player7p + player7c
    player8 = info_data + player8p + player8c
    player9 = info_data + player9p + player9c
    player10 = info_data + player10p + player10c
    
    #Append lists to empty list outside function so when iterating over multiple game_ids, the data is saved each time.
    total_data_list.append(player1)
    total_data_list.append(player2)
    total_data_list.append(player3)
    total_data_list.append(player4)
    total_data_list.append(player5)
    total_data_list.append(player6)
    total_data_list.append(player7)
    total_data_list.append(player8)
    total_data_list.append(player9)
    total_data_list.append(player10)
    
    return

#Column headers for initial game data dataframe.
headers1 = ['gameId', 'gameVersion', 'gameDuration', 'summonerName', 'teamId', 'individualPosition', 'championName', 'win', 'kills', 'deaths', 'assists', 'totalMinionsKilled', 'neutralMinionsKilled', 
           'goldEarned', 'totalDamageDealtToChampions', 'totalDamageTaken', 'totalHeal', 'totalHealsOnTeammates', 'totalDamageShieldedOnTeammates', 'damageDealtToTurrets', 'visionScore', 'wardsPlaced', 
           'wardsKilled', 'visionWardsBoughtInGame', 'firstBloodKill', 'firstBloodAssist', 'firstTowerKill', 'firstTowerAssist', 'doubleKills', 'tripleKills', 'quadraKills', 'pentaKills', 
           'laneMinionsFirst10Minutes', 'jungleCsBefore10Minutes', 'outnumberedKills', 'soloKills', 'turretPlatesTaken', 'epicMonsterSteals', 'skillshotsHit', 'skillshotsDodged', 'wardsGuarded',
           'abilityUses']

#Iterate over all game_ids into getGameData function. Output is list of lists in total_data_list.
for i in range(len(game_id_list)):
    getGameData(game_id_list[i])

#Create dataframe using output and headers.
df_gamedata = pd.DataFrame(data = total_data_list, columns = headers1)

#Empty list to collect data.
red_bans_name_list = []
blue_bans_name_list = []
champions_picked_list = []

#Function to take in game_id and output pick ban data.
def getPickBanData(game_id):
    #Get json data from game_id and ddragon, which has a key for converting championId to championName.
    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/NA1_{game_id}?api_key={api_key}'
    url2 = 'http://ddragon.leagueoflegends.com/cdn/12.22.1/data/en_US/champion.json'
    response = requests.get(url).json()
    champion_json = requests.get(url2).json()
    
    #Iterate through game_id json and append pick data to list outside function.
    for i in range(0,10):
        champions_picked_list.append(response['info']['gameId'])
        champions_picked_list.append(response['info']['participants'][i]['championName'])
        champions_picked_list.append(response['info']['participants'][i]['teamId'])
        champions_picked_list.append(response['info']['participants'][i]['win'])
    
    #Iterate through game_id json and append ban data per side to list outside function. Red = 1, Blue = 0 in teams.
    red_bans_key_list = []
    for i in range(0,5):
        red_bans_key_list.append(response['info']['teams'][1]['bans'][i]['championId'])
    #List must be in string format to match json data from ddragon.
    red_bans_key_list = list(map(str, red_bans_key_list))
    
    blue_bans_key_list = []
    for i in range(0,5):
        blue_bans_key_list.append(response['info']['teams'][0]['bans'][i]['championId'])
    blue_bans_key_list = list(map(str, blue_bans_key_list))

    #champions_name_list is a list of champion names.
    champions_name_list = list(champion_json['data'].keys())

    #champions_key_list is a list of champion keys indexed the same as champions_name_list.
    champions_key_list = []
    for i in champions_name_list:
        champions_key_list.append(champion_json['data'][i]['key'])

    #Iterate over lists of ban keys per side and champion keys. When keys are equal, take same index in champion keys and append the value at the same index in list of champion names.
    for i in range(len(red_bans_key_list)):
        for j in range(len(champions_key_list)):
            if red_bans_key_list[i] == champions_key_list[j]:
                red_bans_name_list.append(champions_name_list[j])
            
    for i in range(len(blue_bans_key_list)):
        for j in range(len(champions_key_list)):
            if blue_bans_key_list[i] == champions_key_list[j]:
                blue_bans_name_list.append(champions_name_list[j])
    
    return

#Column headers for initial pick data dataframe.
headers2 = ['gameId', 'championName', 'teamId', 'win']

#Iterate over all game_ids into getPickBanData function. Output is list of red side bans, blue side bans, and champions picked.
for i in range(len(game_id_list)):
    getPickBanData(game_id_list[i])

#Change format of champions_picked_list from list to list of lists, 'grouping' elements in the original list together.
picks = []
for i in range(0, 10*len(game_id_list)):
    picks.append(champions_picked_list[4*i:4*(i+1)])

#Create dataframe using output and headers.
df_pick = pd.DataFrame(data = picks, columns = headers2)

#Change format of x_bans_name_list from list to list of lists, 'grouping' elements in the original list together based on game_id and side.
red_bans = []
for i in range(len(game_id_list)):
    red_bans.append(red_bans_name_list[5*i:5*(i+1)])

blue_bans = []
for i in range(len(game_id_list)):
    blue_bans.append(blue_bans_name_list[5*i:5*(i+1)])

#Create dataframes of bans from each side seperated by ban order.
headers3 = ['firstBan', 'secondBan', 'thirdBan', 'fourthBan', 'fifthBan']

df_red_bans = pd.DataFrame(columns = headers3, data = red_bans)
df_blue_bans = pd.DataFrame(columns = headers3, data = blue_bans)

#Create new sqlite file to store initial data or reference existing file.
database_path = 'storage.sqlite'
Path(database_path).touch()
con = sqlite3.connect(database_path)
cur = con.cursor()

#Create tables, COMMENT OUT after initial set up.
# cur.execute('''CREATE TABLE gamedata ( gameId int, gameVersion text, gameDuration int, summonerName text, teamId int, individualPosition text, championName text, win text, kills int, deaths int, assists int, 
#                                         totalMinionsKilled int, neutralMinionsKilled int, goldEarned int, totalDamageDealtToChampions int, totalDamageTaken int, totalHeal int, totalHealsOnTeammates int,
#                                         totalDamageShieldedOnTeammates int, damageDealtToTurrets int, visionScore int, wardsPlaced int, wardsKilled int, visionWardsBoughtInGame int, firstBloodKill text, 
#                                         firstBloodAssist text, firstTowerKill text, firstTowerAssist text, doubleKills int, tripleKills int, quadraKills int, pentaKills int, laneMinionsFirst10Minutes int, 
#                                         jungleCsBefore10Minutes float, outnumberedKills int, soloKills int, turretPlatesTaken int, epicMonsterSteals int, skillshotsHit int, skillshotsDodged int, 
#                                         wardsGuarded int, abilityUses int )''')
# cur.execute('''CREATE TABLE picks ( gameId int, championName text, teamId int, win text)''')
# cur.execute('''CREATE TABLE redBans ( firstBan text, secondBan text, thirdBan text, fourthBan text, fifthBan text )''')
# cur.execute('''CREATE TABLE blueBans ( firstBan text, secondBan text, thirdBan text, fourthBan text, fifthBan text )''')

#Import data.
df_gamedata.to_sql('gamedata', con, if_exists='append', index=False)
df_pick.to_sql('picks', con, if_exists='append', index=False)
df_red_bans.to_sql('redBans', con, if_exists='append', index=False)
df_blue_bans.to_sql('blueBans', con, if_exists='append', index=False)

#Close connection.
con.close()