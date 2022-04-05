
def produit(n, m):
    i = 1
    res = 0
    while i <= n:
        res = res + m 
        i += 1
    print(res)


produit(3, 2)

# --- OU ---

def produit(n, m):
    res = 0
    for i in range(0, m):
        res += n
    print('Le résultat du produit de', str(n), 'et', str(m), 'est', str(res))


a = int(input('Entrez le premier nombre SVP: '))
b = int(input('Entrez le second SVP: '))


produit(a, b)
