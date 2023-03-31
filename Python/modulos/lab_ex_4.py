from string_hifen import ordem, max, mini

def main():
    p=input("Digite as palavras desejadas separando-as por hífen(-): ")
    ordem(p)
    print("Maiúsculas = ",max(p))
    print("Minúsculas = ",mini(p))

if __name__ == "__main__":
    main()