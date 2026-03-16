class SocialManager:
    def __init__(self):
        self.posts = 0
    def post(self, content):
        print(f"[Social] AI posztolás: {content}")
        self.posts += 1
    def status(self):
        return f"Posztok száma: {self.posts}"

status = SocialManager()
def post(content): status.post(content)
def status(): return status.status()
