#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

#create empty shopping cart
cart = {}

for shop in (freelancers, antiques, pet_shop):
    #input box to show what you can buy
    buy_item = input(f'Welcome to {shop["name"]}!  What do you want to buy: {shop}').lower()
    #update cart
    cart.update({buy_item:shop.pop(buy_item)}) #use pop
buy_items = ", ".join(list(cart.keys()))
print(f'You Purchased {buy_items}. Today it is all free. Have a nice day of mayhem!')
