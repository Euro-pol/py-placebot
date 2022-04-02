import requests
import json
import time
color_map = { # credits to some random guy from github
    "#FF4500": 2,  # bright red
    "#FFA800": 3,  # orange
    "#FFD635": 4,  # yellow
    "#00A368": 6,  # darker green
    "#7EED56": 8,  # lighter green
    "#2450A4": 12,  # darkest blue
    "#3690EA": 13,  # medium normal blue
    "#51E9F4": 14,  # cyan
    "#811E9F": 18,  # darkest purple
    "#B44AC0": 19,  # normal purple
    "#FF99AA": 23,  # pink
    "#9C6926": 25,  # brown
    "#000000": 27,  # black
    "#898D90": 29,  # grey
    "#D4D7D9": 30,  # light grey
    "#FFFFFF": 31,  # white
}
print("coded by timof121 in one morning so dont except something super epic")
bearer = input('PUT YOUR BEARER TOKEN HERE: ')
x = input('PUT THE X START COORDINATE HERE: ')
xoffset = input('HOW MUCH WE SHOULD MOVE X EVERY TIME?: ')
y = input('PUT THE Y START COORDINATE HERE: ')
yoffset = input('HOW MUCH WE SHOULD MOVE Y EVERY TIME?: ')
cooldown = input("PUT HOW MUCH COOLDOWN U WANT BEETWEN PLACES IN SECONDS: ")
print("2 = bright red \n 3 = orange \n 4 = yellow \n 6 = darker green \n 8 = lighter green \n 12 = darkest blue \n 13 = medium normal blue \n 14 = cyan \n 18 = darkest purple \n 19 = normal purple \n 23 = pink \n 25 = brown \n 27 = black \n 29 = grey \n 30 = light grey \n 31 = white")
color = input('SELECT FROM THE LIST ABOVE: ')
data = payload = json.dumps(
        {
            "operationName": "setPixel",
            "variables": {
                "input": {
                    "actionName": "r/replace:set_pixel",
                    "PixelMessageData": {
                        "coordinate": {"x": x, "y": y},
                        "colorIndex": color,
                        "canvasIndex": 0,
                    },
                }
            },
            "query": "mutation setPixel($input: ActInput!) {\n  act(input: $input) {\n    data {\n      ... on BasicMessage {\n        id\n        data {\n          ... on GetUserCooldownResponseMessageData {\n            nextAvailablePixelTimestamp\n            __typename\n          }\n          ... on SetPixelResponseMessageData {\n            timestamp\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
        }
    )
headers = {
        "origin": "https://hot-potato.reddit.com",
        "referer": "https://hot-potato.reddit.com/",
        "apollographql-client-name": "mona-lisa",
        "Authorization": "Bearer " + bearer,
        "Content-Type": "application/json",
    }
def send():
    global x
    global y
    for i in range(5):
        r = requests.post("https://gql-realtime-2.reddit.com/query", headers=headers, data=data)
    print(r.text)
    x += xoffset
    y += yoffset
while True:
    send()
    time.sleep(int(cooldown))
