import time
import asyncio

from lcu_driver_multi import Connector


amonge = '''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⣠⣤⣤⣤⣤⣤⣀⣀⠉⠻⣿⣿⣿⣿⣿⣿⣿\n
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⣾⣬⣽⣿⣿⣿⣿⡿⢿⣿⣆⠈⢻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⢀⣞⡉⢩⣙⣿⡿⠉⠄⣠⣤⠤⠉⠄⠄⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠁⣼⣿⣿⣯⣿⣿⠁⢰⣾⣦⡤⠄⢀⣶⡀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⢀⣿⣿⣿⣿⣿⠟⠁⠄⠈⢿⣿⣿⣿⣿⡇⠄⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠇⢸⣿⣿⡟⠛⠃⡠⠄⠄⠄⠈⣿⣿⣿⣿⡇⠄⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠄⣿⣿⣿⣶⣾⣿⣿⣿⣤⣤⣄⣘⣿⣿⠁⡀⠄⢻⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⣏⣉⣽⣿⣿⣿⣿⣿⣿⣿⣿⠄⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠄⣼⣿⣁⣸⣿⣿⣿⣿⣿⡿⠟⠉⠙⠋⠹⠟⠁⠄⢸⣿⣿⣿
⣿⣿⣿⣿⣿⡏⢀⣿⣿⣿⣿⠋⢠⣤⣤⣤⣤⠈⢿⣿⣷⣦⣄⠄⠄⢸⣿⣿⣿
⣿⠋⣀⣤⣄⣠⣼⣿⣿⣿⣿⡀⢹⣿⣿⣿⣿⠄⢸⣿⣿⣿⣿⣿⠄⢸⣿⣿⣿
⣧⠄⢿⣿⣿⣿⣿⣿⣿⣿⡿⠃⢸⠿⠛⠉⣁⣠⣿⣿⣿⣿⣿⣿⠄⣼⣿⣿⣿
⣿⣷⣄⣉⠉⠉⢉⣉⣉⣁⣤⣾⡏⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣈⠙⠛⠛⠟⠛⠛⢉⣁⣤⣾⣿⣿⣿⣿'''
amoguspotion = '''
GUYS! If i spin this fidget spinner, on this amangas, for 5 seconds, you guys have to smashdat like butten. Yeah guys, Let's do this. 3 2 1 go. 1,2,3,4,5,6,7,8,9,10, BOOM now you guys have to smashdat like button! Wanna join my free gift cards giveaway? Subscribe to my channel, Like the video, and turn notifications on. And finally, tell me on the comment section that you subscribed. HEY N AND A SQUAD WELCOME BACK TO ANOTHER BRAND NEW VIDEO ANOTHER DAY ANOTHER BANGER. GUYS, ON TONIGHTS VIDEO WE HAVE THE MOST INSANE VIDEO ARLIGHT GUYS BECAUSE I'M GONNA BE DRINKING, the amangas potion guys look at this, i ordered this potion a few weeks ago and it just arrived to me alright guys. And look at this potion, like the color looks really weird guys. It's not blue, it's like, it's mixed of everything like you can see some shadows in it. Which is the scariest thing ever guys, and there was this sticker on it. That makes even look more scarier, this is the amangas potion. If you drink this, you will turn into the character from amangas, alright guys i have no idea. But we are gonna try it out and see if this potion actually works, and we are gonna be drinking this potion at 3AM in the morning. It's the only time that the potion works, alright guys. FOR THOSE WHO DOESN'T KNOW WHAT HAPPENS AT 3 AM IN THE MORNING. 3 AM IS THE TIME WHERE ALL THE EVIL SPIRITS COME TO EARTH GUYS. AND IT'S THERE TIME TO DO ANYTHING THEY WANT. THAT'S WHY, ONLY AT 3 AM THE POTIONS WORK. So right now, i'm just gonna be drinking this potion, and see what is going to happen. BOOM, i might turn into this. BUT BEFORE THIS VIDEO STARTS YOU GUYS KNOW WHAT TO DO. GO DOWN RIGHT NOW, SMASHDAT LIKE BUTTEN, SUBSCRIBE TO MY CHANNEL IF YOU ARE NEW HERE, AND TURN THE POST NOTIFICATIONS ON TO BE A NOTIFICATION SQUAD GUYS! But before this video starts, you know what time it is! *intense dabbing with loud NCS music*. ALRIGHT GUYS LET'S JUST START MESSING AROUND LOOK AT THE TIME! LOOK AT THE TIME GUYS 3:09 AM IN THE MORNING RIGHT NOW. RIGHT OVER HERE let's just open it out right now. oh my god oh my god this is gonna be scary guys. Come on, oh my god it doesn't open okay. OH MY GOD THE POTION IS OPEN RIGHT NOW! Ok perfect let's smell it first. *sniff* OH MY GOD, EEWWW. IT'S SMELLS SO BAD! I don't even know if i wanna drink it anymore it smells so bad. *sniff,sniff,sniff,sniff* EEWWW OH MY GOD IT SMELL SO BAD GUYS! Come on we just have to drink it all, come on. In 3,2,1 *Drinks*. AAAAHH, OH MY GOD WE ACTUALLY DRANK IT! There's a bit more left i have to finish this bottle. *Drinks* Ok now the bottle is empty. Oh my god guys. Ok now, where's the cap i need to put the cap back on, okay, let's just put the glass down right now. This is it the bottle is empty and i actually drank, the potion, so i'm just gonna put it down here. ALRIGHT GUYS, all we have to do *phone rings*. WAIT WHAT IS THIS! WAIT WHO IS THAT? THIS IS REALLY SCARY GUYS! Oh my gosh should i answer it it? It looks so scary. Hello? "Hello, hello, hello." Hey who is this? "it doesn't matter. i'm calling from space right now." Wait you are calling me from space? How is that possible, why are you calling me from space? "I am the imposter." Wait you are the imposter? OH AMANGAS! WAIT WHAT! HOW ARE YOU CALLING ME RIGHT NOW? "Did you get the potion i sent you?" Yes i dide get, like i got the potion. You sent it to me? "Yes, i made that potion. The potion was created in space." THE POTION WAS CREATED IN SPACE? AND IT WAS SENT TO ME? LIKE YOU MEAN THIS BOTTLE THAT I JUST GOT, CAME FROM SPACE? "It's a really powerful potion. It took us months to make it." Oh my god this took months to make? OK wait, what is going to happen, Like i finished the bottle and drank the whole thing? "We don't know yet. You're the first one to have the potion." Wait what you mean you don't know? you made the potion! "And you're the first one to get it." Like nobody has ever drank this potion i am the first one to do it? "Yes you are. By the way remember, do not, get, scared. Haaa." Okay i'm not scared. "Good, I am on my way now." You're on your way here now? "yes, in case things go wrong." You don't need to control me it's not gonna be that bad. "We are almost there, Goodbye." Wait i hear something outside! Ok ok i'm not gonna be scared, goodbye. That is really creepy guys! And they said they are actually on their way to my house, in case anything goes wrong! Like what can happen to... *faints* *exhales,exhales* What the! Wait what is that? WHAT IS HAPPENING TO MY FACE? Wait wha why i am i turning red and blue, and yellow! WHAT IS HAPPENING RIGHT NOW? *faints* Ohh *exhales,exhales* COME ON, IT'S GETTING WORSE! I THINK I'M TURNING INTO AN IMPOSTER! OH MY GOD I DON'T KNOW HOW TO STOP THIS! OH MY GOD THIS IS THE SCARIEST THING... *faints* AHH *exhales,exhales* OH MY GOD, WHAT IS THIS! YO THAT LOOKS SO SCARY GUYS! I THINK I'M TURNING INTO THE RED IMPOSTER! THIS IS SO SCARY LOOKING RIGHT NOW I DON'T KNOW HOW TO GO BACK. I HAVE NO IDEA WHAT I CAN DO TO BE BACK. THERE IS NO WAY BACK NOW! *faints* OH *exhales,exhales* come, wait, what else happened? OH MY GOD, KNOW I KNOW I AM ACTUALLY TURNING INTO THE IMPOSTER! WAIT WHAT IS HAPPENING TO ME? WHAT, IS.... *faints* OH MY GOD, I ACTUALLY TURNED INTO AN AMANGAS! WOW, WHAT IS HAPPENING? WHY AM I IN THE AIR? OH MY GOD GUYS THIS IS INSANE THIS IS ACTUALLY FUN! OH MY GOD BUT THIS IS LIKE A NEW KIND OF SCARY RIGHT NOW! AND I DON'T KNOW WHY I SOUND LIKE THIS, I SOUND SO SCARY TOO! OH MY GOD GUYS THIS IS THE, WAIT HOW DO I GO BACK I'M ACTUALLY LIKE PANICKING RIGHT NOW I'M GETTING SCARED. I DO WANT TO GO BACK INTO BEING ME! I WANT TO GO BACK INTO BEING ME! Ohoh *exhales,exhales,* OH my god! OH MY GOD I'M ACTUALLY BACK! I'M BACK GUYS IT'S ME! THAT WAS THE MOST INSANE THING EVER THE POTION DIDN'T LAST THAT LONG! WHICH I'M REALLY HAPPY AND I'M BACK TO BEING HUMAN AGAIN! OH MY GOD THE POTION ACTUALLY WORKED! ALRIGHT GUYS, I GUESS I'M JUST GONNA BE ENDING THE VIDEO RIGHT OVER HERE ALRIGHT GUYS. CAUSE THIS IS LIKE SO INSANE! ALRIGHT GUYS, GO DOWN RIGHT NOW SMASHDA LIKE BUTTEN, SUBSCRIBE TO MY CHANNEL IF YOU ARE NEW, AND TURN ON POST NOTIFICATION TO BE A NOTIFICATION SQUAD GUYS. AND I WILL SEE YOU GUYS, IN THE NEXT, VIDEO, PEACE!'''

async def champ_select_chat(connection, message):
    r = await connection.request('get', '/lol-chat/v1/conversations/', data={})
    res = await r.json()
    champ_select_url = ''
    for i in res:
        if i['type'] == 'championSelect':
            champ_select_url = i['id']
    if champ_select_url != '':
        r = await connection.request('post', '/lol-chat/v1/conversations/' + champ_select_url + '/messages', data={'body': message})
        res = await r.json()
        print(res)
    else:
        print('Not in champ select / not connected to chat!')


async def lcu_get(connection, method):
    r = await connection.request('get', method)
    res = await r.json()
    print(res)

async def send_message(connection, target, message):
    r = await connection.request('post', f'/lol-game-client-chat/v1/instant-messages?summonerName={target}&message={message}', data={})
    res = await r.json()
    print(res)

async def send_message2(connection, target, message):
    r = await connection.request('get', '/lol-chat/v1/conversations/', data={})
    res = await r.json()
    url = ""
    for i in res:
        if i['gameName'].lower() == target.lower():
            url = i['id']
    if url != '':
        r = await connection.request('post', '/lol-chat/v1/conversations/' + url + '/messages',
                                     data={'body': message})
        res = await r.json()
        print(res)
    else:
        print(f'Did not find conversation with user {target}')


in_queue_status = "inQueue"
in_champ_select_status = 'championSelect'

async def connect(connection):
    timestamp = time.time() * 1000 - 60 * 60 * 1000
    # Some sample ingame data. Setting your status to this will make the account appear as in a custom game playing Sona for 60 minutes.
    lol_ingame_data = {'championId': '37', 'companionId': '2010', 'gameId': '5304140174',
                       'gameMode': 'CLASSIC', 'gameQueueType': 'NONE', 'gameStatus': 'inGame',
                       'isObservable': 'ALL', 'level': '239', 'mapId': '18', 'masteryScore': '394',
                       'pty': '', 'puuid': '8f7f7e42-1767-533e-8788-1c22759e5d51', 'queueId': '-1',
                       'rankedLeagueDivision': 'NA', 'rankedLeagueQueue': 'RANKED_SOLO_5x5',
                       'rankedLeagueTier': 'CHALLENGER', 'rankedLosses': '0',
                       'rankedPrevSeasonDivision': 'NA', 'rankedPrevSeasonTier': 'CHALLENGER',
                       'rankedSplitRewardLevel': '2', 'rankedWins': '135',
                       'regalia': '{"bannerType":2,"crestType":2}', 'skinVariant': '37017',
                       'skinname': 'Sona Sona', 'timeStamp': str(timestamp)}
    print(f"Using the LCU API with account {connection.name}")
    print("The initial status is:")
    print(connection.request_sync('get', '/lol-chat/v1/me'))
    print("If changing the status does not work, try creating an open lobby.")
    await connection.request('put', '/lol-chat/v1/me', data={'availability': 'offline', 'lol': {'gameStatus': 'outOfGame'}})
    print('Connect handler done.')


# Fired when the client is closed
async def disconnect(connection):
    print(f'The client {connection.name} has been closed. Trying to restart it...')
    connection.loop.create_task(try_start_client_in_endless_loop(connection.name, connect, disconnect, [game_status_ws_entry], connection.loop))

# Called whenever the client status changes
async def game_status_listener(connection, event):
    print(f"The game status of {connection.name} was updated. Changing it back now...")
    new_status = {'availability': 'offline', 'lol': {'gameStatus': 'outOfGame'}}
    # Changing the status should never trigger this function more than once. Because on the second call, it will
    # set the status to the same state it currently is in, which should not result in an update event.
    # But sleep for one second just in case it does somehow trigger itself infinitely...
    await asyncio.sleep(1)
    await connection.request('put', '/lol-chat/v1/me', data=new_status)


async def try_start_client_in_endless_loop(*args):
    found = start_client(*args)
    if not found:
        print(f"Client {args[0]} was not found, waiting 5 seconds and trying again...")
        await asyncio.sleep(5)
        # using unnamed varargs to keep things interesting
        event_loop = args[4]
        event_loop.create_task(try_start_client_in_endless_loop(*args))

# Start the client with the given name, ready listener, close listener, websocket listeners and event loop.
# Returns True if the client was found.
def start_client(name, ready, close, websocket_listeners, event_loop) -> bool:
    print(f"Initializing connector for {name}")
    connector = Connector(name=name, loop=event_loop)
    connector.ready(ready)
    connector.close(close)
    for websocket_listener in websocket_listeners:
        url = websocket_listener['url']
        event_types = websocket_listener['event_types']
        handler_func = websocket_listener['handler_func']
        connector.ws.register(url, event_types=event_types)(handler_func)
    return connector.start()


client_names = ['schuhbart', 'duaiistdusk']
game_status_ws_entry = {'url': '/lol-chat/v1/me', 'event_types': ('UPDATE',),
                        'handler_func': game_status_listener}
def main():
    event_loop = asyncio.get_event_loop()
    for client_name in client_names:
        event_loop.create_task(try_start_client_in_endless_loop(client_name, connect, disconnect, [game_status_ws_entry], event_loop))
    print("Running for eternity. This will consume no resources if no tasks are in the event queue.")
    event_loop.run_forever()


if __name__ == "__main__":
    main()
