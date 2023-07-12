tipo_1 = str(input())
tipo_2 = str(input())
tipo_3 = str(input())

dicionario = {
    ("vertebrado","ave","carnivoro"):"aguia",
    ("vertebrado","ave","onivoro"):"pomba",
    ("vertebrado","mamifero","onivoro"):"homem",
    ("vertebrado","mamifero","herbivoro"):"vaca",
    ("invertebrado","inseto","hematofago"):"pulga",
    ("invertebrado","inseto","herbivoro"):"lagarta",
    ("invertebrado","anelideo","hematofago"):"sanguessuga",
    ("invertebrado","anelideo","onivoro"):"minhoca",
}

animal = dicionario.get((tipo_1,tipo_2,tipo_3))
print(animal)

