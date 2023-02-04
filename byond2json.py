import json
import requests

def hub2dict(game : str = "Exadv1/SpaceStation13") -> dict:
    """
    Converts current BYOND hub data to a dictionary.
    :param game: game to get the hub data for. e.g. "Exadv1/SpaceStation13"
    :return: dictionary mirroring the hub data.
    """
    hub = requests.get(f"https://secure.byond.com/games/{game}?format=text")
    if hub.status_code != 200:
        raise Exception(f"byond2json: Failed to get hub data for {game}! Request returns {hub.status_code}")
    data = {}
    lines = hub.content.decode("latin-1").split("\n")
    for l in range(0, len(lines)):
        if " = " in lines[l]:
            if lines[l].strip().split(" = ")[1].startswith("\""):
                lines[l] = lines[l].replace("\"", "", 1)
            if lines[l].strip().endswith("\""):
                lines[l] = lines[l][:-2]
    data["type"] = lines[1].strip().split(" = ")[1]
    data["title"] = lines[2].strip().split(" = ")[1]
    data["path"] = lines[3].strip().split(" = ")[1]
    data["short_desc"] = lines[4].strip().split(" = ")[1]
    data["long_desc"] = lines[5].strip().split(" = ")[1]
    data["author"] = lines[6].strip().split(" = ")[1]
    data["version"] = lines[7].strip().split(" = ")[1]
    data["banner"] = lines[8].strip().split(" = ")[1]
    data["icon"] = lines[9].strip().split(" = ")[1]
    data["small_icon"] = lines[10].strip().split(" = ")[1]
    data["multi_player"] = bool(lines[11].split(" = ")[1])
    data["date"] = lines[12].strip().split(" = ")[1]
    data["last_updated"] = lines[13].strip().split(" = ")[1]
    data["last_played"] = lines[14].strip().split(" = ")[1]
    data["listing"] = lines[15].strip().split(" = ")[1]
    data["tags"] = lines[16].strip().split(" = ")[1].replace("list(\"", "").replace("\")", "").split("\", \"")
    data["fans"] = int(lines[17].split(" = ")[1])
    data["screenshots"] = int(lines[18].split(" = ")[1])
    data["video"] = lines[19].strip().split(" = ")[1]
    worlds = []
    worlddata = {}
    for counter in range(21, len(lines[20:])):
        if lines[counter].strip().startswith("world/") or lines[counter].strip() == "":
            worlds.append(worlddata)
            worlddata = {}
        else:
            key = lines[counter].strip().split(" = ")[0]
            value = lines[counter].strip().split(" = ")[1]
            if key == "players":
                value = value.replace("list(\"", "").replace("\")", "").split("\",\"")
                if value == ["list()"]:
                    value = []
            if key == "server_version":
                value = int(value)
            worlddata[key] = value
    data["worlds"] = worlds
    return data

def hub2json(game : str = "Exadv1/SpaceStation13", indent : int = 4) -> str:
    """
    Converts current BYOND hub data to a JSON string.
    :param game: game to get the hub data for. e.g. "Exadv1/SpaceStation13"
    :param indent: JSON indent level. Default is 4.
    :return: JSON string mirroring the hub data.
    """
    return json.dumps(hub2dict(game), indent=indent)
