Largura = int(input("digite a largura: "))
Altura = int(input("digite a altura: "))

print(Largura*"#")

while Altura > 2:
    print ("#", end="")
    x = Largura - 2
    print(x*" ",  end="")
    print ("#")
    Altura -=1

print(Largura*"#")




