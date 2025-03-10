class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        """Ürün ekleme metodu"""
        if product.update_stock(quantity):  
            if product.name in self.items:
                self.items[product.name]['quantity'] += quantity
            else:
                self.items[product.name] = {'product': product, 'quantity': quantity}
        else:
            print(f"Yetersiz stok: {product.name}")

    def remove_product(self, product_name):
        """Ürün çıkarma metodu"""
        if product_name in self.items:
            product = self.items[product_name]['product']
            quantity = self.items[product_name]['quantity']
            product.stock += quantity  
            del self.items[product_name]
            print(f"{product_name} ürünü sepetten çıkarıldı.")
        else:
            print("Bu ürün sepetinizde bulunmamaktadır.")

    def display_cart(self):       
        if not self.items:
            print("Sepetiniz şu an boş.")
            return
        
        print("\nSepetinizdeki Ürünler:")
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            total_price = product.price * quantity
            print(f"- {product.name}: {quantity} adet | {total_price} TL")

    def get_total(self):      
        return sum(item['product'].price * item['quantity'] for item in self.items.values())
