import json
from tkinter import filedialog

json_file_path = str(filedialog.askopenfilename())

with open(json_file_path, 'r') as j:
     beatmapProperties = json.loads(j.read())
