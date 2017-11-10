# class ShoppingCart(object):
#     def __init__(self):
#         self.total = 0
#         self.items = {}
#     def add_item(self,item_name,quantity,price):
#         self.cost = quantity*price
#         self.total += self.cost
#         self.items[item_name] = quantity
#     def remove_item(self,item_name,quantity,price):
#         self.cost = quantity*price
#         self.total -= self.cost
#         del self.items[item_name]
#         if quantity > len(self.items):
#             self.items = {}
            
#     def checkout(self,cash_paid):
#         if cash_paid > self.total:
#             self.balance = cash_paid - self.total
#             return self.balance
#         else:
#             return "Cash paid not enough"
        
# class Shop(ShoppingCart):
#     def __init__(self):
#         self.quantity = 100
#     def remove_item(self):
#         self.quantity -= 1


# def remove_duplicates(word):
# 	n_word = []
# 	for i in word:
# 		if i not in n_word:
# 			n_word.append(i)
# 	f_word = "".join(sorted(n_word))
# 	n_len = len(word) - len(f_word)

# 	return f_word,n_len

# print (remove_duplicates("thelexash"))

# def my_sort(nums):
# 	new,new1 = [],[]
# 	for i in nums:
# 		if i%2 != 0:
# 			new.append(i)
#             new = sorted(new)
# 	for n in  nums:
# 		if n%2 == 0:
# 			new1.append(n)
#             new1 = sorted(new1)

# 	return new.extend(new1)
# print(my_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def power(a,b):
	ans = 1
	if b == 2:
		return b*b
	elif b == 0:
		return 1
	elif b == 1:
		return a
	else:
		for i in range(b):
			ans *=a
		return ans

print (power(2,9))
