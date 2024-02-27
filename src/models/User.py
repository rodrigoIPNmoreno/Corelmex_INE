# ---->> clase que se llama de forma externa y recibe el id, usuario, contrasenha y sobrenombre

class User():

    def __init__(self, id, username, password, roles) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.roles = roles