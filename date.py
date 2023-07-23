"""
Créé le Ve 03/02/2023 à 01:11
Auteur : Nate
date.py
"""

class Date :
    
    """
    Cette classe définit des dates en jours (int de 1 à 31, fonction du mois), mois (int de 1 à 12) et année (int positif).
    L'utilisation d'années négatives est possible mais n'est pas actuellement prise en charge de manière fiable.
    
    Méthodes :
        ¤ Edition de l'objet :
        __init__                                                                            (ok)- init(date) - cas générique (sans année) - annee < 0 -
        __repr__                                                                            (ok)
        ¤ Méthodes de conteneur :
        __getitem__                                                                         (ok)
        __setitem__                                                                         (ok)
        __delitem__                                                                         (ok)
        ¤ Opérateurs mathématiques : (conversions nécessaires)
        __add__
        __sub__
        __mul__
        __truediv__ (?)
        __floordiv__
        __mod__
        ¤ Opérateurs inversés :
        __rmul__ (?)
        ¤ Opérateurs de comparaison :
        __eq__
        __gt__
        __ge__
        ¤ Autres :
        to_a                                                                                (ok)
        to_m                                                                                (ok)
        to_j                                                                                (ok) (avc j act : pb de compatibilité avc duree ?)
        to_int                                                                              (ok) -intérêt spécial : annee < 0 : à voir
        nb_jours_en_cours                                                                   (ok)
    
    Fonctions annexes (?)
        validite_annee                                                                      (ok)
        validite_mois                                                                       (ok)
        validite_jour                                                                       (ok)
        bissextile                                                                          (ok)
        nb_annees_bis                                                                       (ok)
        to_j_greg                                                                           (ok)
        to_a_greg                                                                           (ok) complexité : raccourcir le calcul : à priori ok
        nb_mois_dans_annee                                                                  (ok) modif comment, gros test ?, amel ? à priori ok
        from_a                                                                              (ok)
        from_m                                                                              (ok)
        from_j                                                                              (en cours)
    
    idées :
        _ en cours : validité des données (années ? / jours à refaire)
        _ ok : année bissextile
        _ init(j,m,a) + méthodes :
            - ok : affichage
            - ok : conteneur
            - mathématiques
            - math inv
            - comparaison
            (- autres)
        _ ok : to_j/m/a/int (int positif d'abord)
        _ from_j/m/a/int (int positifs)
        _ méthode bissext ?
        _ format d'affichage (variable globale qui règle le mode d'affichage ?)
        _ conversion en chiffres romains ? (programme à part ?)
        _ mul float ?
        _ numéro semaine ?
        _ jour de la semaine ?
        _ fusionner les longueurs mois ?
        (cf programme algobox...)
    remarques :
        _ self.to_j : faut-il plutôt considérer le nombre de jours révolus ?
        _ to_j_greg : return float ? (/400 ou pas?) / complexité ?
    """
    
    
    
    
    
    ## Attributs de classe
    
    
    
    
    
    longueurs_mois = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    longueurs_mois_bis = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) # à fusionner ?
    
    
    
    
    
    ## Edition de l'objet
    
    
    
    
    
    def __init__ (self, j, m, a) :
        """
        Constructeur de Date à partir d'un nombre entier de jours (j), de mois (m) et d'années (a).
        """
        validite_mois(m)
        validite_jour(j, m, bissextile(a))
        self.jour = j
        self.mois = m
        self.annee = a
    
    
    
    def __repr__ (self) :
        """
        Méthode d'affichage d'une Date.
        """
        aff_j = ""
        aff_m = ""
        sep = "/"
        if self.jour <= 9 :
            aff_j += "0"
        if self.mois <= 9 :
            aff_m += "0"
        aff_j += str(self.jour)
        aff_m += str(self.mois)
        return aff_j + sep + aff_m + sep + str(self.annee)
    
    
    
    
    
    ## Méthodes de conteneur
    
    
    
    
    
    def __getitem__ (self, ind) :
        """
        Méthode d'indexation en lecture. Permet de récupérer les valeurs avec les indices "j", "m" et "a".
        """
        if ind == "j" :
            return self.jour
        elif ind == "m" :
            return self.mois
        elif ind == "a" :
            return self.annee
        else :
            raise ValueError("Valeur de l'indice invalide. Valeur : " + str(ind))
    
    
    
    def __setitem__ (self, ind, val) :
        """
        Méthode d'indexation en écriture. Permet de modifier les valeurs avec les indices "j", "m" et "a" et des valeurs adéquates.
        """
        if ind == "j" :
            validite_jour(val, self.mois, bissextile(self.annee))
            self.jour = val
        elif ind == "m" :
            validite_mois(val)
            self.mois = val
        elif ind == "a" :
            if type(val) != int :
                raise TypeError("L'année n'est pas de type int. Type : " + str(type(val)))
            self.annee = val
        else :
            raise ValueError("Valeur de l'indice invalide. Valeur : " + str(ind))
    
    
    
    def __delitem__ (self, ind) :
        """
        Méthode de suppression d'attribut (lève une exception).
        """
        raise AttributeError("Suppression d'un attribut impossible.")
    
    
    
    
    
    ## Opérateurs mathématiques
    
    
    
    
    
    ## Opérateurs inversés
    
    
    
    
    
    ## Opérateurs de comparaison
    
    
    
    
    
    ## Autres
    
    
    
    
    
    def to_a (self) :
        """
        Renvoie le nombre d'années révolues comprises dans la Date.
        """
        return self.annee
    
    
    
    def to_m (self) :
        """
        Renvoie le nombre de mois révolus compris dans la Date.
        """
        return self.to_a() * 12 + self.mois - 1
    
    
    
    def to_j (self) :
        """
        Renvoie le nombre de jours compris dans la Date (jour actuel compris).
        """
        b = nb_annees_bis(self.annee)
        return b * 366 + (self.annee - b) * 365 + self.nb_jours_en_cours()
    
    
    
    def to_int (self) :
        """
        Transforme la Date en nombre entier.
        """
        return self.to_j()
    
    
    
    def nb_jours_en_cours (self) :
        """
        Renvoie le nombre de jours écoulés depuis le début de l'année en cours (jour actuel inclu).
        """
        cpt = 0
        for m in range(self.mois - 1) :
            cpt += Date.longueurs_mois[m]
        if bissextile(self.annee) and self.mois > 2 :
            cpt += 1
        cpt += self.jour
        return cpt
    
    
    
    
    
## Fonctions annexes





def validite_annee (a) :
    """
    Vérifie la validité d'un identificateur d'année (int, positif dans un premier temps).
    
    Paramètre : a : identificateur d'année.
    Valeur de retour : aucune.
    Exceptions : TypeError, ValueError.
    """
    if type(a) != int :
        raise TypeError("L'identificateur d'année n'est pas de type int. type : " + str(type(a)))
    if a < 0 :
        raise ValueError("Année négative !")



def validite_mois (m) :
    """
    Vérifie la validité d'un identificateur de mois (int entre 1 et 12).
    
    Paramètre : m : identificateur de mois.
    Valeur de retour : aucune.
    Exceptions : TypeError, ValueError.
    """
    if type(m) != int :
        raise TypeError("L'identificateur de mois n'est pas de type int. type : " + str(type(m)))
    if m < 1 or m > 12 :
        raise ValueError("L'identificateur de mois a une valeur invalide. valeur : " + str(m))



def validite_jour (j, m, a) :
    """
    Vérifie la validité d'un identificateur de jour (int entre 1 et 28/29/30/31) en fonction du mois et de l'année.
    
    Paramètres : j : identificateur de jour / m : identificateur de mois / a : identificateur d'année.
    Valeur de retour : aucune.
    Exceptions : TypeError, ValueError.
    """
    validite_annee(a)
    validite_mois(m)
    est_bis = bissextile(a)
    if est_bis :
        longueurs = Date.longueurs_mois_bis
    else :
        longueurs = Date.longueurs_mois
    if type(j) != int :
        raise TypeError("L'identificateur de jour n'est pas de type int. type : " + str(type(j)))
    if j < 1 or j > 31 :
        raise ValueError("L'identificateur de jour a une valeur invalide. valeur : " + str(j))
    if j > longueurs[m-1] :
        raise ValueError("L'identificateur de jour a une valeur invalide pour le mois courrant. valeur : " + str(j) + " (mois:" + str(m) + ", année:" + str(a) + ").")



def bissextile (annee) :
    """
    Calcule le caractère bissextile d'une année et renvoie le booléen correspondant.
    
    Paramètre : annee : l'année à tester (int)
    Valeur de retour : booléen décrivant le caractère bissextile.
    """
    #if annee % 4 != 0 :
    #    return False
    #if annee % 100 == 0 and annee % 400 != 0 :
    #    return False
    #return True
    if annee % 400 == 0 :
        return True
    if annee % 100 == 0 :
        return False
    if annee % 4 == 0 :
        return True
    return False



def nb_annees_bis (annee) :
    """
    Compte le nombre d'années bissextiles depuis l'an 0 jusqu'à annee exclue (années positives uniquement !).
    """
    cpt = 0
    for k in range(annee) :
        if bissextile(k) :
            cpt += 1
    return cpt



def to_j_greg (annee) :
    """
    Renvoie le nombre de jours correspondant à un nombre d'année(s) de type arbitraire dans le calendrier grégorien (indépendamment de la bissextilité).
    
    /!\ Faut-il return  nbj_400 * annee pour rester sur des int ???
    """
    nbab_400 = nb_annees_bis(400)                       # calcul du nombre d'années bissextiles dans 400 ans
    nbj_400 = nbab_400 * 366 + (400 - nbab_400) * 365   # calcul du nombre de jours dans 400 ans
    nbj = nbj_400 / 400                                 # calcul du nombre de jours moyen dans 1 an
    return nbj * annee                                  # calcul du nombre de jours moyen sur la durée voulue



def to_a_greg (jour) :
    """
    Renvoie le nombre d'année(s) de type arbitraire correspondant à un nombre de jours dans le calendrier grégorien (indépendamment de la bissextilité).
    """
    nbab_400 = nb_annees_bis(400)                       # calcul du nombre d'années bissextiles dans 400 ans
    nbj_400 = nbab_400 * 366 + (400 - nbab_400) * 365   # calcul du nombre de jours dans 400 ans
    nba = 400 / nbj_400                                 # calcul du nombre d'année(s) dans 1 jour
    return nba * jour                                   # calcul du nombre d'années sur la durée voulue
"""
nbj400 : nb de jours en 400 ans (nbj400 jours = 400 ans)
nba1 ans = 1 jour = 1 jour * nbj400 jours / nbj400 jours = nbj400 jours / nbj400 jours = 400 ans / nbj400 jours
"""



def nb_mois_dans_annee (jours, isbis = False) :
    """
    Renvoie un tuple de deux nombres qui sont :
     _ le nombre de mois complètement écoulés dans l'année en cours (entier dans 0 - 11).
     _ le nombre de jours restants dans le mois en cours.
    jours : nombre de jours correspondant (dans 1 - 365 / 366 selon la bissextilité)
    isbis : booléen décrivant le caractère bissextile
    L'algorithme est censé terminer au cours de la boucle, la dernière exception n'est JAMAIS censée être levée.
    /!\ approximation de to_a_greg possible... considérer des jours négatifs ? kézako ?
    """
    if isbis :
        tup = Date.longueurs_mois_bis
        if jours not in range(1,367) :
            raise ValueError("Cette méthode ne fonctionne que pour une année en cours. (jours : " + str(jours) + ")")
    else :
        tup = Date.longueurs_mois
        if jours not in range(1,366) :
            raise ValueError("Cette méthode ne fonctionne que pour une année en cours. (jours : " + str(jours) + ")")
    cpt = 0
    reste = jours
    for k in range(1,13) :
        cpt += tup[k-1]
        if jours <= cpt :
            return k-1, reste
        reste -= tup[k-1]
    raise ValueError("Cette exception n'est pas censée être levée !!! (trop de jours considérés ?)")



def from_a (annee) :
    """
    Convertit un nombre d'années positif en Date.
    La Date correspond au 1er de l'année demandée.
    """
    if type(annee) != int :
        raise TypeError("Construction de Date impossible à partir de " + str(type(annee)) + ".")
    if annee < 0 :
        raise ValueError("Date négative.")
    return Date(1, 1, annee)



def from_m (mois) :
    """
    Convertit un nombre de mois positif en Date.
    Le nombre de mois correspond au nombre de mois révolus écoulés. La Date renvoyée correspond au 1er du mois suivant.
    (exemple : 1er février pour 1)
    """
    if type(mois) != int :
        raise TypeError("Construction de Date impossible à partir de " + str(type(mois)) + ".")
    if mois < 0 :
        raise ValueError("Date négative / nulle.")
    return Date(1, ((mois) % 12) + 1, (mois) // 12)



def from_j (jours) :
    """
    pb probablement exclusif du 366 !
    pb réglé à priori
    A tester ! -> pour un jour quelconque -> pour le 01/01 -> pour le 31/12
    
    
    aprox_an = int(to_a_greg(jours)) # dernier jour de l'année toujours arrondi à l'année supérieure !
    nb_bis = nb_annees_bis(aprox_an)
    nb_j = nb_bis * 366 + (aprox_an - nb_bis) * 365
    nbj_restant = jours - nb_j
    if nbj_restant == 0 :
        nbj_restant += 366 #bug si non bis
        aprox_an -= 1
    mois, nbj_dans_mois = nb_mois_dans_annee(nbj_restant, bissextile(aprox_an))
    """
    
    nbab400 = nb_annees_bis(400)                        # nombre d'années bissextiles en 400 ans (0-399) = 97
    nbj400 = nbab400 * 366 + (400 - nbab400) * 365      # nombre de jours en 400 ans = 146097
    a = (jours // nbj400) * 400                         # nombre de cycles de 400 ans écoulés
    restej = jours % nbj400                             # nombre de jours à parcourir dans le dernier cycle de 400 ans incomplet
    if restej > 366 :                                       # parcours complet de l'année 0 du cycle ?
        a += 1
        restej -= 366
    nbab99 = nb_annees_bis(100)-1                       # nombre d'années bissextiles en 99 ans (1-99) = 24
    nbj99 = nbab99 * 366 + (99 - nbab99) * 365          # nombre de jours en 99 ans = 36159
    nbj4 = 3 * 365 + 366                                # nombre de jours en 4 ans = 1461
    if restej > nbj99 :                                     # parcours complet des années 1-99 ?
        a += 99
        restej -= nbj99
    else :                                                  # parcours du siècle incomplet ?
        a += (restej // nbj4) * 4                               # nombre de cycles de 4 ans écoulés
        restej %= nbj4
        if restej // 365 < 4 :                                  # nombre d'années en plus (dans 0-3) (cas critique à traiter)
            a += restej // 365
            restej %= 365
    return Date(nbj_dans_mois, mois+1, aprox_an)



def test_nb (nb_a_debut = 0, nb_a_fin = 1000) :
    """
    pb : init de cptj !->ok
    complexité ? il prend de plus en plus de temps...
    opérations couteuses au fur et à mesure
    complexité du to_j() ?
    """
    cptj = from_a(nb_a_debut).to_j()-1
    for a in range(nb_a_debut, nb_a_fin):
        if a % 10 == 0 :
            print("année : ", a)
        bis = bissextile(a)
        if bis :
            lg = Date.longueurs_mois_bis
        else :
            lg = Date.longueurs_mois
        for m in range(1,13) :
            for j in range(1, lg[m-1]+1) :
                cptj += 1
                if Date(j,m,a).to_j() != cptj :
                    return False
    return True



def test_date (nb_a_debut = 0, nb_a_fin = 1000) :
    """
    lève une exception..... from_j(366) !!!!
    """
    cptj = from_a(nb_a_debut).to_j()-1
    for a in range(nb_a_debut, nb_a_fin):
        #if a % 10 == 0 :
        #    print("année : ", a)
        bis = bissextile(a)
        if bis :
            lg = Date.longueurs_mois_bis
        else :
            lg = Date.longueurs_mois
        for m in range(1,13) :
            for j in range(1, lg[m-1]+1) :
                cptj += 1;print("cptj : ",cptj)
                if not equals(Date(j,m,a), from_j(cptj)) :
                    return False
    return True



def equals (date1, date2) :
    return date1.annee == date2.annee and date1.mois == date2.mois and date1.jour == date2.jour




