import os
import json


TOKENN = os.environ['TOKEN']

json_object = json.dumps({
  "DISCORD_TOKEN": TOKENN,
  "GITHUB_TOKEN": "",
  "FEEDBACK_CHANNEL_ID" : 0
})

with open("config.json", "w") as outfile: 
    outfile.write(json_object) 
