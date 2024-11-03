import json
with open('menu.json', 'r') as f:
    data = json.load(f)

items = data.get('items', [])
while True:
    print('-'*40)
    print(' OUR CGEC Restaurant')
    print('-'*40)
    print('1. Show Menu')
    print('2. Order Items')
    print('3. Add Item')
    print('4. Add Review')
    print('5. Exit')
    print('-'*40)
    choice = int(input())
    if choice == 1:
       print('-'*40)
       print('ID\tName\t\tPrice')
       print('-'*40)
       for item in items:
           print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
           print('-'*40)
    elif choice == 2:
           order_item = list(map(int,input('what you want t to try today? ').split(',')))
           print('-'*40)
           print('ID\tName\t\tPrice')
           print('-'*40) 
           total_bill = 0   
           for order_item in order_item:
               for item in items:
                   if item['id'] == order_item:   
                    print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}') 
                    total_bill = total_bill + int(item.get('price', 10))  
                    break
           print('-'*40)
           print(f'\t Total Amount: {total_bill}')
           print('-'*40)       
           print('Total Amount:', item.get("price")) 
    elif choice == 3: 
         name = input('Enter item name: ')
         item_price =  int(input('Enter the price: ')) 
         item_type = input('veg or non-veg: ')
         items.append({
             "id": len(items)  + 1,
              'name' : name,
              'price': item_price,
              'veg': True if item_type == 'veg' else False,
              'reviews': []
         }) 
         data['items'] = items
         with open('menu.json', 'w') as f:
              json.dump(data, f)
         print('Item is added.')           
    elif choice == 4:  
         print('Add review')  
    else:
         print('Thank You')     
         break