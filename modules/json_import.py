import json
from tkinter import filedialog

def getBeatmapData():
     json_file_path = str(filedialog.askopenfilename())

     with open(json_file_path, 'r') as j:
          return json_file_path, json.loads(j.read())
