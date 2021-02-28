import random
from os import system, name
def clear():
    if name == 'nt': 
       _ = system('cls')

    else:
       _ = system('clear')

door = random.randint (1,3)
dif = input("Welcome to the Potato and Fries Help Center. What would you like to do?\nP.S. Enter 1-3 to do what is on the list. \n1. File a complaint\n2. File an work request\n3. Report a bug \n\n")

if dif == "1":
    st = input("")

if dif == "2":
    st = input("First take time to go into here to buy a book:\nhttps://docs.google.com/presentation/d/1DdaJxPx5iqwCByY5Djjz2fg66Ls-i5Impg_bgdlwKcc/comment#slide=id.gc6f59039d_0_0\n\nAnd then take time to fill out this form:\nhttps://docs.google.com/forms/d/e/1FAIpQLSfvMeBGGaZE_vsgYZz-ZQHne7i6sWSBY_n785tVuXATAG766w/viewform\nReload the site to report other errors.")

if dif == "3":
    st = input("")