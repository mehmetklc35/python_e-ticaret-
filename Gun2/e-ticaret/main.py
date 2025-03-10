from product import Product
from cart import Cart
from customer import Customer
from order import Order

def main():
    print("\n🔹 Hoş Geldiniz! Alışveriş Sepeti Uygulaması 🔹")
    name = input("Adınızı girin: ")
    email = input("E-posta adresinizi girin: ")
    customer = Customer(name, email)
    cart = Cart()
    
    products = {
        "Telefon": Product("Telefon", 15000, 10),
        "Laptop": Product("Laptop", 25000, 5),
        "Kulaklık": Product("Kulaklık", 2000, 15),
        "Saat": Product("Saat", 5000, 7)
    }

    while True:
        print("\nYapmak İstediğiniz İşlemi Seçiniz:")
        print("1. Ürün ekle")
        print("2. Ürün çıkar")
        print("3. Sepeti görüntüle")
        print("4. Siparişi Tamamla")
        print("5. Çıkış")

        choice = input("Seçiminizi yapın (1-5): ")

        if choice == "1":
            print("\nMevcut Ürünler:")
            for product_name, product in products.items():
                print(f"- {product}")
            
            product_name = input("Sepete eklemek istediğiniz ürünün adını girin: ")
            if product_name in products:
                try:
                    quantity = int(input("Kaç adet eklemek istiyorsunuz? "))
                    cart.add_product(products[product_name], quantity)
                except ValueError:
                    print("Hata! Lütfen geçerli bir sayı girin.")
            else:
                print("Bu ürün mevcut değil.")

        elif choice == "2":
            product_name = input("Sepetten çıkarmak istediğiniz ürünün adını girin: ")
            cart.remove_product(product_name)

        elif choice == "3":
            print("\n🔹 Sepetinizdeki Ürünler 🔹")
            cart.display_cart()
            print(f"Toplam Tutar: {cart.get_total()} TL")

        elif choice == "4":
            total = cart.get_total()
            if total == 0:
                print("Sepetiniz boş, sipariş veremezsiniz!")
            else:
                order = Order(customer, cart)
                order.place_order()
                cart.items.clear()  
                print("\n✅ Sipariş tamamlandı! Teşekkür ederiz.")

        elif choice == "5":
            print("Çıkış yapılıyor... İyi günler dileriz!")
            break
        
        else:
            print("Geçersiz giriş! Lütfen 1-5 arasında bir sayı girin.")

if __name__ == "__main__":
    main()
