def init_app(val): # converter um valor monetario em float para moeda brl
    a = '{:,.2f}'.format(float(val))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')
