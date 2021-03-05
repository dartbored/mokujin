import os
import json

def startup():
    TOKENN = os.environ['TOKEN']
    
    logger.info(f'TOKEN IS READY: {TOKEN[:7]}')

    json_object = json.dumps({
    "DISCORD_TOKEN": TOKENN,
    "GITHUB_TOKEN": "",
    "FEEDBACK_CHANNEL_ID" : 0
    })

    with open("config.json", "w") as outfile: 
      outfile.write(json_object)
