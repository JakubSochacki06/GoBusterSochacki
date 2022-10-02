import os
import requests

# Folder Path
path = "wordlists"

# Change the directory
os.chdir(path)


# iterate through all file
modes = [i[:len(i)-4] for i in os.listdir()]
print(modes)
wordlist = input('Which wordlist would you like to choose?')
url = input('What url would you like to try?')
file_path = f"C:/Users/jsoch/PycharmProjects/pythonProject/goBusterSochaVersion/{path}/{wordlist}.txt"
positive = []
with open(file_path, "r") as data:
    for i in data:
        r = requests.get(url=f'{url}/{i}')
        print(f'testing {url}/{i}')
        if r.status_code == 200:
            positive.append(f'{url}/{i}')
print('''----------POSITIVE RESPONSES------------''')
for i in positive:
    print(i)

# with open("wordlists/")