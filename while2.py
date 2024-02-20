foodlist = [
    'cabbage', 'cake', 'carrots', 'carne asada', 'celery', 
    'cheese', 'chicken', 'catfish', 'chips', 'chocolate', 
    'coffee', 'cookies', 'corn', 'cupcakes', 'crab', 'curry', 
    'cereal', 'chimichanga'
]
foods = []
i = input()
while i in foodlist and i!='q':
    foods.append(i)
    print("Press 'q' to quit")
    i = input("Enter a food: ")
    
print(foods)