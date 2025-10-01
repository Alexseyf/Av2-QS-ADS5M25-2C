class Product:
    def __init__(self, id, name, price, quantity=0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def is_available(self):
        """Verifica se o produto está disponível em estoque"""
        return self.quantity > 0
    
    def validate(self):
        """Valida se o produto tem informações válidas"""
        if not self.id or not self.name:
            return False
        
        if self.price < 0:
            return False
        
        if self.quantity < 0:
            return False
        
        return True


class Inventory:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        """Adiciona um produto ao inventário"""
        if not product.validate():
            return False
        
        if product.id in self.products:
            return False
        
        self.products[product.id] = product
        return True
    
    def remove_product(self, product_id):
        """Remove um produto do inventário"""
        if product_id not in self.products:
            return False
        
        del self.products[product_id]
        return True
    
    def get_product(self, product_id):
        """Obtém um produto pelo ID"""
        return self.products.get(product_id)
    
    def update_quantity(self, product_id, quantity):
        """Atualiza a quantidade de um produto"""
        product = self.get_product(product_id)
        if not product:
            return False
        
        new_quantity = product.quantity + quantity
        
        if new_quantity < 0:
            return False
        
        product.quantity = new_quantity
        return True
    
    def list_available_products(self):
        """Lista todos os produtos disponíveis"""
        return [p for p in self.products.values() if p.is_available()]
    
    def get_total_value(self):
        """Calcula o valor total do inventário"""
        return sum(p.price * p.quantity for p in self.products.values())
