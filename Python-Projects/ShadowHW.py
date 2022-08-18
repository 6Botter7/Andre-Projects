from tokenize import Name


squad = {
    "VooDoo": {
        "Name": "Andre Williams",
        "Age": 26,
        "Location": "Cape Town",
        "Play Style": "Aggresive"
    },
    "Shadowtoad": {
        "Name": "Johan Rabie",
        "Age": 40,
        "Location": "Gordonsbay",
        "Play Style": "Tactician"
    },
    "Jester": {
        "Name": "Timmy Malan",
        "Age": 30,
        "Location": "Secunda",
        "Play Style": "Aggresive"
    }
}


# def add_member(real_name, age, location, play_style):
#     # my_dict["Name"].append("Guru")
#     squad["VooDoo"],["Name"].append(real_name)
#     squad["VooDoo"],["Age"].append(age)
#     squad["VooDoo"],["Location"].append(location)
#     squad["VooDoo"],["Play Style"].append(play_style)
#     # squad[real_name].append()
#     return squad
def add_member(nick_name, real_name, age, location, play_style):

    # newsquad = squad[nick_name].append(nick_name)
    # squad[newsquad], ["Name"].append(real_name)
    # squad[newsquad], ["Age"].append(age)
    # squad[newsquad], ["Location"].append(location)
    # squad[newsquad], ["Play Style"].append(play_style)
    # # squad[real_name].append()
    # return squad
    squad[nick_name] = {
        "Name": real_name,
        "Age": age,
        "Location": location,
        "Play Style": play_style
    }
    return squad


add_member("Botter", "FA Williams", 27, "Beaufort West", "Passive")
add_member("Preacher", "Matthew Nel", 28, "England", "Passive Aggresive")


def remove_Member(nick_name):
    squad.pop(nick_name)


def display_squad():
    print(squad)
    return squad
