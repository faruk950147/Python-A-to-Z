def discount_offer(discount):
    def final_price(price):
        return price - discount
    return final_price
