def display_invoice_total(price, quantity):
    total = price * quantity
    print(f"Total: {total}")


price = int(input())
quantity = int(input())
display_invoice_total(price, quantity)