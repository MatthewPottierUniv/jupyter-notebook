# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Séquence n°1 - Premiers pas sur Python
#
# ## 1) Variables et typage dynamique
#
# Ce document vous permettra de vous exercer en douceur au langage de programmation Python. Lorsque les cellules sont précédées de crochets [ ]:, cela signifie qu'il s'agit d'une cellue destiné à écrire du code.
# Afin d'exécuter ("Run", en anglais) les cellules, vous pouvez appuyer sur l'icone de lancement en forme de triangle ou bien utiliser le raccourci Ctrl + Entrée.
#
# Commençons !

# %%
# Commencer une ligne de code par un # vous permet d'insérer un commentaire qui ne sera pas pris en compte dans l'exécution de votre commande.
# C'est un moyen idéal de commenter chaque action et de ne pas se perdre ;)

# Que vous utilisiez IDLE, Jupyter ou VSCode, Python vous permet d'exécuter des calculs:
# En exécutant la cellule (Ctrl + Entrée), vous obtiendrez le résultat juste en-dessous !

2*2

# %% [markdown]
# Nous avons exécuté notre première ligne ! Maintenant, on souhaiterait sauvegarder ce résultat afin de ne pas le perdre. Pour cela, on crée une variable qui sauvegardera notre objet.

# %%
# Codons notre première variable et imprimons-la à l'aide de la commande print()
# Nous réalisons l'opération 2*2 et désirons sauvegarder le résultat.
# Pour ce faire, il est primordial d'utiliser une variable :

a = 2*2

# Seulement, rien ne s'affiche lorsqu'on exécute la cellule.

# %%
# En fait, la cellule précédente a bien été validée et la variable (a) créée.
# MAIS, nous n'avons pas demandé à Python de nous imprimer le résultat.

# Utilisons pour cela, la commande print()

print(a)

# D'ailleurs, vous noterez que ce document enregistre les résultats de bloc en bloc.
# Si vous n'avez pas exécuté le bloc précédent, vous devriez avoir un message d'erreur car en l'absence d'exécution, la variable (a) n'aura jamais été créée !
# Dans ce cas, revenez dans le bloc précédent et exécutez-le !

# %% [markdown]
# ### Opérations mathématiques simples et texte

# %%
# Addition
print(2+2)

# Soustraction
print(2-2)

# Multiplication (signe *)
print(2*2)

# Division (signe /)
print(2/2)

# %%
# Nous pouvons aussi travailler avec du texte brut dans Python. Pour le spécifier, on utilise les guillemets.

a = "ADiReO"
print(a)

# %% [markdown]
# ### Type et typage dynamique dans Python
#
# Chaque objet appartient à un type défini. Pour vérifier le type de votre variable, vous pouvez utiliser la commande type().

# %%
# type STR pour 'String' ou 'Chaîne de caractères"
a = "Bonjour à toutes et à tous !"
type(a)

# %%
# type INT pour 'Integer' ou 'Nombre entier'
a = 2
type(a)

# %%
# FLOAT pour 'Floating Point Number' ou 'Nombre flottant'
a = 2.5
type(a)

# Notez qu'il faut utiliser le point "." comme séparateur et non la virgule, cela ne fonctionnera pas !
# Si vous utilisez une virgule, Python considère qu'il s'agit d'un tuple et non d'un nombre décimal !

# %% [markdown]
# Nous avons de nombreux autres types natifs dans Python comme 'BOOL' pour "booléen", les tuples ou encore les listes. Nous verrons cela au fur et à mesure des séances.

# %% [markdown]
# Python est un langage de programmation qui permet notamment de modifier le type de l'objet
# C'est ce qu'on appelle le typage dynamique !

# %%
# Ici, la variable a est de type INT.
a = 3
print(type(a))

# Grâce à la commande STR, je souhaite modifier le type de la variable a en une chaîne de caractères, STR.
a = str(a)
print(type(a))

# %%
# Enfin, sachez que vous pouvez très bien faire des calculs entre des nombres INT et des nombres FLOAT

2*2.5

# %% [markdown]
# ### STR et concaténation
#
# L'un des avantages de Python est aussi de pouvoir imprimer directement votre variable à l'intérieur même d'une chaîne de caractères afin d'automatiser certains processus.

# %%
a = "Hélène"
b = "Martin"
print("Je m'appelle", a, b)

# %%
# On peut également concaténer des variables en un seule si nous avons besoin de les grouper.

a = "Hélène"
b = "Martin"

nom_entier = (a + b)
print(nom_entier)

# Pour ajouter l'espace entre le prénom et le nom, on peut ajouter un espace nous-mêmes.

nom_entier = (a + " " + b)
print(nom_entier)

# %% [markdown]
# ### Input
#
# Enfin, pour clôturer cette leçon, nous allons voir la fonction 'input' qui vous permet d'interroger un utilisateur afin de collecter des données. Dès que vous exécuterez cette commande, une zone de texte s'ouvrira afin de vous permettre de répondre.

# %%
input("Quel est votre prénom ?")

# %% [markdown]
# Notez que cette commande collectera toujours les données sous le type STR, y compris des données numériques ! C'est pourquoi le typage dynamique est si important en Python. Si vous avez envie d'opérer des statistiques sur les âges de vos utilisateur.rice.s, vous aurez besoin au préalable de modifier le type STR en INT ou FLOAT.

# %%
a = input("Quel est votre âge ?")

print(type(a))

# %% [markdown]
# Voici la fin de la première séance ! Vous aurez vu ici une base pratique afin de mettre en place les éléments présentés dans le cours. Vous trouverez sur l'ENT, une série d'exercices pour cette leçon qui vous permettra d'affiner vos premières connaissances !
