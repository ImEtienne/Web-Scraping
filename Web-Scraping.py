from bs4 import BeautifulSoup
import requests

# Question 1 :
def liste_liens(page):
    # Ceci est un commentaire expliquant que nous récupérons la page cible et l'ajoutons au chemin d'accès principal
    url = "https://iceandfire.fandom.com/wiki/" + page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find("div", class_="mw-body-content mw-content-ltr");
    links = []
    for link in div.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/wiki/') and not ':' in href: # la partie du lien après '/wiki/' pour obtenir les titres des pages liées
            var = href[6:]
            if var not in links:  # dans ce code nous évitons les doublons en ne stockant que les titres des pages uniques
                links.append(var)
    return links

#links = liste_liens("Petyr_Baelish")
#for link in links: 
#    print(link)
#for i, link in enumerate(links):#affiche de tous les liens dans la page(avec saut de ligne)
#    


# =========================== ##################### =============================================#
# Question 2 :
def svg_dico(dico, fichier):
    with open(fichier, 'w') as f: # On ouvre le fichier en mode écriture et on l'assigne à la variable 'f'
        f.write("{\n")
        for key, value in dico.items(): #  parcourir les clés et les valeurs du dico
            f.write(f' "{key}": {value},\n')
        f.write("}\n")
          
#svg_dico({'Petyr_Baelish': links}, 'file3.txt')



#=========================================#############################======================#
# Question 3 :
def chg_dico(fichier):
   with open(fichier, 'r') as f:
        lines = f.readlines() # mets toutes les lignes dans la variable "lines"
        dico = {}
        for line in lines:
            if ":" in line: # si il y a : dans la ligne alors on rentre :
                key, value = line.split(":") # on separe key,value avec split en mettant au milieu ":" comme separateur
                dico[key.strip()] = value.strip() # enleve les espace au debut et a la fin en ajoutant le couple clé:value dans le dico
        return dico

#dico = chg_dico('file.txt')


#================================#########################==========================#
# Question 4:
def parcours_graphe(start_page, file_name):
    visited = set() # set pour stocker les pages déjà visitées
    queue = [start_page] # queue pour stocker les pages à visiter, avec leur profondeur
    graph = {} # dictionnaire pour stocker le graphe
    
    while queue:
        page=queue.pop(0)
        if page in visited: # si la page a djà été visitée ou si on a atteint la profondeur maximale, on pss à la page svte
            continue
        
        visited.add(page) # on marque la page comme visitée
        links = liste_liens(page) # on récupère les liens de la page
        graph[page] = links # on ajoute les liens à la représentation du graphe
        
        for link in links:
            if link not in visited:
                queue.append(link) # on ajoute les pages liées à la queue, avec une profondeur supérieure
                
        svg_dico(graph, file_name) # on sauvegarde la représentation du graphe dans un fichier

#parcours_graphe("Petyr_Baelish","wiki3.txt")

#==================================########===============================#
# Question 5:
def plus_court_chemin(start_page, end_page, file_name):
    graph = chg_dico(file_name) # on charge le graphe à partir du fichier
    queue = [(start_page, [start_page])] # on commence la queue avec la page de départ
    visited = set() # set pour stocker les pages déjà visitées
    
    while queue: # on extrait le premier element de queue  et le stock dans page et path
        (page, path) = queue.pop(0)
        if page not in visited:
            visited.add(page)
            links = liste_liens(page) # on récupère les liens de la page
            graph[page] = links # on ajoute les liens à la représentation du graphe
            for link in graph[page]:
                if link == end_page:
                    return path + [end_page]  # concatène "path" avec une nouvelle liste contenant le sommet "end-page"
                elif link not in visited:
                    queue.append((link, path + [link]))
    return None

#chemin =plus_court_chemin("Dorne", "Bastard", "wiki.txt")
##print(chemin)
#res : ['Dorne', 'House_Targaryen', 'Rhaego']


#======================================########======================#
# Question 6:
def poids_lien(page):
        """Calcule le poids d'un lien vers la page donnée"""
        return sum(2 if c in "aeiouyAEIOUY" else 1 for c in page)

# def poids_chemin(chemin):
#         # Calcule le poids total du chemin.
#         poids = sum(poids_lien(page) for page in chemin[:-1]) # [:-1] exclusion du dernier élément de la liste
#         return poids

def liste_liens_poids(page):
    # Calcule la liste des liens sortants de la page avec leur poids.
    url = "https://iceandfire.fandom.com/wiki/" + page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find("div", class_="mw-body-content mw-content-ltr");
    links = set()
    for link in div.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/wiki/') and not ':' in href:
            var = href[6:]
            poids = poids_lien(var)
            links.add((var, poids))
    return links

def pcc_voyelles(start_page, end_page, page):
    graph = {} # dictionnaire pour stocker le graphe
    visited = set() # set pour stocker les pages déjà visitées
    queue = [(0, start_page, [])] # queue pour stocker les pages à visiter, avec leur poids et le chemin parcouru
    
    while queue:
        poids, page, chemin = min(queue, key=lambda x: x[0]) # on récupère la page avec le poids minimal
        queue.remove((poids, page, chemin)) # on l'enlève de la queue
        if page == end_page: # si on a atteint la page cible, on retourne le chemin
            return chemin + [page]
        if page in visited: # si la page a déjà été visitée, on passe à la suivante
            continue
        visited.add(page) # on marque la page comme visitée
        links = liste_liens_poids(page) # on récupère les liens sortants de la page
        graph[page] = links # on ajoute les liens à la représentation du graphe
        for link, poids_lien in links:
            if link not in visited:
                # on ajoute les pages liées à la queue, avec leur poids et le chemin parcouru
                queue.append((poids + poids_lien, link, chemin + [page]))
    
    return None


print(pcc_voyelles("Dorne", "Bastardy", "wiki.txt"))
#res : ['Dorne', 'Bastard', 'Ellaria_Sand', 'Bastardy']

#===========================================######========================#
# Question 7:


