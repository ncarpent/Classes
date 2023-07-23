"""
Créé le : 10/02/2023 à 01h22
Auteur : Nate
pile.py
"""

class Pile :
    
    """
    Cette classe définit des piles d'éléments empilables.
    Un élément ne peut rentrer qu'en tête de pile, décalant tous les autres éléments vers le fond.
    Un élément ne peut sortir qu'en tête de pile.
    
    Méthodes :
        ¤ Edition de l'objet :
            __init__                    (ok)
            __repr__                    (ok)
            (__str__ ?)
        ¤ Méthodes de conteneur :
            __getitem__                 (ok : exception)
            __setitem__                 (ok : exception)
            __delitem__                 (ok : exception)
            __contains__ ?
            __len__                     (ok)
        ¤ Opérateurs mathématiques :
            __add__ ?
            __sub__ ?
            __mul__ ?
            __truediv__ ?
            __floordiv__ ?
            __mod__ ?
            __pow__ ?
        ¤ Opérateurs inversés ?
        ¤ Opérateurs en-place ?
        ¤ Opérateurs de comparaison ?
        ¤ Autres :
            empiler                     (ok)
            depiler                     (ok)
            tete                        (ok)
            vider                       (ok)
            est_vide                    (ok)
            copier                      (ok : copie de surface !)
            str                         (ok)
            afficher                    (ok)
    
    Fonctions annexes :(méthodes ?)
        
        copie_profonde (?)
        affiche par méth de pile ?
        champ "taille" ?
        
        
        
         
        
    
    idées : 
    _ pile non-typée / typée par le 1er obj / type = None / NoneType ??? (utiliser type(None) à première vue / fonction de typage (pile vide)
    obliger fonction de typage ? intérêt : peut rester None / inconvénient : un peu chiant
    _ champ de taille ?
    _ cf contains de file pour amélioration de la complexité (pour approfondir)
    
    /!\ list : ajout en fin !!!
    """
    
    
    
    
    
    ## Edition de l'objet
    
    
    
    
    
    def __init__ (self) :
        """
        Construit une nouvelle Pile
        """
        self.stack = []
        self.type = None
    
    
    
    def __repr__ (self) :
        """
        Affiche une Pile.
        """
        ret = "["
        for k in range(len(self.stack)-1) :
            ret += self.stack[k].__repr__() +  ", "
        if len(self.stack) > 0 :
            ret += self.stack[-1].__repr__()
        ret += "/" # / ou _ ou <
        return ret
    
    
    
    
    
    ## Méthodes de conteneur
    
    
    
    
    
    def __getitem__ (self, ind) :
        """
        Méthode d'indexation en lecture. Lève une exception.
        """
        raise TypeError("L'accès au contenu de la Pile n'est pas permis.\nUtiliser les méthodes de gestion de Pile pour accéder à la tête de Pile.")
    
    
    
    def __setitem__ (self, ind, val) :
        """
        Méthode d'indexation en écriture. Lève une exception.
        """
        raise TypeError("L'accès au contenu de la Pile n'est pas permis.\nUtiliser les méthodes de gestion de Pile pour accéder à la tête de Pile.")
    
    
    
    def __delitem__ (self, ind) :
        """
        Méthode d'indexation en suppression. Lève une exception.
        """
        raise TypeError("L'accès au contenu de la Pile n'est pas permis.\nUtiliser les méthodes de gestion de Pile pour accéder à la tête de Pile.")
    
    
    
    def __contains__ (self, val) :
        """
        Test si l'objet val est dans la Pile. Permet la syntaxe val in self.
        Attention au coût de cette méthode (parcours jusqu'à trouver la valeur ou jusqu'au fond) !
        """
        tmp = Pile()
        find = False
        while not self.est_vide() :
            if self.tete() == val :
                find = True
                break
            tmp.empiler(self.depiler())
        while not tmp.est_vide() :
            self.empiler(tmp.depiler())
        return find
    
    
    
    def __len__ (self) :
        """
        Renvoie la longueur de la Pile.
        """
        return len(self.stack)
    
    
    
    ## Autres
    
    
    
    def empiler (self, obj) :
        """
        Ajoute un élément en tête de pile.
        """
        self.stack.append(obj)
    
    
    
    def depiler (self) :
        """
        Retire l'élément en tête de pile et le renvoie.
        """
        if len(self) == 0 :
            raise IndexError("Une pile vide ne peut pas être dépilée.")
        return self.stack.pop(-1)
    
    
    
    def tete (self) :
        """
        Renvoie l'élément en tête de pile.
        """
        if len(self) == 0 :
            raise IndexError("Pile vide.")
        return self.stack[-1]
    
    
    
    def vider (self) :
        """
        Vide la pile de tous ses éléments.
        """
        while len(self) > 0 :
            self.depiler()
    
    
    
    def est_vide (self) :
        """
        Teste si la pile est vide (True) ou non (False).
        """
        return len(self) == 0
    
    
    
    def copier (self, p) :
        """
        Copie le contenu de la pile dans p (vidée au préalable), dans le même ordre.
        /!\ Ceci est une copie de surface /!\
        """
        if type(p) != Pile :
            raise TypeError("Copie de Pile dans " + type(p) + ".")
        p.vider()
        tmp = Pile()
        while not self.est_vide() :
            tmp.empiler(self.depiler())
        while not tmp.est_vide() :
            tete = tmp.depiler()
            self.empiler(tete)
            p.empiler(tete)
    
    
    
    def str (self) :
        """
        Transforme une Pile en chaîne de caractères. intérêt ?
        """
        ret = "["
        tmp = Pile()
        while not self.est_vide() :
            tmp.empiler(self.depiler())
        while not tmp.est_vide() :
            tete = tmp.depiler()
            if tmp.est_vide() :
                ret += str(tete)
            else :
                ret += str(tete) + ", "
            self.empiler(tete)
        ret += "/"
        return ret
    
    
    
    def afficher (self) :
        """
        Affiche une Pile.
        """
        print(self.str())




