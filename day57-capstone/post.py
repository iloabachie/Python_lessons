# not used in the capstone but shold have.

import requests, ConsolePrint

class Post:
    def __init__(self, id, title, subtitle, body):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.search = str(id) + ": " + title       
      
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: ({self.search})\n"

posts = requests.get("https://api.npoint.io/88838b326e7274d04e53").json()

post_class = []

for post in posts:
    post_class.append(Post(post['id'], post['title'], post['subtitle'], post['body']))

for _ in post_class:
    print(_)


for x in range(2):
    if x % 2 == 1:
        ConsolePrint.startConsoleSave()
    for _ in post_class:
        print(x, "============================================")
        print(_.id)
        print(_.title)
        print(_.subtitle)
        print(_.body)
        print(x, "============================================")
    if x % 5 == 1:
        ConsolePrint.endConsoleSave(prompt=False)
