cidade = str(input("Em que cidade você nasceu: ")).strip()
if cidade[:5].upper() == "SANTO":
   print("Você nasceu em {}".format(cidade))
else:
    print("Você não nasceu em {}".format(cidade))
