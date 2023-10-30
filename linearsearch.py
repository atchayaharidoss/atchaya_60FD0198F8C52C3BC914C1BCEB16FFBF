def linearSearchProduct(productList, targetProduct):
    indices =  [] 
    for index, product in enumerate(productList):
        if product == targetProduct:
            indices.append(index)
    return indices

productList = ["shoes", "boot", "loafer", "shoes"] 
targetProduct1 = "shoes"
targetProduct2 = 'apple'

result1 = linearSearchProduct(productList, targetProduct1)
print(result1)

result2 = linearSearchProduct(productList, targetProduct2)
print(result2)