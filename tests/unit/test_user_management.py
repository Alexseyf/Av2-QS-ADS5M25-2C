import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from user_management import User, UserManager

class TestUser:
    def test_user_creation(self):
        """Testa a criação de um usuário"""
        user = User("testuser", "test@example.com", "Password123")
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.password == "Password123"
        assert user.active is True

    def test_validate_email_valid(self):
        """Testa validação de email com formato válido"""
        user = User("testuser", "test@example.com", "Password123")
        assert user.validate_email() is True

    def test_validate_email_invalid_no_at(self):
        """Testa validação de email sem @"""
        user = User("testuser", "testexample.com", "Password123")
        assert user.validate_email() is False

    def test_validate_email_invalid_no_domain(self):
        """Testa validação de email sem domínio completo"""
        user = User("testuser", "test@example", "Password123")
        assert user.validate_email() is False

    def test_validate_email_empty(self):
        """Testa validação de email vazio"""
        user = User("testuser", "", "Password123")
        assert user.validate_email() is False

    def test_validate_password_valid(self):
        """Testa validação de senha válida"""
        user = User("testuser", "test@example.com", "Password123")
        assert user.validate_password() is True

    def test_validate_password_too_short(self):
        """Testa validação de senha muito curta"""
        user = User("testuser", "test@example.com", "Pass1")
        assert user.validate_password() is False

    def test_validate_password_no_uppercase(self):
        """Testa validação de senha sem letra maiúscula"""
        user = User("testuser", "test@example.com", "password123")
        assert user.validate_password() is False

    def test_validate_password_no_digit(self):
        """Testa validação de senha sem número"""
        user = User("testuser", "test@example.com", "PasswordABC")
        assert user.validate_password() is False

    def test_disable_user(self):
        """Testa a desativação de um usuário"""
        user = User("testuser", "test@example.com", "Password123")
        assert user.active is True
        
        result = user.disable()
        assert result is True
        assert user.active is False
        assert user.is_active() is False