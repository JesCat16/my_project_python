def aptdao(s,p):
    if s == "F" and p >= 50:
        return print("Está Apto!")
    elif s == "M" and p >= 60:
        return print("Está Apto!")
    else:
        return print("Não está apto")