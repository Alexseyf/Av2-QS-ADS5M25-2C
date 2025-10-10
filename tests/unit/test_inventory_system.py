import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from inventory_system import InventorySystem, Product

class TestInventory:
    def test_add_product_success(self):
        """Testa adição de produto com sucesso"""
        inventory = InventorySystem()
        product = Product(1, "Test Product", 19.99, 10)
        
        result = inventory.add_product(product)
        assert result is True
        assert inventory.get_product(1) == product

    def test_add_product_duplicate(self):
        """Testa adição de produto duplicado"""
        inventory = InventorySystem()
        product1 = Product(1, "Test Product", 19.99, 10)
        product2 = Product(1, "Another Product", 29.99, 5)
        
        inventory.add_product(product1)
        result = inventory.add_product(product2)
        assert result is False

    def test_add_product_invalid(self):
        """Testa adição de produto inválido"""
        inventory = InventorySystem()
        product = Product(1, "", -5.0, -5)
        
        result = inventory.add_product(product)
        assert result is False

    def test_remove_product_success(self):
        """Testa remoção de produto com sucesso"""
        inventory = InventorySystem()
        product = Product(1, "Test Product", 19.99, 10)
        
        inventory.add_product(product)
        result = inventory.remove_product(1)
        assert result is True
        assert inventory.get_product(1) is None

    def test_remove_product_nonexistent(self):
        """Testa remoção de produto inexistente"""
        inventory = InventorySystem()
        result = inventory.remove_product(999)
        assert result is False

    def test_get_product(self):
        """Testa obtenção de produto"""
        inventory = InventorySystem()
        product = Product(1, "Test Product", 19.99, 10)
        
        inventory.add_product(product)
        retrieved_product = inventory.get_product(1)
        assert retrieved_product == product
        assert inventory.get_product(999) is None

    def test_update_quantity_increase(self):
        """Testa aumento da quantidade de um produto"""
        inventory = InventorySystem()
        product = Product(1, "Test Product", 19.99, 10)
        
        inventory.add_product(product)
        result = inventory.update_quantity(1, 5)
        assert result is True
        assert product.quantity == 15

    def test_update_quantity_decrease(self):
        """Testa diminuição da quantidade de um produto"""
        inventory = InventorySystem()
        product = Product(1, "Test Product", 19.99, 10)
        
        inventory.add_product(product)
        result = inventory.update_quantity(1, -3)
        assert result is True
        assert product.quantity == 7

    def test_update_quantity_to_zero(self):
        """Testa atualização da quantidade para zero"""
        inventory = InventorySystem()
        product = Product(1, "Test Product", 19.99, 10)
        
        inventory.add_product(product)
        result = inventory.update_quantity(1, -10)
        assert result is True
        assert product.quantity == 0

    def test_update_quantity_below_zero(self):
        """Testa atualização da quantidade para abaixo de zero (deve falhar)"""
        inventory = InventorySystem()
        product = Product(1, "Test Product", 19.99, 10)
        
        inventory.add_product(product)
        result = inventory.update_quantity(1, -15)
        assert result is False
        assert product.quantity == 10

    def test_update_quantity_nonexistent_product(self):
        """Testa atualização da quantidade de um produto inexistente"""
        inventory = InventorySystem()
        result = inventory.update_quantity(999, 5)
        assert result is False

    def test_list_available_products(self):
        """Testa listagem de produtos disponíveis"""
        inventory = InventorySystem()
        product1 = Product(1, "Test Product 1", 19.99, 10)
        product2 = Product(2, "Test Product 2", 29.99, 0)
        product3 = Product(3, "Test Product 3", 39.99, 5)
        
        inventory.add_product(product1)
        inventory.add_product(product2)
        inventory.add_product(product3)
        
        available_products = inventory.list_available_products()
        assert len(available_products) == 2
        assert product1 in available_products
        assert product2 not in available_products
        assert product3 in available_products

    def test_get_total_value(self):
        """Testa cálculo do valor total do inventário"""
        inventory = InventorySystem()
        product1 = Product(1, "Test Product 1", 10.00, 5)
        product2 = Product(2, "Test Product 2", 20.00, 3)
        product3 = Product(3, "Test Product 3", 15.00, 2)
        
        inventory.add_product(product1)
        inventory.add_product(product2)
        inventory.add_product(product3)
        
        total_value = inventory.get_total_value()
        assert total_value == 140.00