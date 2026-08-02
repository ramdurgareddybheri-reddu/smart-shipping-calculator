def shipping_cost():
    distance=int(input("Enter the distance in kilometers: "))
    package_weight=int(input("Enter the package weight in kilograms: "))
    item=input("GLASSITEM (G) PLASTICITEM (PL) WOOD(WD) PAPERITEM (PI) IRONITEM (IT) ")
    if item.upper()=="G":
        shipping_cost=distance*package_weight*0.25
        return shipping_cost
    elif item.upper()=="PL":
        shipping_cost=distance*package_weight*0.10
        return shipping_cost
    elif item.upper()=="WOD":
        shipping_cost=distance*package_weight*0.55
        return shipping_cost
    elif item.upper()=="PI":
        shipping_cost=distance*package_weight*0.0520
        return shipping_cost
    elif item.upper()=="IT":
        shipping_cost=distance*package_weight*0.90
        return shipping_cost
    else:
        print("Please enter a valid item")




cost=shipping_cost()
print("shipping cost is:${0:.2f}".format(cost))