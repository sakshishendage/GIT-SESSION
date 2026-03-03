import re
def validate_isbn(isbn):
    pattern = r'^\d{5}$'
    return re.match(pattern, isbn) is not None
def validate_price(price):
    try:
        price = float(price)
        if price >= 0:
            return True
        else:
            return False
    except:
        return False
