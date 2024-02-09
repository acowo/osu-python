import json
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()
beatmap_dir = os.path.dirname(file)
osu = open(file,'r+').readlines()
out = {}
sliders = ['C','L','P','B']

def blank(line):
    if line=='' or line=='/n':
        return 1

def get_line(phrase):
    for num, line in enumerate(osu, 0):
        if phrase in line:
            return num

out['general'] = {}
out['metadata'] = {}
out['difficulty'] = {}
out['timingpoints'] = []
out['hitobjects'] = []

general_line = get_line('[General]')
events_line = get_line('[Events]')
metadata_line = get_line('[Metadata]')
difficulty_line = get_line('[Difficulty]')
events_line = get_line('[Events]')
timing_line = get_line('[TimingPoints]')
hit_line = get_line('[HitObjects]')


general_list = osu[general_line:metadata_line-1]
metadata_list = osu[metadata_line:difficulty_line-1]
difficulty_list = osu[difficulty_line:events_line-1]
timingpoints_list = osu[timing_line:hit_line-1]
hitobject_list = osu[hit_line:]

for item in general_list:
    if ':' in item:
        item = item.split(': ')
        out['general'][item[0]] = item[1]

for item in metadata_list:
    if ':' in item:
        item = item.split(':')
        out['metadata'][item[0]] = item[1]

for item in difficulty_list:
    if ':' in item:
        item = item.split(':')
        out['difficulty'][item[0]] = item[1]

for item in timingpoints_list:
    if ',' in item:
        item = item.split(',')
        point = {
        'offset':item[0],
        'millperbeat':item[1]
        }
        try:
            point['meter']:item[2]
        except:
            'nothing'
        out['timingpoints'].append(point)


for item in hitobject_list:
    if ',' in item:
        item = item.split(',')
        point = {
            'x':item[0],
            'y':item[1],
            'time':item[2],
            'type':item[3],
            'hitsound':item[4]
        }
        if item[5] and sliders not in item:
            point['extras'] = item[5]
        try:
            point['slidertype'] = item[6]
        except:
            'nothing'
        out['hitobjects'].append(point)

output = json.dumps(out).replace('\n','')
with open(f'{beatmap_dir}\\'+out['metadata']['Title'].rstrip()+' '+out['metadata']['Version'].rstrip()+'.json','w') as file:
    file.write(output)
print(out['metadata']['Title'].rstrip()+' '+out['metadata']['Version'].rstrip()+'.json written successfully')