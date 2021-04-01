import requests
cid = 'izy142yv8fg9qzeh4sec8qbh42ksxy'                                                                      
cs = 'd44e3rrdpkx4ufqby16g4xjma8p1qp'
url = f'https://id.twitch.tv/oauth2/token?client_id={cid}&client_secret={cs}&grant_type=client_credentials'   #logs into the api using the info from prior lines              
pl= requests.post(url).json() #pl = payload (aka response)
url = 'https://api.igdb.com/v4/games'
token = pl["access_token"]
headers = {'Client-ID': cid, 'Authorization': f'Bearer {token}'}


data = 'fields *; where id = 989;'
pl2 = requests.post(url, headers=headers, data=data)

def search_twitch(search_text):
    data = f'search "{search_text}";'
    pl2 = requests.post(url, headers=headers, data=data)  
    #extract list of game ids from the API's dictionary
    game_ids = [game['id'] for game in pl2.json()]
    data = f'fields name , id; where id = {tuple(game_ids)};'
    pl2 = requests.post(url, headers=headers, data=data)
    return pl2.json()