class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.active = True
    
    def validate_email(self):
        """Valida se o email tem formato correto"""
        if not self.email:
            return False
        if not '@' in self.email:
            return False
        if not '.' in self.email.split('@')[1]:
            return False
        return True
    
    def validate_password(self):
        """Valida se a senha atende aos requisitos mínimos de segurança"""
        if len(self.password) < 8:
            return False
        if not any(c.isupper() for c in self.password):
            return False
        if not any(c.isdigit() for c in self.password):
            return False
        return True
    
    def disable(self):
        """Desativa o usuário"""
        self.active = False
        return True
    
    def is_active(self):
        """Retorna se o usuário está ativo"""
        return self.active


class UserManager:
    def __init__(self):
        self.users = {}
    
    def add_user(self, user):
        """Adiciona um usuário ao sistema"""
        if user.username in self.users:
            return False
        
        if not user.validate_email():
            return False
        
        if not user.validate_password():
            return False
        
        self.users[user.username] = user
        return True
    
    def remove_user(self, username):
        """Remove um usuário do sistema"""
        if username not in self.users:
            return False
        
        del self.users[username]
        return True
    
    def get_user(self, username):
        """Obtém um usuário pelo username"""
        return self.users.get(username)
    
    def authenticate(self, username, password):
        """Autentica um usuário"""
        user = self.get_user(username)
        if not user:
            return False
        
        if not user.is_active():
            return False
        
        return user.password == password
    
    def list_users(self):
        """Lista todos os usuários ativos"""
        return [user for user in self.users.values() if user.is_active()]
