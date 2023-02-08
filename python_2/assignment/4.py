'''dictionary comprehension'''

def dollar_to_rupee():
    """"create a new dictionary"""
    price={'Laptop':10,'mobile':5,'watch':3,'keyword':1}
    """multipliyed the price and convert to rupee
    convert to rupee=one dolaar convert to indian rupee"""
    convert_to_ruppe=81.38
    n_price={i: j*convert_to_ruppe for (i,j) in price.items()}
    return n_price
rc=dollar_to_rupee()
print(rc)