
backPack = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    print('Inventory:')
    totalItems = 0
    for k, v in inventory.items():
        print(str(v), k)
        totalItems += v
    print('Total number of items: ' + str(totalItems))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
        
displayInventory(backPack)
addToInventory(backPack, loot)
displayInventory(backPack)


