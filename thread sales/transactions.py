#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1,2
daily_sales = """Edith Mcbride   ;,;$1.21   ;,;   white ;,; 09/15/17   , Myrtle Morris ;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

daily_sales_replaced = daily_sales.split(';,;', '+')
#print(daily_sales_replaced)

Edith Mcbride   +$1.21   +   white + 
09/15/17   , Myrtle Morris 
+   $22.66   + green&white&blue+09/15/17


#3,4
daily_transactions = daily_sales_replaced.split(',')
# print(daily_transactions)

#['Edith Mcbride   +$1.21   +   white + \n09/15/17   ',' Myrtle Morris \n+   $22.66   + green&white&blue+09/15/17']


#5,6,7
daily_transactions_split = []

for transaction in daily_transactions:
	daily_transactions_split.append(transaction.split('+'))
# print(daily_transactions_split)


#[['Edith Mcbride   ', '$1.21   ', '   white ', ' \n09/15/17   '], [' Myrtle Morris \n', '   $22.66   ', ' green&white&blue', '09/15/17']]


#8,9

transactions_clean= []
for transaction in daily_transactions_split:
  transaction_clean= []
  for data_point in transaction:
    transaction_clean.append(data_point.replace("\n", "").strip(" "))
    transactions_clean.append(transaction_clean)

# print(transactions_clean)



#[['Edith Mcbride', '$1.21', 'white', '09/15/17'],['Myrtle Morris', '$22.66', 'green&white&blue', '09/15/17']]


# #10
customers = []
sales = [] 
thread_sold = []


# #11,12
for transaction in transactions_clean:
	customers.append(transaction[0])
	sales.append(transaction[1])
	thread_sold.append(transaction[2])
# print(customers)
# print(sales)
# print(thread_sold)


#['Edith Mcbride', 'Myrtle Morris']

#['$1.21', '$22.66']

#['white','green&white&blue']



#13, 14, 15
total_sales = 0
for sale in sales:
	total_sales += float(sale.strip('$'))
# print(total_sales)
	
#5994.9599999999955


#16
# print(thread_sold)

#['white','green&white&blue']


#17, 18
thread_sold_split = []

for sale in thread_sold:
	for color in sale.split("&")
		thread_sold.split.append(color)
# print(thread_sold_split)


#['white','white', 'blue', 'green', 'white', 'blue', 'green', 'white', 'blue', 'green', 'white', 'blue', 'green', 'white', 'blue', 'green', 'white', 'blue', 'green', 'white', 'blue']
	

#19,20
def color_count(color):
  color_total = 0
  for thread_color in thread_sold_split:
    if color == thread_color:
      color_total += 1
  return color_total

# print(color_count('white'))

#returns 112


#21,22
colors = ['red','yellow','green','white','black','blue','purple']

for color in colors:
  #print("Thread Shed sold {0} threads of {1} thread today".format(color_count(color), color))


# Thread Shed sold 96 threads of red thread today
# Thread Shed sold 136 threads of yellow thread today
# Thread Shed sold 120 threads of green thread today
# Thread Shed sold 112 threads of white thread today
# Thread Shed sold 104 threads of black thread today
# Thread Shed sold 88 threads of blue thread today
# Thread Shed sold 68 threads of purple thread today

