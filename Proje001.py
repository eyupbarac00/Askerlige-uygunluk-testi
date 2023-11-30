yas = input("Kaç yaşındasınz?\n")
okul = input("Okuyor musunuz E/H\n")

if int(yas) < 18 and okul.upper() == "E" or "H":
    print("Askerlik için daha çok zamanın var :)")
elif int(yas) >= 18 and okul.upper() == "E":
    print("Okulun bitsin gelirsin aslanım ;)")
elif int(yas) >= 18 and okul.upper() == "H":
    print("En kısa zamanda bekleriz aslan parçası :D")
