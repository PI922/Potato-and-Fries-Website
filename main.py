import random
from os import system, name
def clear():
    if name == 'nt': 
       _ = system('cls')

    else:
       _ = system('clear')

door = random.randint (1,3)
dif = input("Welcome to the Potato and Fries Help Center.\nWhat would you like to do?\nP.S. Enter 1-3 to do what is on the list. \nType Chinese to translate to Chinese(Simplified).\nType Telugu to translate to Telugu. \nType German to translate to German.\nType Hindi to translate to Hindi.\nType Spanish to translate to 1. File a complaint\n2. File an work request\n3. Report a bug \n\n")

if dif == "1":
    st = input("File a complaint here:\nhttps://docs.google.com/forms/d/e/1FAIpQLSd-XwIF6C-Uwvad_Wkpf6184ZGjEv0dD0zgv31ZsZy9Nicb-g/viewform\nReload the site to report errors. ")

if dif == "2":
    st = input("First take time to go into here to buy a book:\nhttps://docs.google.com/presentation/d/1DdaJxPx5iqwCByY5Djjz2fg66Ls-i5Impg_bgdlwKcc/comment#slide=id.gc6f59039d_0_0\n\nAnd then take time to fill out this form:\nhttps://docs.google.com/forms/d/e/1FAIpQLSfvMeBGGaZE_vsgYZz-ZQHne7i6sWSBY_n785tVuXATAG766w/viewform\nReload the site to report errors.")

if dif == "3":
    st = input("Take time to fill out this form to report an error:\nhttps://docs.google.com/forms/d/e/1FAIpQLScixeMDROeSKIkyuW9uYaSy57p0qcZRtptrgRy8QVqZvhvJHw/viewform\nReload the site to report any other errors.")

if dif == "Chinese":
    st = input("欢迎来到马铃薯和薯条帮助中心。\n你想干什么？ \nP.S. 输入1-3以执行列表中需要执行的操作。\n1.提出投诉\n2.提出工作要求\n3.报告错误\n\n")

if dif == "Telugu":
    st = input("బంగాళాదుంప మరియు ఫ్రైస్ సహాయ కేంద్రానికి స్వాగతం. మేము మీకు ఏమి సహాయపడతాము? \n1. ఫిర్యాదును ఫైల్ చేయండి \n2. పని అభ్యర్థనను ఫైల్ చేయండి \n3. బగ్‌ను నివేదించండి")

if dif == "German":
    st = input("Willkommen in der Hilfe zu Kartoffeln und Pommes. Mit was können wir dir helfen? \n1. Eine Beschwerde einreichen \n2. Eine Arbeitsanforderung einreichen \n3. Einen Fehler melden")
    
if dif == "Hindi":
  st = input("आलू और आलू सहायता केंद्र में आपका स्वागत है। हम आपकी कैसे मदद कर सकते हैं? \n1. शिकायत दर्ज करें \n2. एक कार्य अनुरोध दर्ज करें \n3. एक बग रिपोर्ट करें")
  
if dif == "Spanish":
  st = input("Bienvenido al Centro de ayuda de Potato and Fries. ¿Qué podemos ayudarte? \n1. Presentar una queja \n2. Presentar una solicitud de trabajo \n3. Informar un error")
  
if dif == "French":
  st = input("Bienvenue dans le centre d'aide Pommes de terre et frites. En quoi pouvons-nous vous aider?\n 1. Déposer une plainte \n2. Déposer une demande de travail \n3. Signaler un bogue")

if dif == "":
  st = input("")