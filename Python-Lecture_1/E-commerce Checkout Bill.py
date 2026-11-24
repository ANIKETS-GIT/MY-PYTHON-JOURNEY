# E-commerce Checkout Bill
# Given price = 1299.50, quantity = 3, discount_percent = 15, and GST of 18% applied after discount. 
# Calculate the subtotal, discount amount, GST amount and final payable amount. 
# Also print a boolean free_delivery that is True if the final amount is above 2000.

given_price = 1299.50
quantity = 3
discount_percent = 15
gst_percent = 18

sub_total = given_price * quantity
discount_amount = discount_percent/100 * sub_total
after_discount_amount = sub_total - discount_amount
gst_amount = gst_percent/100 * after_discount_amount
final_payable_amount = sub_total - discount_amount + gst_amount

print("sub_total : ",sub_total)
print("discount_amount : ", discount_amount)
print("gst_amount : ", gst_amount)
print("final_payable_amount : ", final_payable_amount )
print("free_delivery : ", final_payable_amount > 2000)




