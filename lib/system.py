class System():
    """システム変数
    status(bool): 起動中の是非
    players(Players): プレイヤー一覧
    guild(discord.Guild): 実行鯖ID

    """
    def __init__(self):
        self.status = "nothing"
        self.guild = None
        self.channel = Channels()
        self.player = Player()
        self.inside = Inside()


class Channels():
    def __init__(self):
        self.yes = "no"
        self.wolf = None
        self.fortun = None

class Player():
    def __init__(self):
        self.yes = "no"
        self.all = []
        self.live = []
        self.dead = []

class Inside:
    def __init__(self):
        self.channel = None
        self.role = Roles()

class Roles():
    def __init__(self):
        self.team_a = None
        self.team_b = None
