class Personas:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


def ListasPersonas():
    li = []
    li2 = []

    li.append(Personas('Camilo', 23))
    li.append(Personas('Alejandra', 33))
    li.append(Personas('Ana', 20))
    li.append(Personas('Andres', 17))
    li.append(Personas('Miguel', 9))
    li.append(Personas('Mari', 5))

    for i in li:
        if i.age > 18:
            li2.append(i.name)
            li2.append(i.age)
    print(li2)

ListasPersonas()