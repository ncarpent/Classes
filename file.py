"""
Créé le : 13/02/2023 à 00h42
Auteur : Nate
file.py
"""

class File :
    
    """
    Cette classe définit des files d'éléments enfilables.
    Un élément ne peut rentrer qu'en tête de file, décalant tous les autres éléments vers la queue.
    Un élément ne peut sortir qu'en queue de file.
    Attention: coût important pour les longues listes (>= 100 000 ?)
    
    Méthodes :
        ¤ Edition de l'objet :
            __init__                    (ok)
            __repr__                    (ok)
            (__str__ ?)
        ¤ Méthodes de conteneur :
            __getitem__                 (ok)
            __setitem__                 (ok)
            __delitem__                 (ok)
            __contains__                (~ok~)
            __len__                     (ok)
        ¤ Opérateurs mathématiques ?
        ¤ Opérateurs inversés ?
        ¤ Opérateurs en-place ?
        ¤ Opérateurs de comparaison ?
        ¤ Autre :
            enfiler                     (ok)
            defiler                     (ok)
            pied                        (ok)
            vider                       (ok)
            est_vide                    (ok)
            copier                      (ok : copie de surface !)
    
    Fonctions annexes : ?
    
    Remarques :
    _ enfiler(100 000) dure ~1sec alors que vider tourne très longtemps (interruption)
    _ en effet defiler est plus long qu'enfiler.
    """
    
    
    
    ## Edition de l'objet
    
    
    
    def __init__ (self) :
        """
        Construit une nouvelle File.
        """
        self.queue = []
        self.type = None
    
    
    
    def __repr__ (self) :
        """
        Affiche une File.
        """
        ret = ">"
        for k in range(len(self.queue)-1) :
            ret += self.queue[k].__repr__() + ", "
        if len(self.queue) > 0 :
            ret += self.queue[-1].__repr__()
        ret += "<"
        return ret
    
    
    
    ## Méthodes de conteneur
    
    
    
    def __getitem__ (self, ind) :
        """
        Méthode d'indexation en lecture. Lève une exception.
        """
        raise TypeError("L'accès au contenu de la File n'est pas permis.\nUtiliser les méthodes de gestion de File pour accéder à la tête ou à la queue de File.")
    
    
    
    def __setitem__ (self, ind, val) :
        """
        Méthode d'indexation en écriture. Lève une exception.
        """
        raise TypeError("L'accès au contenu de la File n'est pas permis.\nUtiliser les méthodes de gestion de File pour accéder à la tête ou à la queue de File.")
    
    
    
    def __delitem__ (self, ind) :
        """
        Méthode d'indexation en suppression. Lève une exception.
        """
        raise TypeError("L'accès au contenu de la File n'est pas permis.\nUtiliser les méthodes de gestion de File pour accéder à la tête ou à la queue de File.")
    
    
    
    def __contains__ (self, val) :
        """
        Test si l'objet val est dans la File. Permet la syntaxe val in self.
        Attention au coût de cette méthode (pas de parcours ou parcours TOTAL ) !
        test : 1 in file des k de 0 à 10_000_000 :VRAIMENT très long (interrompu) -> print après le premier while pour vérifier ça (+ "if not find" pas encore pris en compte dans le test : simplifie peut-être déjà les choses...)
        1ere boucle infinie ??? non (ok sur des files courtes)
        coût du pop ?
        """# test pour 1 000 000
        find = False
        tmp = File()
        cpt=0
        print("init ok")#test
        while not self.est_vide() :
            if not find and self.pied() == val :
                if self.pied() % 100000 == 0 :# test
                    print(self.pied())#test
                find = True
                if tmp.est_vide() :
                    break
            print("cpt", cpt)#test
            cpt+=1#test
            tmp.enfiler(self.defiler())
        print("fin 1ere boucle")#test
        while not tmp.est_vide() :
            self.enfiler(tmp.defiler())
        return find
    
    
    
    def __len__ (self) :
        """
        Renvoie la longueur de la File.
        """
        return len(self.queue)
    
    
    
    ## Autres
    
    
    
    def  enfiler (self, obj) :
        """
        Ajoute un élément en tête de File.
        """
        self.queue.append(obj)
    
    
    
    def defiler (self) :
        """
        Retire l'élément en queue de File et le renvoie.
        """
        if len(self) == 0 :
            raise IndexError("Une File vide ne peut pas être défilée.")
        return self.queue.pop(0)
    
    
    
    def pied (self) :
        """
        Renvoie l'élément en queue de File.
        """
        if len(self) == 0 :
            raise IndexError("File vide.")
        return self.queue[0]
    
    
    
    def vider (self) :
        """
        Vide la File de tous ses éléments.
        """
        while len(self) > 0 :
            self.defiler()
    
    
    
    def est_vide (self) :
        """
        Test si la File est vide (True) ou non (False).
        """
        return len(self) == 0
    
    
    
    def copier (self, f) :
        """
        Copie le contenu de la File dans f (vidée au préalable), dans le même ordre.
        /!\ Ceci est une copie de surface /!\
        """
        if type(f) != File :
            raise TypeError("Copie de File dans " + str(type(f)) + ".")
        f.vider()
        tmp = File()
        while not self.est_vide() :
            pied = self.defiler()
            f.enfiler(pied)
            tmp.enfiler(pied)
        while not tmp.est_vide() :
            self.enfiler(tmp.defiler())




