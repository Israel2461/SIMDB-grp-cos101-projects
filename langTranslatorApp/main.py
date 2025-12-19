from languages.ebira import translate as ebira_lang
# from languages.yoruba import translate as yoruba_lang
from languages.igbo import translate as igbo_lang
# from languages.hausa import translate as hausa_lang
from languages.calabar import translate as calabar_lang


while True:
    print("WELCOME TO SIMDB TRANSLATOR APP")
    print("Choose the language you want to translate to below:")
    print("1. Ebira")
    print("2. Igbo")
    print("3. Hausa")
    print("4. Yoruba")
    print("5. Calabar")
    print("6. Exit")

    choice = int(input("Enter your choice: (1-5)\n"))
    if choice == 1:
        word = input("Enter the word in english: ")
        print(ebira_lang(word))
    elif choice == 2:
        word = input("Enter the word in english: ")
        print(igbo_lang(word))
    elif choice == 3:
        word = input("Enter the word in english: ")
        # print(hausa_lang(word))
    elif choice == 4:
        word = input("Enter the word in english: ")
        # print(yoruba_lang(word))
    elif choice == 5:
        word = input("Enter the word in english: ")
        print(calabar_lang(word))
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Please enter a valid choice!")