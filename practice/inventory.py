## Fantasy Game Inventory
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inv):
    print('Inventory: ')
    ## Iterate through the dictionary of inv
    ## print the value / key for each item
    for k, v in inv.items():
        print(v, k)
    ## print the total of inv using sum to return total of all values combined
    print('Total number of items: ' +str(sum(inv.values())))

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    ## Iterate through dragonLoot list
    ## For each item, either add 1 to existing value
    ## Otherwise create a key/value pair if it doesn't exist
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
        
displayInventory(inv)
addToInventory(inv, dragonLoot)
displayInventory(inv)