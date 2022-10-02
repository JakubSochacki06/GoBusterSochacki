import os
import requests
import threading
import time

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


def main():

    def thread1():
        with open(file_path, "r") as input_file:
            data = input_file.readlines()
            # from 0% to 25% of data
            for i in data[:int(len(data) / 4)]:
                time.sleep(0.1)
                r = requests.get(url=f'{url}/{i}')
                print("THREAD1")
                print(f'testing {url}/{i}')
                if r.status_code == 200:
                    positive.append(f'{url}/{i}')

    def thread2():
        with open(file_path, "r") as input_file:
            data = input_file.readlines()
            # from 25% to 50% of data
            for i in data[int(len(data) / 4):int(len(data) / 2)]:
                time.sleep(0.1)
                r = requests.get(url=f'{url}/{i}')
                print("THREAD2")
                print(f'testing {url}/{i}')
                if r.status_code == 200:
                    positive.append(f'{url}/{i}')

    def thread3():
        with open(file_path, "r") as input_file:
            data = input_file.readlines()
            # from 50% to 75% of data
            for i in data[int(len(data) / 2):int(len(data) * 0.75)]:
                time.sleep(0.1)
                r = requests.get(url=f'{url}/{i}')
                print("THREAD3")
                print(f'testing {url}/{i}')
                if r.status_code == 200:
                    positive.append(f'{url}/{i}')

    def thread4():
        with open(file_path, "r") as input_file:
            data = input_file.readlines()
            # from 75% to 100% of data
            for i in data[int(len(data) * 0.75):int(len(data))]:
                time.sleep(0.1)
                r = requests.get(url=f'{url}/{i}')
                print("THREAD4")
                print(f'testing {url}/{i}')
                if r.status_code == 200:
                    positive.append(f'{url}/{i}')

    thread1 = threading.Thread(target=thread1)
    thread2 = threading.Thread(target=thread2)
    thread3 = threading.Thread(target=thread3)
    thread4 = threading.Thread(target=thread4)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    if not thread1.is_alive() and not thread2.is_alive() and not thread3.is_alive() and not thread4.is_alive():
        print('''----------POSITIVE RESPONSES------------''')
        for i in positive:
            print(i)
if __name__ == "__main__":
    main()
# with open("wordlists/")