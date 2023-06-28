
#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}
#add purse
purse = 1000
cart_total = 0
#create an empty shopping cart
cart = {}
#loop through stores/dicts
stores = [freelancers, antiques, pet_shop]

for shop in (freelancers, antiques, pet_shop):
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f'Welcome to {(shop["name"])}! What do you want to buy: {shop}').lower()
    #escape clause
    if buy_item in shop:
        #update the cart
        cart.update({buy_item:shop.pop(buy_item)}) # use pop...

        cart_total = cart_total + buy_item.get(buy_item)
        buy_items = ", ".join(list(cart.keys()))
    else:
        continue
print("Total cost: " + cart_total)    
print(f'You Purchased {buy_items}. You have ' + purse + ' remaining. Have a nice day of mayhem!')