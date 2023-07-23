"""
Créé le Di 6/8/2017 à 14:50
Auteur : Nate
durees.py
"""

class Duree :
    
    """
    Cette classe définit des durées en heures (int de 0 à [23]), minutes (int de 0 à 59) et secondes (int de 0 à 59).
    
    Liste des méthodes :
        # Edition de l'objet :
            * __init__                          (ok) plusieurs constructeurs
                -> init_hms                     (ok)
                -> init_hm                      (ok)
                -> init_dur                     (ok)
            * __repr__                          (ok)
        # Méthodes de conteneur :
            * __getitem__                       (ok)
            * __setitem__                       (ok)
            * __delitem__                       (ok)
        # Opérateurs mathématiques :
            * __add__                           (ok)
            * __sub__                           (ok)
            * __mul__                           (ok)
            * __floordiv__                      (ok)
            * __mod__                           (ok)
        # Opérateur mathématiques inverse :
            * __rmul__                          (ok)
        # Opérateurs comparatifs :
            * __eq__                            (ok)
            * __gt__                            (ok)
            * __ge__                            (ok)
        # Autres :
            * to_h                              (ok)
            * to_min                            (ok)
            * to_sec                            (ok)
            * to_int                            (ok)
            * format12                          (ok)
            * duree12                           (ok)
            * duree24                           (ok)
    
    Liste des fonctions annexes :
        * validite_h                            (ok)
        * validite_h_restreint                  (ok)
        * validite_min                          (ok)
        * validite_min_restreint                (ok)
        * validite_sec                          (ok)
        * validite_sec_restreint                (ok)
        * validite_duree                        (ok)
        * validite_duree_restreint              (ok)
        * from_h                                (ok)
        * from_min                              (ok)
        * from_sec                              (ok)
        * from_int                              (ok)
    
    A faire :
    _ ok : fonctions de vérification de validité des données
    _ ok : modulo par une durée (utile pour le format) (et autres opérations -> bof)
    _ ok : format 12 / 24 h utiles pour les durees sup à 24h. (renvoi une durée inf à 24h) (durée et chaîne)
    _ ok : faire une fonction to_int (actuellement to_min, plus tard to_sec, et facilement changeable)
    _ ok : et utiliser ...
    _ ok : détailler les commentaires (?)
    _ ok : méthodes de classes ou fonctions ??? (+ méthodes "privées" (ex de a.from_min(int))) + utilisation
    _ en suspens : constructeurs multiples ? fonctions from_ en méthodes ?
    _ ok : modélisation des secondes (maj liste fonctions avant)
    _ ok : produit flottant (et autre ?)
    _ en suspens : paramètre  global de gestion de la restrictivité des données (?)
    """
    
    
    
    
    

    ## Edition de l'objet
    
    
    
    
    
    def __init__ (self, *args) :
        """
        Constructeur de la classe Duree.
        Construit une Duree à partir d'une autre Duree, d'un nombre d'heures et de minutes ou juste d'un nombre de secondes.
        """
        if len(args) == 0 :
            self.init_hms(0, 0, 0)
        elif len(args) == 1 :
            if type(args[0]) == Duree :
                self.init_dur(args[0])
            elif type(args[0]) == int :
                self.init_hms(0, 0, args[0])
        elif len(args) == 2 :
            self.init_hm(args[0], args[1])
        elif len(args) == 3 :
            self.init_hms(args[0], args[1], args[2])
        else :
            raise AttributeError("Nombre d'arguments incorrect fournis à la construction de l'objet.")
    
    
    
    def init_hms (self, heures = 0, minutes = 0, secondes = 0) :
        """
        Construit une Duree à partir d'un nombre d'heures, de minutes et de secondes entier positif.
        Si le nombre de minutes ou de secondes est supérieur à 60 la valeur est convertie automatiquement.
        
        Paramètres : heures : nombre d'heures entier positif /
                     minutes : nombre de minutes entier positif /
                     secondes : nombre de secondes entier positif.
        """
        # vérifications
        validite_h(heures)
        validite_min(minutes)
        validite_sec(secondes)
        
        # données
        self.sec = secondes % 60
        self.min = ((secondes // 60) + minutes) % 60
        self.h = (((secondes // 60) + minutes) // 60) + heures
    
    
    
    def init_hm (self, heures = 0, minutes = 0) :
        """
        Construit une durée à partir d'un nombre d'heures entier positif et d'un nombre de minutes entier positif.
        Si le nombre de minutes est supérieur à 60 la valeur est convertie automatiquement.
        
        Paramètres : heures : nombre d'heures entier / minutes : nombre de minutes entier
        """
        # vérifications
        validite_h(heures)
        validite_min(minutes)
        
        # données
        self.sec = 0
        self.min = minutes % 60
        self.h = (minutes // 60) + heures
    
    
    
    def init_dur (self, duree) :
        """
        Construit une durée à partir d'une autre durée.
        Suppose que la durée en paramètre est correctement définie.
        
        Paramètre : duree : une Duree valide
        """
        # vérifications
        validite_duree(duree)
        
        # données
        self.h = duree.h
        self.min = duree.min
        self.sec = duree.sec
    
    
    
    def __repr__ (self) :
        """
        Renvoie la chaîne de caractères utilisée pour l'affichage.
        """
        
        str_h = ""
        str_min = ""
        str_sec = ""
        
        # affichage heures
        if self.h <= 9 :
            str_h += "0"
        str_h += str(self.h)
        
        # affichage minutes
        if self.min <= 9 :
            str_min += "0"
        str_min += str(self.min)
        
        # affichage secondes
        if self.sec <= 9 :
            str_sec += "0"
        str_sec += str(self.sec)
        
        # affichage
        return str_h + ":" + str_min + ":" + str_sec
    
    
    
    
    
    ## Méthodes de conteneur
    
    
    
    
    
    def __getitem__ (self, ind) :
        """
        Renvoie le nombre d'heures (avec l'indice "h"), de minutes (avec l'indice "min") ou de secondes (avec l'indice "sec") d'une durée.
        Seules les indices "h", "min" et "sec" sont utilisables.
        
        Exception : IndexError
        """
        if ind == "h" :
            return self.h
        elif ind == "min" :
            return self.min
        elif ind == "sec" :
            return self.sec
        else :
            raise IndexError ("L'indice " + str(ind) + " n'est pas valable. \nSeuls \"h\", \"min\" et \"sec\" sont utilisables.")
    
    
    
    def __setitem__ (self, ind, val) :
        """
        Modifie le nombre d'heures (avec l'indice "h"), de minutes (avec l'indice "min") ou de secondes (avec l'indice "sec") d'une durée.
        Seules les indices "h", "min" et "sec" sont utilisables.
        Attention : l'utilisation d'une plage de valeurs adéquate (0-59 pour les secondes, 0-59 pour les minutes, 0-23 pour les heures) est laissée au libre arbitre de l'utilisateur (conversion automatique).
        
        Exception : IndexError
        """
        if ind == "h" :
            validite_h(val)
            self.h = val
        elif ind == "min" :
            validite_min(val)
            self.min = val % 60
            self.h += val // 60
        elif ind == "sec" :
            validite_sec(val)
            self.sec = val % 60
            self.min += (val // 60) % 60
            self.h += (val // 60) // 60
        else :
            raise IndexError ("L'indice " + str(ind) + " n'est pas valable. \nSeuls \"h\", \"min\" et \"sec\" sont utilisables.")
    
    
    
    def __delitem__ (self, ind) :
        """
        Méthode de suppression d'un attribut (lève une exception).
        """
        raise AttributeError ("Vous ne pouvez supprimmer un attribut seul.")
    
    
    
    
    
    ## Méthodes mathématiques
    
    
    
    
    
    def __add__ (self, objet) :
        """
        Additionne deux Duree ensemble.
        
        Paramètre : objet : un autre objet de type Duree.
        Valeur de retour : la somme self + objet (de type Duree).
        Exception : TypeError.
        """
        if type(objet) == Duree :
            return  from_int(self.to_int() + objet.to_int())        
        else :
            raise TypeError ( "Vous ne pouvez pas sommer une durée avec un objet de type " + str(type(objet)) )
        
    
    
    
    def __sub__ (self, objet) :
        """
        Soustrait deux Duree. self doit être supérieur à objet.
        
        Paramètre : objet : un autre objet de type Duree.
        Valeur de retour : la différence self - objet (de type Duree).
        Exceptions : ValueError, TypeError.
        """
        if type(objet) == Duree :
            r = self.to_int() - objet.to_int()
            if r < 0 :
                raise ValueError ("La différence de ces deux durées est négative.")
            return from_int(r)
        else :
            raise TypeError ( "Vous ne pouvez pas soustraire une durée avec un objet de type " + str(type(objet)) )
    
    
    
    def __mul__ (self, objet) :
        """
        Multiplie une Duree par un coefficient entier ou flottant positif.
        
        Paramètre : objet : un autre objet de type int / float.
        Valeur de retour : le produit self * objet (de type Duree).
        Exceptions : ValueError, TypeError.
        """
        if type(objet) == int :
            if objet < 0 :
                raise ValueError ("La Duree est multipliée par un coefficient négatif.")
            return from_int(self.to_int() * objet)
        elif type(objet) == float :
            if objet < 0 :
                raise ValueError ("La Duree est multipliée par un coefficient négatif.")
            return from_int(int(self.to_int() * objet))
        else :
            raise TypeError ("Vous ne pouvez pas multiplier une Duree par un objet de type " + str(type(objet)) + ".")
    
    
    
    def __floordiv__ (self, objet) :
        """
        Divise une Duree par un coefficient entier ou par une autre Duree. Renvoie le quotient de la division euclidienne.
        
        Paramètre : objet : un autre objet de type Duree ou int.
        Valeur de retour : le quotient de la division euclidienne self // objet.
        Exceptions : ValueError, ZeroDivisionError, TypeError.
        """
        if type(objet) == int :
            if objet < 0 :
                raise ValueError ("La Duree est divisée par un coefficient négatif.")
            if objet == 0 :
                raise ZeroDivisionError ("Division par zéro.")
            return from_int(self.to_int() // objet)
        elif type(objet) == Duree :
            return self // objet.to_int()
        else :
            raise TypeError ("Vous ne pouvez pas diviser une Duree par un objet de type " + str(type(objet)) + ".")
    
    
    
    def __mod__ (self, objet) :
        """
        Divise une Duree par un coefficient entier ou par une autre Duree. Renvoie le reste de la division euclidienne.
        
        Paramètre : objet : un autre objet de type Duree ou int.
        Valeur de retour : le reste de la division euclidienne self % objet.
        Exceptions : ValueError, ZeroDivisionError, TypeError.
        """
        if type(objet) == int :
            if objet < 0 :
                raise ValueError ("La Duree est divisée par un coefficient négatif.")
            if objet == 0 :
                raise ZeroDivisionError ("Division par zéro.")
            return from_int(self.to_int() % objet)
        elif type(objet) == Duree :
            return self % objet.to_int()
        else :
            raise TypeError ("Vous ne pouvez pas diviser une Duree par un objet de type " + str(type(objet)) + ".")
    
    
    
    
    
    ## Opérateurs mathématiques inversés
    
    
    
    
    
    def __rmul__ (self, objet) :
        """
        Défini la multiplication inverse (d'un entier par une Duree).
        
        Paramètre : objet : un autre objet de type int.
        Valeur de retour : le produit objet * self (de type Duree).
        """
        return self * objet
    
    
    
    
    
    ## Méthodes de comparaison
    
    def __eq__ (self, objet) :
        """
        Teste l'égalité de deux Duree.
        
        Paramètre : objet : un autre objet.
        Valeur de retour : l'égalité booléenne self == objet.
        """
        
        if type(objet) != Duree :
            return False
        return self.to_int() == objet.to_int()
    
    # __ne__ : redéfinit self != objet
    
    
    def __gt__ (self, objet) :
        """
        Teste la supériorité stricte d'une Duree par rapport à une autre.
        
        Paramètre : objet : un autre objet de type Duree.
        Valeur de retour : la supériorité stricte booléenne self > objet.
        Exception : TypeError.
        """
        if type(objet) != Duree :
            raise TypeError ("Les types Duree() et " + str(type(objet)) + " ne sont pas comparables.")
        return self.to_int() > objet.to_int()
    
    # __lt__ : redéfinit self < objet
    
    def __ge__ (self, objet) :
        """
        Teste la supériorité large d'un Duree par rapport à une autre.
        
        Paramètre : objet : un autre objet.
        Valeur de retour : la supériorité large booléenne self >= objet.
        Exception : TypeError.
        """
        if type(objet) != Duree :
            raise TypeError ("Les types Duree() et " + str(type(objet)) + " ne sont pas comparables.")
        return self.to_int() >= objet.to_int()
    
    # __le__ : redéfinit self <= objet
    
    
    ## Autre
    
    
    
    
    
    def to_h (self) :
        """
        Renvoie le nombre d'heures comprises dans la Duree.
        """
        return self.h
    
    
    
    def to_min (self) :
        """
        Renvoie le nombre de minutes comprises dans la Duree.
        """
        return 60 * self.to_h() + self.min
    
    
    
    def to_sec (self) :
        """
        Renvoie le nombre de secondes comprises dans la Duree.
        """
        return 60 * self.to_min() + self.sec
    
    
    
    def to_int (self) :
        """
        Transforme la Duree en nombre entier.
        """
        return self.to_sec()
    
    
    
    def format12 (self) :
"""
        Renvoie la chaîne de caractère correspondant à une durée au format 12h.
        """
        d12 = self.duree12()
        d24 = self.duree24()
        if 1 <= d24.h <= 12:
            meridien = "am"
        else :
            meridien = "pm"
        return d12.__repr__() + " " + meridien
    
    
    
    def duree12 (self) :
        """
        Renvoie une Duree au format 12h.
        """
        return Duree((self.h - 1) % 12 + 1, self.min, self.sec)
    
    
    
    def duree24 (self) :
        """
        Renvoie une Duree au format 24h.
        """
        return Duree(self.h % 24, self.min, self.sec)





## Fonctions annexes





'''
def validite_nb (nombre) :
    if type(nombre) != int :
        raise TypeError(str(nombre) + " n'est pas entier.")
    if nombre < 0 :
        raise ValueError(str(nombre) + " est négatif.")
'''


def validite_h (heures) :
    """
    Fonction de vérification de la validité d'une variable représentant un nombre entier d'heures.
    
    Paramètres : heures : nombre dont on souhaite vérifier la validité en tant qu'heures.
    Valeur de retour : aucune.
    Exceptions : TypeError, ValueError.
    """
    if type(heures) != int :
        raise TypeError("Le nombre d'heures n'est pas entier.")
    if heures < 0 :
        raise ValueError("Le nombre d'heures est négatif.")



def validite_h_restreint (heures) :
    """
    Fonction vérifiant qu'une heure est bien dans la plage de valeurs 0-23.
    
    Paramètres : heures : nombre dont on souhaite vérifier la validité en tant qu'heures.
    Valeur de retour : aucune.
    Exceptions : implicites : TypeError, ValueError / ValueError.
    """
    validite_h(heures)
    if heures > 23 :
        raise ValueError("Nombre d'heures trop élevé (>23).")



def validite_min (minutes) :
    """
    Fonction de vérification de la validité d'une variable représentant un nombre entier de minutes.
    
    Paramètres : minutes : nombre dont on souhaite vérifier la validité en tant que minutes.
    Valeur de retour : aucune.
    Exceptions : TypeError, ValueError.
    """
    if type(minutes) != int :
        raise TypeError("Le nombre de minutes n'est pas entier.")
    if minutes < 0 :
        raise ValueError("Le nombre de minutes est négatif.")



def validite_min_restreint (minutes) :
    """
    Fonction vérifiant qu'une minute est bien dans la plage de valeurs 0-59.
    
    Paramètres : minutes : nombre dont on souhaite vérifier la validité en tant que minutes.
    Valeur de retour : aucune.
    Exceptions : implicites : TypeError, ValueError / ValueError.
    """
    validite_min(minutes)
    if minutes > 59 :
        raise ValueError("Nombre de minutes trop élevé (>59).")



def validite_sec (secondes) :
    """
    Fonction de vérification de la validité d'une variable représentant un nombre entier de secondes.
    
    Paramètre : secondes : nombre dont on souhaite vérifier la validité en tant que secondes.
    Valeur de retour : aucune
    Exceptions : TypeError, ValueError.
    """
    if type(secondes) != int :
        raise TypeError("Le nombre de secondes n'est pas entier.")
    if secondes < 0 :
        raise ValueError("Le nombre de secondes est négatif.")



def validite_sec_restreint (secondes) :
    """
    Fonction vérifiant qu'une seconde est bien dans la plage de valeurs 0-59.
    
    Paramètre : secondes : nombre dont on souhaite vérifier la validité en tant que secondes.
    Valeur de retour : aucune.
    Exceptions : implicites : TypeError, ValueError / ValueError.
    """
    validite_sec(secondes)
    if secondes > 59 :
        raise ValueError("Nombre de secondes trop élevé (>59).")



def validite_duree (duree) :
    """
    Fonction de vérification de la validité d'une variable représentant une Duree.
    
    Paramètres : duree : Duree dont on souhaite vérifier la validité en tant que durée.
    Valeur de retour : aucune.
    Exceptions : implicites : TypeError, ValueError / TypeError.
    """
    if type(duree) != Duree :
        raise TypeError("La durée n'est pas de type Duree.")
    validite_h(duree.h)
    validite_min(duree.min)
    validite_sec(duree.sec)



def validite_duree_restreint (duree) :
    """
    Fonction vérifiant qu'une Duree est bien dans la plage de valeurs 0:00 - 23:59.
    
    Paramètres : duree : Duree dont on souhaite vérifier la validité en tant que durée.
    Valeur de retour : aucune.
    Exceptions : implicites : TypeError, ValueError / TypeError.
    """
    if type(duree) != Duree :
        raise TypeError("La durée n'est pas de type Duree.")
    validite_h_restreint(duree.h)
    validite_min_restreint(duree.min)
    validite_sec_restreint(duree.sec)



def from_h (h) :
    """
    Convertit un nombre d'heures positif en Duree.
    
    Paramètre : h : un nombre d'heures (entier positif).
    Valeur de retour : la Duree correspondant au nombre d'heure fournit.
    Exceptions : TypeError, ValueError.
    """
    validite_h(h)
    return Duree(h, 0)



def from_min (m) :
    """
    Convertit un nombre de minutes positif en Duree.
    
    Paramètre : m : un nombre de minutes (entier positifs).
    Valeur de retour : la Duree correspondant au nombre de minutes fournit.
    Exceptions : TypeError, ValueError.
    """
    validite_min(m)
    return Duree(m//60, m%60)



def from_sec (s) :
    """
    Convertit un nombre de secondes positif en Duree.
    
    Paramètre : s : un nombre de secondes (entier positif).
    Valeur de retour : la Duree correspondant au nombre de secondes fournit.
    Exceptions : TypeError, ValueError.
    """
    validite_sec(s)
    return Duree((s//60)//60, (s//60)%60, s%60)



def from_int (n) :
    """
    Convertit un nombre entier positif en Duree.
    
    Paramètre : n : un entier positif.
    Valeur de retour : la Duree correspondant au nombre fournit.
    """
    return from_sec(n)





