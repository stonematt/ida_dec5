# import codecademylib
import pandas as pd

visits = pd.read_csv('myfiles/d11-visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('myfiles/d11-cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('myfiles/d11-checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('myfiles/d11-purchase.csv',
                       parse_dates=[1])

#print visits.head(2)
#print cart.head(2)
#print checkout.head(2)
#print purchase.head(2)


#left join visits to carts and count result
v_to_cart = pd.merge(visits, cart, how='left')
visit_count = len(v_to_cart)
print "visitors: ", visit_count


#count the number of records w/ null in cart_time
no_cart=len(v_to_cart[v_to_cart.cart_time.isnull()])
print "didn't add to cart: ", no_cart

#what percent of visistor didn't put something in their cart
no_shoppers = float(no_cart) / visit_count
print 'percent not shopping: ', no_shoppers

# left merg from cart to checkout and count shoppers who didn't buy.
cart_to_checkout = cart.merge(checkout, how='left')
shopper_count = len(cart_to_checkout)
print 'shoppers: ', shopper_count
no_checkout = len(cart_to_checkout[cart_to_checkout.checkout_time.isnull()])
print 'didn\'t checkout: ', no_checkout
percent_no_checkout = no_checkout / float(shopper_count)
print "percent no checkout: " , percent_no_checkout

# merge all four datasets into a single dataframe w/ left join.
all_data = visits.merge(cart, how='left')\
						.merge(checkout, how='left')\
  					.merge(purchase, how='left')

#print all_data.head(10)

#calculate % conversion on each step
visits = float(len(all_data))
#cart
to_cart = float(len(all_data[~all_data.cart_time.isnull()]))
#checkout
to_checkout = float(len(all_data[~all_data.checkout_time.isnull()]))
#purchase
to_purchase = float(len(all_data[~all_data.purchase_time.isnull()]))

#calulate dropout steps in funnel
percent_to_cart = (to_cart / visits *100)
percent_to_checkout =to_checkout / visits *100
percent_to_purchase =to_purchase / visits *100

print 'summary conversion'
print 'visit to cart: %0.2f%% proceed, %0.2f%% dropout' % (percent_to_cart, 100 - percent_to_cart)
print 'visit to checkout: %0.2f%%, %0.2f%% total dropout' % (percent_to_checkout, 100 - percent_to_checkout)
print 'visit to purchase: %0.2f%%, %0.2f%% total dropout' % (percent_to_purchase, 100 - percent_to_purchase)
print ''
print 'another way to think about it...'
print 'progressive conversions'
print 'visit but no cart: %0.2f%%' % ((1 - (to_cart / visits)) *100)
print 'cart but no checkout: %0.2f%%' % ((1 - to_checkout / to_cart) *100)
print 'checkout but no purchase: %0.2f%%' % ((1 - to_purchase / to_checkout) *100)


# calculate time on site between initial visit to purchase
all_data['time_to_purchase'] = all_data['purchase_time'] - all_data['visit_time']

print 'average time to purchase: ', all_data.time_to_purchase.mean() 

