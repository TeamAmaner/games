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
        self.insider = Inside()


class Channels():
    def __init__(self):
        self.yes = "no"
        self.wolf = None
        self.fortun = None


class Inside:
    def __init__(self):
        self.channel = None
        self.guild = None
        self.role = Inside_Roles()
        self.player = Inside_Player()
        self.channel = Inside_Channel()

class Inside_Roles():
    def __init__(self):
        self.team_a = None
        self.team_b = None

class Inside_Player():
    def __init__(self):
        self.all = []

class Inside_Channel():
    def __init__(self):
        self.team_a = None
        self.team_b = None
