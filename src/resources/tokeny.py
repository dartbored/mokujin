import os
import json

def startup():
	TOKENN = os.environ['TOKEN']
	GHT = os.environ['GH']

	print(f'TOKEN IS READY: {TOKENN[:4]}')

	datao = {
		"DISCORD_TOKEN": f'{TOKENN}',
		"GITHUB_TOKEN": f'{GHT}',
		"FEEDBACK_CHANNEL_ID" : 0
	}

	json_object = json.dumps(datao)

	with open("config.json", "w") as outfile: 
		outfile.write(json_object)
