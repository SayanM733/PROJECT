import os
if __name__ == '__main__':
    print("Hello I am RoboSpeaker 1.1 created by Sayan Mandal")
    while True:
        x = input("Enter what you want to me to speake: ")
        if x == "bahenchod":
            # os.system("say 'Chal nikal bahen ki lowdi'")
            break
        command = f"say {x}"
        os.system(command)