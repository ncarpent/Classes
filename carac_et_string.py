"""
Créé le Ve 02/04/2021 à 23:50
Auteur : Nate
"""

"""
A faire :
¤ faire les méthodes de construction de la classe Carac.
¤ faire les méthodes de construction de la classe String.
¤ faire les méthodes de Carac.
¤ remettre le nom d'origine aux méthodes de Carac.
* annulé : caractères ascii en tant que constantes de classe (Carac) : lève des exceptions : les caractères ne sont pas affichables
¤ Carac.__init__ : pour une String
¤ String.__init__ : pour une str
? String.__init__ : pour un objet quelconque ???
_ faire les méthodes de String : capitalize, center, count, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isdigit, isnumeric (?), isidentifier, islower, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, partition, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate (?), upper, zfill, maketrans (?).
_ Carac.join (et String.join) à améliorer un peu : pour un iterable quelconque
_ faire le formatage de String
* faire les caractères ascii en tant que constantes de classe (Carac / String ?) : ascii(0 à 255), minuscule, majuscule, alphabétique, chiffre, numérique, espace, affichable : ne va pas fonctionner
_ supprimer les codes erreurs
_ réécrire les messages d'erreurs
_ améliorer la documentation des classes
_ refaire la documentation des méthodes
/!\ se limiter aux caractères 0 à 256
non traité : casefold (simillaire à lower mais traite aussi des caractères non latin : eszett, lettres grecques...), encode (?), isdecimal (simillaire à isdigit)
_ faire une documentation du fichier global
_ générer des chaines aléatoires et comparer les résultats des méthodes de str et de String.
"""



## Classe Carac





class Carac :
    """
    Classe des caractères affichables. Seul les 128 premiers caractères ascii sont gérés correctement.
    
    Cette classe contient les méthodes suivantes :
        Edition de l'objet -------------------------------------------------------------------------------------
        _ __init__ : constructeur de la classe                                                              (ok) err 1, 2, 2.5
        _ __repr__ : affichage d'un Carac                                                                   (ok)
        Méthode de conteneur -----------------------------------------------------------------------------------
        _ __len__ : longueur d'un Carac (caractère vide : 0, autre : 1)                                     (ok)
        Opérations mathématiques -------------------------------------------------------------------------------
        _ __add__ : concaténation de deux Carac (création d'une String)                                     (ok) (nécessite la classe string) err 7
                    (cas d'un Carac + une String : appel à String.__radd__)
        _ __mul__ : duplication d'un Carac par un entier                                                    (ok) (nécessite la classe string) err 8
        _ __rmul__ :duplication inversée                                                                    (ok) (nécessite la classe string)
        Comparaisons -------------------------------------------------------------------------------------------
        _ __eq__ : test d'égalité de deux Carac                                                             (ok)
                    (le test d'inégalité en découle automatiquement)
        _ __gt__ : comparaison de deux Carac   (a>b)                                                        (ok) err 3
        _ __lt__ : comparaison de deux Carac   (a<b)                                                        (ok) err 4
        _ __ge__ : comparaison de deux Carac   (a>=b)                                                       (ok) err 5
        _ __le__ : comparaison de deux Carac   (a<=b)                                                       (ok) err 6
        
        Les méthodes __iadd__ et __imul__ ne sont pas définies
        
        Autres méthodes :
        
        Tests --------------------------------------------------------------------------------------------------
        _ islower : test si le caractère est une minuscule                                                  (ok)
        _ isupper : test si le caractère est une majuscule                                                  (ok)
        _ isalpha : test si le caractère est un symbole alphabétique                                        (ok)
        _ isdigit : test si le caractère est un chiffre                                                     (ok)
        _ isnumeric : test si le caractère est un symbole numérique                                         (ok)
        _ isalnum : test si le caractère est un symbole alphanumérique                                      (ok)
        _ isspace : test si le caractère est un espace                                                      (ok)
        _ isprintable : test si le caractère est affichable                                                 (ok)
        Casse --------------------------------------------------------------------------------------------------
        _ lower : change un caractère alphabétique en minuscule                                             (ok)
        _ upper : change un caractère alphabétique en majuscule                                             (ok)
        _ swapcase : inverse la casse                                                                       (ok)
        Autre --------------------------------------------------------------------------------------------------
        _ join : utilise le caractère pour joindre des chaines                                              (ok)
    
    Cette classe est associée aux fonctions suivantes :
        _ codasc : obtention du code ascii d'un caractère                                                   (ok)
        _ chara : construction d'un caractère à partir d'un code ascii                                      (ok)
        
    """
    

    
    def __init__ (self, obj='') :
        """
        Constructeur de la classe Carac.
        Prends une chaîne de caractères unitaire (ou un caractère, ou une string) en argument.
        Codes erreurs 1 et 2.
        """
        if type(obj) == Carac : # crée un nouvel objet
            self.val = obj.val
        elif type(obj) == str :
            if len(obj) <= 1 :
                self.val = obj
            else :
                raise ValueError("Un caractère ne peut pas être construit à partir d'une chaîne de caractère de longueur " + str(len(obj)) + ". Seules longueurs possibles : 0 ou 1. (Erreur Carac 2)")
        elif type(obj) == String :
            if len(obj) == 0 :
                self.val = ''
            elif len(obj) == 1 :
                self.val = obj[0].val
            else :
                raise ValueError("Un caractère ne peut pas être construit à partir d'une string de longueur " + str(len(obj)) + ". Seules longueurs possibles : 0 ou 1. (Erreur Carac 2.5)")
        else :
            raise TypeError("Un caractère ne peut pas être construit à partir d'un objet de type : " + str(type(obj)) + ". (Erreur Carac 1)") 
    
    
    
    def __repr__ (self) :
        """
        Afficheur de la classe Carac.
        """
        return self.val
    
    
    
    def __len__ (self) :
        """
        Renvoie la longueur d'un caractère (0 pour un caractère vide, 1 sinon).
        """
        return len(self.val)
    
    
    
    def __add__ (self, autre) :
        """
        Somme d'un caractère et d'un autre objet (de type Carac). Renvoie un objet de type String.
        Implémente l'opération self + autre.
        Code erreur 7
        """
        if type(autre) == Carac :
            return String(self, autre)
        else :
            try :
                return autre.__radd__(self)
            except :
                raise TypeError("Un caractère n'est pas sommable avec un objet de type " + str(type(autre)) + ". (Code erreur 7)")
    
    
    
    def __mul__ (self, autre) :
        """
        Produit d'un caractère et d'un autre objet (de type int). Renvoi un objet de type String.
        Implémente l'opération self * autre.
        Code erreur 8.
        """
        if type(autre) == int :
            l = [self for i in range(autre)]
            return String(*l)
        else :
            raise TypeError("Un caractère ne peut pas être multiplié par un objet de type " + str(type(autre)) + " (seulement par un entier). (Code erreur 8).")
    
    
    
    def __rmul__ (self, autre) :
        """
        Produit d'un objet quelconque (entier attendu) et d'un caractère. Renvoi un objet de type String.
        Implémente l'opération autre * self.
        """
        return self * autre
    
    
    
    def __eq__ (self, autre) :
        """
        Test d'égalité de deux caractères.
        Implémente la relation ==.
        La relation != est implémentée automatiquement et a!=b renvoie not(a==b).
        """
        if type(autre) != Carac :
            return False
        return self.val == autre.val
    
    
    
    def __gt__ (self, autre) :
        """
        Test de comparaison de deux caractères.
        Implémente la relation >.
        Code erreur 3.
        """
        if type(autre) != Carac :
            raise TypeError("L'objet " + str(autre) + " (de type " + str(type(autre)) + ") n'est pas comparable à un caractère. (Erreur Carac 3)")
        return codasc(self) > codasc(autre)
    
    
    
    def __lt__ (self, autre) :
        """
        Test de comparaison de deux caractères.
        Implémente la relation <.
        Code erreur 4.
        """
        if type(autre) != Carac :
            raise TypeError("L'objet " + str(autre) + " (de type " + str(type(autre)) + ") n'est pas comparable à un caractère. (Erreur Carac 4)")
        return codasc(self) < codasc(autre)
    
    
    
    def __ge__ (self, autre) :
        """
        Test de comparaison de deux caractères.
        Implémente la relation >=.
        Code erreur 5.
        """
        if type(autre) != Carac :
            raise TypeError("L'objet " + str(autre) + " (de type " + str(type(autre)) + ") n'est pas comparable à un caractère. (Erreur Carac 5)")
        return codasc(self) >= codasc(autre)
    
    
    
    def __le__ (self, autre) :
        """
        Test de comparaison de deux caractères.
        Implémente la relation <=.
        Code erreur 6.
        """
        if type(autre) != Carac :
            raise TypeError("L'objet " + str(autre) + " (de type " + str(type(autre)) + ") n'est pas comparable à un caractère. (Erreur Carac 6)")
        return codasc(self) <= codasc(autre)
    
    
    
    
    
    ## Autres méthodes
    
    ## Tests
    
    
    
    def islower (self) :
        """
        Test si le caractère est une minuscule.
        """
        return codasc(self) in range(97,123)
    
    
    
    def isupper (self) :
        """
        Test si le caractère est une majuscule.
        """
        return codasc(self) in range(65, 91)
    
    
    
    def isalpha (self) :
        """
        Test si le caractère est alphabétique.
        """
        return self.islower() or self.isupper()
    
    
    
    def isdigit (self) :
        """
        Test si le caractère est un chiffre.
        """
        return codasc(self) in range(48, 58)
    
    
    
    def isnumeric (self) :
        """
        Test si le caractère est numérique. (identique à isdigit en ascii(128)).
        """
        return self.isdigit()
    
    
    
    def isalnum (self) :
        """
        Test si le caractère est alphanumérique.
        """
        return self.isalpha() or self.isnumeric()
    
    
    
    def isspace (self) :
        """
        Test si le caractère est un espace.
        """
        return (codasc(self) in range(9, 14)) or (codasc(self) in range(28, 33))
    
    
    
    def isprintable (self) :
        """
        Test si le caractère est affichable.
        """
        return codasc(self) in range(32, 127)
    
    
    
    ## Modifications
    
    
    
    def lower (self) :
        """
        Renvoi le caractère minuscule associé si c'est un caractère alphabétique majuscule, ou le caractère inchangé sinon.
        """
        k = codasc(self)
        if k in range(65, 91) :
            return chara(k+32)
        else :
            return chara(k)
    
    
    
    def upper (self) :
        """
        Renvoi le caractère majuscule associé si c'est un caractère alphabétique minuscule, ou le caractère inchangé sinon.
        """
        k = codasc(self)
        if k in range(97, 123) :
            return chara(k-32)
        else :
            return chara(k)
    
    
    
    def swapcase (self) :
        """
        Renvoie le caractère de casse inversée (ou le même caractère s'il n'a pas de casse).
        """
        k = codasc(self)
        if k in range(65, 91) :
            return chara(k+32)
        elif k in range(97, 123) :
            return chara(k-32)
        else :
            return chara(k)
    
    
    
    def join (self, liste) :
        """
        Joint les String éléments de liste avec le caractère fournit.
        Renvoit une nouvelle String.
        """
        s=String()
        for i, k in enumerate(liste) :
            s += k
            if i != len(liste)-1 :
                s += self
        return s
    
    
    
    
    
## Fonctions asociées à la classe Carac





def codasc (c) :
    """
    Renvoie le code ascii d'un caractère.
    """
    if type(c) == Carac :
        return ord(c.val)
    else :
        raise TypeError("Seuls les caractères possèdent un code ASCII.")



def chara (code) :
    """
    Renvoie le caractère associé à un code ascii.
    """
    return Carac(chr(code))
    
    
    


## Classe String





class String :
    """
    Classe des chaînes de caractères affichables (liste de Carac).
    
    Cette classe contient les méthodes suivantes :
        Edition de l'objet :---------------------------------------------------------------------------------------------
        _ __init__ : constructeur de la classe                                                              (ok) err 11
        _ __repr__ : affichage d'une String                                                                 (ok)
        Méthodes de conteneurs :-----------------------------------------------------------------------------------------
        _ __getitem__ : lecture d'un élément d'une String                                                   (ok) err 10
        _ __contains__ : appartenance d'un Carac à String                                                   (ok)
        _ __len__ : longueur d'une String                                                                   (ok)
        Les méthodes __setitem__ et __delitem__ ne sont pas définies.
        Opérations mathématiques :---------------------------------------------------------------------------------------
        _ __add__ : concaténation d'une String avec une String ou un Carac                                  (ok) err 1
        _ __mul__ : duplication d'une String par un entier                                                  (ok) err 2
        _ __mod__ : formatage d'une String                                                                  (A faire) (plus tard...)
        _ __radd__ : concaténation d'un Carac avec une String                                               (ok) err 3
        _ __rmul__ : duplication inversée (d'un entier par une String)                                      (ok)
        _ __iadd__ : concaténation en place                                                                 (ok) err 4
        _ __imul__ : duplication en place                                                                   (ok) err 5
        _ __imod__ : formatage en place                                                                     (A faire) (plus tard...)
        Les méthodes __sub__, __isub__, __trudiv__, __floordiv__, __pow__ et __rmod__ ne sont pas définies.
        Comparaisons :---------------------------------------------------------------------------------------------------
        _ __eq__ : test d'égalité de deux String                                                            (ok)
        _ __gt__ : comparaison de deux String (a>b)                                                         (ok) (ordre lexicographique) err 6
        _ __ge__ : comparaison de deux String (a>=b)                                                        (ok) (ordre lexicographique) err 7
        _ __lt__ : comparaison de deux String (a<b)                                                         (ok) (ordre lexicographique) err 8
        _ __le__ : comparaison de deux String (a<=b)                                                        (ok) (ordre lexicographique) err 9
        (le test d'inégalité en découle automatiquement)
        
        Autres méthodes :
        
        Tests :----------------------------------------------------------------------------------------------------------
        _ islower                                                                                           (ok)
        _ isupper                                                                                           (ok)
        _ isalpha                                                                                           (ok)
        _ isdigit                                                                                           (ok)
        _ isnumeric                                                                                         (ok)
        _ isalnum                                                                                           (ok)
        _ isidentifier                                                                                      (ok)
        _ istitle                                                                                           (ok)
            _ istitle_word                                                                                  (ok)
            _ istitle_split                                                                                 (ok)
        _ isspace                                                                                           (ok)
        _ isprintable                                                                                       (ok)
        _ startswith                                                                                        (ok) (+) adapter à d'autre types (str)
        _ endswith                                                                                          (ok) (+) adapter à d'autre types (str)
        
        Changements de casse :-------------------------------------------------------------------------------------------
        _ lower                                                                                             (ok)
        _ upper                                                                                             (ok)
        _ swapcase                                                                                          (ok)
        _ capitalize                                                                                        (ok)
        _ title                                                                                             (ok)
            _ title_split                                                                                   (ok)
            
        Alignement :-----------------------------------------------------------------------------------------------------
        _ center                                                                                            (ok) (+) utiliser un autre type que Carac
        _ ljust                                                                                             (ok) (+) utiliser un autre type que Carac
        _ rjust                                                                                             (ok) (+) utiliser un autre type que Carac
        _ zfill                                                                                             (ok)
        
        Indiçage :--------------------------------------------------------------------------------------------------------
        _ find                                                                                              (A verif) carac et string
        _ rfind                                                                                             (A verif) carac et string
        _ index                                                                                             (A faire)
        _ rindex                                                                                            (A faire)
        _ count                                                                                             (A faire)
        
        Modifications :---------------------------------------------------------------------------------------------------
        _ expandtabs                                                                                        (A voir)
        _ replace                                                                                           (A faire)
        _ strip                                                                                             (A faire)
        _ lstrip                                                                                            (A faire)
        _ rstrip                                                                                            (A faire)
        _ translate                                                                                         (A faire plus tard)
        
        Autre :-----------------------------------------------------------------------------------------------------------
        _ join                                                                                              (A faire)
        _ split                                                                                             (A faire)
        _ rsplit                                                                                            (A faire)
        _ splitlines                                                                                        (A faire)
        _ partition                                                                                         (A faire)
        _ rpartition                                                                                        (A faire)
        _ format_map                                                                                        (A faire plus tard)
        _ format                                                                                            (A faire plus tard)
        
        Utilitaire :------------------------------------------------------------------------------------------------------
        _ maketrans                                                                                         (A faire plus tard)
    """
    
    
    
    ## Edition de l'objet
    
    
    
    def __init__ (self, *args) :
        """
        Constructeur de la classe String.
        Prends un nombre quelconque d'arguments de type Carac, str, ou String.
        # si args change une valeur, self ne changera pas
        """ 
        self.car = []
        for k in args :
            if type(k) == String :
                self.car += k.car
            elif type(k) == Carac :
                self.car.append(k)
            elif type(k) == str :
                for i in k :
                    self.car.append(Carac(i))
            else :
                raise TypeError("Une chaine de caractères ne peut pas être générée à partir d'un objet de type " + str(type(k)) + ". Code erreur 11.")
    
    
    
    def __repr__ (self) :
        """
        Afficheur de la classe String.
        """
        s=""
        for c in self.car :
            s += repr(c)
        return s
    
    
    
    ## Méthodes de conteneurs
    
    
    
    def __getitem__ (self, k) :
        """
        Renvoi le k-ième caractère de la chaine (si k est un entier) ou la sous-chaine d'indices k (si k est un slice).
        Implémente l'indexation self[k].
        Code erreur 10.
        """
        if type(k) == int :
            return self.car[k]
        elif type(k) == slice :
            return String(*tuple(self.car[k]))
        else :
            print()
            raise TypeError("Une chaine de caractère ne peut pas être indexée par un objet de type " + str(type(k)) + " (seulement par un entier ou un slice). Coode erreur 10.")
    
    
    
    def __contains__ (self, elem) :
        """
        Test d'appartenance de elem à self.
        Implémente la relation elem in self.
        """
        return Carac(elem) in self.car
    
    
    
    def __len__ (self) :
        """
        Renvoi la longueur de la chaine.
        """
        return len(self.car)
    
    
    
    ## Opérateurs mathématiques
    
    
    
    def __add__ (self, autre) :
        """
        Addition avec un objet de type String ou Carac.
        Implémente l'opération self + autre.
        Code erreur 1.
        """
        if type(autre) == String :
            return String(*self.car + autre.car)
        if type(autre) == Carac :
            return self + String(autre)
        raise TypeError("Une chaine de caractère ne peut pas être additionnée avec un objet de type " + str(type(autre)) + " (seulement String ou Carac). Code Erreur 1.")
    
    
    
    def __radd__ (self, autre) :
        """
        Addition inverse (cas de l'addition d'un caractère et d'une chaine).
        Implémente l'opération autre + self.
        Code erreur 3.
        """
        if type(autre) == Carac :
            return String(autre) + self
        else :
            raise TypeError("Une chaine de caractère ne peut pas être additionnée avec un objet de type " + str(type(autre)) + " (seulement String ou Carac). Code Erreur 3.")
    
    
    
    def __iadd__ (self, autre) :
        """
        Addition en place.
        Implémente l'opération self += autre.
        Code erreur 4.
        """
        if type(autre) == String :
            self.car += autre.car
            return self
        if type(autre) == Carac :
            self.car.append(autre)
            return self
        raise TypeError("Une chaine de caractère ne peut pas être additionnée avec un objet de type " + str(type(autre)) + " (seulement String ou Carac). Code Erreur 4.")
    
    
    
    def __mul__ (self, autre) :
        """
        Multiplication d'une String par un entier.
        Implémente l'opération self * autre.
        Code erreur 2.
        """
        if type(autre) == int :
            return String(*self.car*autre)
        else :
            raise TypeError("Une chaine ne peut pas être multipliée par un objet du type " + str(type(autre)) + " (multiplication possible seulement par un entier). (Code erreur 2).")
    
    
    
    def __rmul__ (self, autre) :
        """
        Multiplication inverse (d'un entier et d'une string).
        Implémente l'opération autre * self.
        """
        return self * autre
    
    
    
    def __imul__ (self, autre) :
        """
        Multiplication en place.
        Implémente l'opération self *= autre.
        Code erreur 5.
        """
        if type(autre) == int :
            self.car *= autre
            return self
        raise TypeError("Une chaine ne peut pas être multipliée par un objet du type " + str(type(autre)) + " (multiplication possible seulement par un entier). (Code erreur 5).")
    
    
    
    ## Comparaisons
    
    
    
    def __eq__ (self, autre):
        """
        Test d'égalité de deux chaines de caractères.
        Implémente l'opération self == autre.
        """
        if type(autre) != String :
            return False
        return self.car == autre.car
    
    
    
    def __gt__ (self, autre) :
        """
        Test de supériorité stricte de deux chaines.
        Implémente l'opération self > autre.
        Code erreur 6.
        """
        if type(autre) != String :
            raise TypeError("Une chaine ne peut pas être comparée à un objet de type " + str(type(autre)) + ". Code erreur 6.")
        for k in range(len(self)) :
            if k < len(autre) :
                if self.car[k] > autre.car[k] :
                    return True
                elif self.car[k] < autre.car[k] :
                    return False
            elif k >= len(autre) :
                return True
        if len(self) == len(autre) :
            return False
        return False
    # s = 'bonjour'
    # t = 'aquarelle'
    # u = 'bonne journée'
    # v = 'bonne nuit'
    # w = 'bonnet'
    # x = 'bonne'
    # t < s < x < u < v < w
    
    
    
    def __ge__ (self, autre) :
        """
        Test de supériorité large de deux chaines.
        Implémente l'opération self >= autre.
        Code erreur 7.
        """
        if type(autre) != String :
            raise TypeError("Une chaine ne peut pas être comparée à un objet de type " + str(type(autre)) + ". Code erreur 7.")
        for k in range(len(self)) :
            if k < len(autre) :
                if self.car[k] > autre.car[k] :
                    return True
                elif self.car[k] < autre.car[k] :
                    return False
            elif k >= len(autre) :
                return True
        if len(self) == len(autre) :
            return True
        return False
    
    
    
    def __lt__ (self, autre) :
        """
        Test d'infériorité stricte de deux chaines.
        Implémente l'opération self < autre.
        Code erreur 8.
        """
        if type(autre) != String :
            raise TypeError("Une chaine ne peut pas être comparée à un objet de type " + str(type(autre)) + ". Code erreur 8.")
        for k in range(len(self)) :
            if k < len(autre) :
                if self.car[k] > autre.car[k] :
                    return False
                elif self.car[k] < autre.car[k] :
                    return True
            elif k >= len(autre) :
                return False
        if len(self) == len(autre) :
            return False
        return True
    
    
    
    def __le__ (self, autre) :
        """
        Test d'infériorité large de deux chaines.
        Implémente l'opération self <= autre.
        Code erreur 9.
        """
        if type(autre) != String :
            raise TypeError("Une chaine ne peut pas être comparée à un objet de type " + str(type(autre)) + ". Code erreur 9.")
        for k in range(len(self)) :
            if k < len(autre) :
                if self.car[k] > autre.car[k] :
                    return False
                elif self.car[k] < autre.car[k] :
                    return True
            elif k >= len(autre) :
                return False
        if len(self) == len(autre) :
            return True
        return True
    
    
    
    ## Tests
    
    
    
    def islower (self) :
        """
        Test si la chaine est en minuscule.
        """
        for k in self :
            if not k.islower() :
                return False
        return True
    
    
    
    def isupper (self) :
        """
        Test si la chaine est en majuscule.
        """
        for k in self :
            if not k.isupper() :
                return False
        return True
    
    
    
    def isalpha (self) :
        """
        Test si la chaine est composée de caractères alphabétiques.
        """
        for k in self :
            if not k.isalpha() :
                return False
        return True
    
    
    
    def isdigit (self) :
        """
        Test si la chaine est composée de chiffres.
        """
        for k in self :
            if not k.isdigit() :
                return False
        return True
    
    
    
    def isnumeric (self) :
        """
        Test si la chaine est composée de caractères numériques.
        """
        for k in self :
            if not k.isnumeric() :
                return False
        return True
    
    
    
    def isalnum (self) :
        """
        Test si la chaine est composée de caractères alphanumériques.
        """
        for k in self :
            if not k.isalnum() :
                return False
        return True
    
    
    
    def isidentifier (self) :
        """
        Test si la chaine est un identifiant.
        Un identifiant est une chaine dont le premier caractère est un tiret(_) ou un caractère alphabétique et qui est uniquement composée de tirets(_), de caractères alphabétiques ou de chiffres.
        """
        if len(self) == 0 :
            return False
        if not(self[0].isalpha()) and codasc(self[0]) != 95 :
            return False
        for k in self :
            if not k.isalpha() and not k.isdigit() and codasc(k) != 95 :
                return False
        return True
    
    
    
    def istitle_word (self) :
        """
        Test si le mot est un titre.
        L'argument doit être un mot. Un mot est une chaine qui n'est composée que de caractères alphabétiques.
        Un mot est un titre s'il est non-vide, son premier caractère est en majuscule et les autres sont en minuscules.
        """
        if not self.isalpha() :
            raise ValueError("Le 'mot' contient des caractères non-alphabétiques")
        if len(self) == 0 : # attention à cette condition /!\
            return False
        if self[0].islower() :
            return False
        for k in range(1, len(self)) :
            if self[k].isupper() :
                return False
        return True
    
    
    
    def istitle_split (self) :
        """
        Renvoie la liste des mots composant la chaine.
        Un mot est une chaine qui n'est composée que de caractères alphabétiques.
        """
        mots = []
        tmp = String()
        for k in self :
            if k.isalpha() :
                tmp += k
            else :
                mots.append(tmp)
                tmp = String()
        mots.append(tmp)
        # suppression des mots vides
        clear = []
        for k in mots :
            if k != String() :
                clear.append(k)
        return clear
    
    
    
    def istitle (self) :
        """
        Test si la chaine est un titre.
        Une chaine est un titre si tous les mots qui la compose sont des titres.
        Un mot est une chaine qui n'est composée que de caractères alphabétiques.
        Un mot est un titre s'il est non-vide, si son premier caractère est en majuscule et si les autres sont en minuscules.
        """
        liste_mots = self.istitle_split()
        if len(liste_mots) == 0 :
            return False
        for k in liste_mots :
            if not k.istitle_word() :
                return False
        return True
    
    
    
    def isspace (self) :
        """
        Test si la chaine est une chaine d'espace.
        """
        for k in self :
            if not k.isspace() :
                return False
        return True
    
    
    
    def isprintable (self) :
        """
        Test si la chaine est affichable.
        """
        for k in self :
            if not k.isprintable() :
                return False
        return True
    
    
    
    def startswith (self, start) :
        """
        Test si la chaine commence par start.
        """
        if type(start) == String :
            if len(start) > len(self) :
                return False
            for k in range(len(start)) :
                if self[k] != start[k] :
                    return False
            return True
        else :
            raise TypeError("L'argument de startswith doit être une String.")
    
    
    
    def endswith (self, end) :
        """
        Test si la chaine fini par end.
        """
        if type(end) == String :
            if len(end) > len(self) :
                return False
            for k in range(1, len(end)+1) :
                if self[-k] != end[-k] :
                    return False
            return True
        else :
            raise TypeError("L'argument de endswith doit être une String.")
    
    
    
    ## Changements de casse
    
    
    
    def lower (self) :
        """
        Renvoie une copie en minuscule de la chaine.
        """
        s = String()
        for k in self :
            s += k.lower()
        return s
    
    
    
    def upper (self) :
        """
        Renvoie une copie en majuscule de la chaine.
        """
        s = String()
        for k in self :
            s += k.upper()
        return s
    
    
    
    def swapcase (self) :
        """
        Renvoie une copie de casse inversée de la chaine.
        """
        s = String()
        for k in self :
            s += k.swapcase()
        return s
    
    
    
    def capitalize (self) :
        """
        Renvoie une copie de la chaine avec le premier caractère en majuscule et les autres en minuscules.
        """
        s = String()
        if len(self) == 0 :
            return s
        for i in range(len(self)) :
            if i == 0 :
                s += self[i].upper()
            else :
                s += self[i].lower()
        return s
    
    
    
    def title_split (self) : # self doit être non vide !!!
        """
        Scinde la chaine en deux (liste des sous-chaines alphabétiques et liste des sous-chaines non-alphabétiques) et renvoie les deux listes.
        La première des deux listes renvoyées est du même type que le premier caractère de la chaine (alphabétique ou non).
        """
        deb_alpha = self[0].isalpha()
        last_alpha = deb_alpha
        mots = []
        autres = []
        tmp = String()
        for k in self :
            if last_alpha == True :
                if k.isalpha() :
                    tmp += k
                else :
                    mots.append(tmp)
                    tmp = String(k)
                    last_alpha = False
            else :
                if k.isalpha() :
                    autres.append(tmp)
                    tmp = String(k)
                    last_alpha = True
                else :
                    tmp += k
        if last_alpha :
            mots.append(tmp)
        else :
            autres.append(tmp)
        if deb_alpha :
            return (mots, autres)
        else :
            return (autres, mots)
    
    
    
    def title (self) :
        """
        Renvoie une copie de la chaine dont tout les mots qui la composent sont des titres.
        Un mot est une chaine (ou une sous-chaine) composée uniquement de caractères alphabétiques.
        Un mot est un titre s'il est non vide, son premier caractère est en majuscule et les autres en minuscules.
        """
        s = String()
        if len(self) == 0 :
            return s
        deb_alpha = False
        lgr_eg = False
        listes = self.title_split()
        if len(listes[0]) == len(listes[1]) :
            lgr_eg = True
        else :
            lgr_eg = False
        if listes[0][0].isalpha() :
            deb_alpha = True
            liste_alpha = listes[0]
            liste_symb = listes[1]
            for i in range(len(liste_symb)) :
                s += liste_alpha[i].capitalize()
                s += liste_symb[i]
            if not lgr_eg :
                s += liste_alpha[-1].capitalize()
        else :
            deb_alpha = False
            liste_symb = listes[0]
            liste_alpha = listes[1]
            for i in range(len(liste_alpha)) :
                s += liste_symb[i]
                s += liste_alpha[i].capitalize()
            if not lgr_eg :
                s += liste_symb[-1]
        return s
    
    
    
    ## Alignements
    
    
    
    def center (self, lgr, car = Carac(" ")) :
        """
        Renvoie une copie de la chaine, de la longueur lgr et centrée avec le caractère de remplissage car.
        Si la longueur spécifiée est inférieure ou égale à la longueur de la chaine, renvoie une copie de la chaine.
        La variable renvoyée est toujours indépendante de la chaine originelle.
        Si la chaine ne peut pas être centrée dans la longueur donnée, elle sera décalée d'un caractère vers la gauche dans la chaine de retour.
        """
        if lgr <= len(self) :
            return String(self)
        nb_car = lgr - len(self)
        if nb_car % 2 == 0 :
            gch = nb_car // 2
            dte = nb_car // 2
        elif nb_car % 2 == 1 :
            gch = nb_car // 2
            dte = nb_car - gch
        s = String()
        for k in range(gch) :
            s += car
        s += self
        for k in range(dte) :
            s += car
        return s
    
    
    
    def ljust (self, lgr, car = Carac(' ')) :
        """
        Renvoie une copie de la chaine, de la longueur lgr et alignée à gauche (utilise car comme caractère de remplissage).
        Si la longueur spécifiée est inférieure ou égale à la longueur de la chaine, renvoie une copie de la chaine.
        La variable renvoyée est toujours indépendante de la chaine originelle.
        """
        s = String(self)
        if lgr <= len(self) :
            return s
        nb_car = lgr - len(self)
        for k in range(nb_car) :
            s += car
        return s
    
    
    
    def rjust (self, lgr, car = Carac(' ')) :
        """
        Renvoie une copie de la chaine, de la longueur lgr et alignée à droite (utilise car comme caractère de remplissage).
        Si la longueur spécifiée est inférieure ou égale à la longueur de la chaine, renvoie une copie de la chaine.
        La variable renvoyée est toujours indépendante de la chaine originelle.
        """
        if lgr <= len(self) :
            return String(self)
        nb_car = lgr - len(self)
        s = String()
        for k in range(nb_car) :
            s += car
        s += self
        return s
    
    
    
    def zfill (self, lgr) :
        """
        Renvoie une copie de la chaine, de la longueur lgr, alignée à droite et éventuellement complétée de '0' pour attiendre cette longueur.
        Si la longueur spécifiée est inférieure ou égale à la longueur de la chaine, renvoie une copie de la chaine.
        """
        return self.rjust(lgr, Carac('0'))
    
    
    
    ## Indiçage
    
    
    
    def find (self, val, start = 0, stop = None) :
        """
        Si val est un caractère, renvoie la position de la première occurance de val dans la chaine, s'il est dans la chaine et -1 sinon.
        Si val est une chaine, renvoie la position de la première occurance de val dans la chaine (en tant que sous-chaine), s'il est dans la chaine et -1 sinon.
        """
        if stop == None :
            stop = len(self)
        if type(val) == Carac :
            for i in range(start, stop) :
                if self[i] == val :
                    return i
            return -1
        if type(val) == String :
            for i in range(len(val)) :
                if i == 0 :
                    pos_init = pos = self.find(val[i], start, stop)
                    if pos == -1 :
                        return -1
                else :
                    if self[pos + 1] != val[i] or pos + 1 >= stop  :
                        return self.find(val, pos_init + 1, stop)
                    pos += 1
            return pos_init
    
    
    
    def rfind (self, val, start = 0, stop = None) :
        """
        Si val est un caractère, renvoie la position de la dernière occurance de val dans la chaine ou -1 s'il n'est pas dans la chaine.
        Si val est une chaine, renvoie la position de la dernière occurance de val dans la chaine (en tant que sous-chaine), s'il est dans la chaine et -1 sinon.
        pas completement correct, peut-etre utiliser un while... (idem pour find je suppose) "bonbjourjour".rfind("bonbj")
        """
        if stop == None :
            stop = len(self)
        if type(val) == Carac :
            for i in range(stop - 1, start - 1, -1) :
                if self[i] == val :
                    return i
            return -1
        if type(val) == String :
            for i in range(len(val)) :
                if i == 0 :
                    pos_init = pos = self.rfind(val[i], start, stop)
                    if pos == -1 :
                        return -1
                else :
                    pos += 1
                    if self[pos] != val[i] or pos >= stop :
                        return self.rfind(val, start, pos_init)
            return pos_init
    
    
    
    
    