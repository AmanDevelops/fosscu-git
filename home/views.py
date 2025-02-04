from django.shortcuts import render

from pathlib import Path
import os
import json
# Build paths inside the project like this: BASE_DIR / 'subdir'.

# Create your views here.
def home(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    members = []
    members_dir = os.path.join(BASE_DIR, 'member')

    hierarchy = ["admin", "member"];

    file_list = os.listdir(members_dir)

    sorted_members = []
    for branch in hierarchy:
        for file in file_list:
            if branch.lower() in file.lower() and file not in sorted_members:
                sorted_members.append(file)
        

    for member in sorted_members:
        with open(f"{members_dir}\{member}", 'r') as f:
            try:
                member_data = json.load(f)
                members.append(member_data)
            except:
                pass
    return render(request, 'home/index.html', {"members": members})