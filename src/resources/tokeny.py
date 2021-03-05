import os
import json

def startup():
    TOKENN = os.environ['TOKEN']
    
    print(f'TOKEN IS READY: {TOKENN[:7]}')

    json_object = json.dumps({
    "DISCORD_TOKEN": TOKENN,
    "GITHUB_TOKEN": "",
    "FEEDBACK_CHANNEL_ID" : 0
    })

    with open("config.json", "w") as outfile: 
      outfile.write(json_object)
