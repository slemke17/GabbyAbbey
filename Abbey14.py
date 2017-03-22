results = input('initial value-->')
n = input('first argument-->')
results = eval("%s%s" % (results,n))

while '%' not in ("%s%s" % (results, n)):
    n = input('next argument-->')
    results = eval("%s%s" % (results, n))
    print(results)
