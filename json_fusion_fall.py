import json
import sys

struct = {}
fusion_fall_file = 'Fusion_Fall_Missions.json'
data = fusion_fall_file.strip("'<>()").replace('\'','/"')
data = dict(data)
data['random_help'] = '1'
struct = json.load(data)
with open(fusion_fall_file, encoding = 'utf-8') as file_obj:
	file_details = json.load(file_obj)
