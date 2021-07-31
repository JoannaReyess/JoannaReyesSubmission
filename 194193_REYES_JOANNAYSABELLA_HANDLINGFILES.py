products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

def get_property(code,property):
    return products[code][property]

def main():
    total=0
    subtotal=0
    order_summary={}
    with open ("receipt.txt","w+") as r:
        r.write('''
    ==
    CODE\t\t\t\t\t\tNAME\t\t\t\t\t\tQUANTITY\t\t\t\t\t\tSUBTOTAL''' + "\n")
        
    while True:
        order= input("product_code,quantity: ")
        if order == "/":
            break
            
        sep= order.split(",")
        if sep[0] in order_summary.keys():
            order_summary[sep[0]] += int(sep[1])
        else:
            order_summary.setdefault(sep[0],int(sep[1]))    
    
    sorted_order= dict(sorted(order_summary.items(),key=lambda item:item[0]))  
    
    for i in sorted_order:
        code= i
        name= get_property(code,"name")
        quantity=sorted_order[i]
        subtotal= get_property(code,"price")*quantity
        total+=subtotal
        with open("receipt.txt","a+") as r:
                r.write(f"\t{code}\t\t\t\t\t{name}\t\t\t\t\t\t{quantity}\t\t\t\t\t\t\t{subtotal}" + "\n")
                
    with open("receipt.txt","a+") as r:
        r.write(f'''
    Total:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{total}
    ==''' + "\n")    
        
main()