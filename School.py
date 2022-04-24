import statistics
print('BIENVENUE ')

while True:
    nb = input("Nombre d'étudiant: ")
    try:
        nb = int(nb)
        break
    except ValueError:
        print('Valeur incorrecte! ')
    notes = input("Nombre de notes: ")
    try:
        notes = int(notes)
        break
    except  ValueError:
        print('Valeur incorrecte! ')

liste_note = []
liste_moyenne = []
bank = {}
liste_bank = []
for i in range(0, nb):
    total = 0
    nom = input("Entrez le nom d'un étudiant: ")
    pnom = input("Entrez son prénom: ")
    while True:
        age = input('Entrez son âge: ')
        try:
            age = int(age)
            if 0 < age <= 100:
                break
            else:
                print('Valeur incorrecte! ')
        except ValueError:
            print('Valeur incorrecte! ')
    iden = '{} {} ({}ans)'.format(nom, pnom, age)
    for i in range(0, notes):
        while True:
            note = input('Entrez la note: ')
            try:
                note = int(note)
                if 0 < note <= 20:
                    total += note
                    break
                else:
                    print('Valeur incorrecte! ')
            except ValueError:
                print('Valeur incorrecte! ')
            liste_note.append(note)
            j = input('Saisissez le jour de la compo: ')
            try:
                j = int(j)
                if 0 < j <= 31:
                    break
                else:
                    print('Valeur incorrecte!')
            except ValueError:
                print('Valeur incorrecte! ')
            m = input('Entrez le mois: ')
            try:
                m = int(m)
                if 0 < m <= 12:
                    break
                else:
                    print('Valeur incorrecte! ')
            except ValueError:
                print('Valeur incorrecte! ')
            a = input("Entrez l'année: ")
            try:
                a = int(a)
                if 1990 < a <= 2030:
                    break
                else:
                    print('Valeur non prise en charge! ')
            except ValueError:
                print('Valeur incorrecte!')
        date_note = 'Nom et prénom: ' + iden + 'Note: ' + note + ', Date : {}/{}/{}'.format(j, m, a)
    moyenne = total/notes
    liste_moyenne.append(moyenne)
    moyen = 'Moyenne: {}'.format(moyenne)
    bank.update({iden:moyen})

liste_bank.append(bank)
liste_moyenne.sort()
print(liste_bank)
print(date_note)
print('Moyenne minimale: ', liste_moyenne[0], ', Moyenne maximale: ', liste_moyenne[-1])
print('Notes de la classe: {}'.format(liste_note))
mediane = print('La médiane de la classe est ', statistics.median(liste_note))
        
            
    
