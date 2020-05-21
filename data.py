import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channels
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2 
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NzAyMjQwOTE0MjE4NjgwMzIw.XsXcjg.kK2n4ZUTf8_ElulQVciQfQUcYcg'
self_bot_token = 'Njk1MTI0NTE1NjcxMjQ0ODEw.Xr28mA.eaEPnMV6LQyH-ViZQhAti-l1M0Q'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '604142351941763072')

input_hq_private  = [
    "604142351941763072",
    "595636121124208640",
    "595654063870181386",
	    "593990638329004032",
	    "595636170025730048",
	    "568617830258442255",
	    "569420198717816852",
	    "591600008353021953",
	    "585285701671714826",
	    "595301050374815757",
	    "590471026899550208",
	    "589120764347678750",
	    "585682137202819101",
	    "590470896649502750",
	    "590182635653824542",
	    "589120764347678750",
	    "589516793350062100",
    "583796470394781696",
    "604142351941763072", # answers1
    "559442345674670082", #answers2
    '577486564402397194' #trivia-answers
]
input_hq_public = ['604142351941763072']
command_channel = '604142351941763072' #trivia-answers
admin_chat = '604142351941763072' # answers2

game_in_session = False
counter_public_1 = 0 
counter_public_2 = 0
counter_public_3 = 0
counter_public_4 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter_private_4 = 0
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0
wronggone4 = 0

seconds_elapsed = 0
