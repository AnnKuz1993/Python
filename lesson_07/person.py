class Person:
    def __init__(self, attrs: dict): #конструктор, задаем атрибуты (словарь)
        self._attributes = attrs

    def __del__(self):               #деструктор, выводим сообщение об удалении объекта
        print("Person removed!")

    def __str__(self):               #приводим атрибуты к строковому значению
        return f"Person: {self._attributes['first_name']} {self._attributes['last_name']}"

    def __repr__(self):              #показ формального представления объекта
        return self.__str__()

    def __getitem__(self, item):     #ключ, который вытаскивает нужные элементы из атрибутов
        if item != 'age':            #ограничили доступ к атрибуту возраст (инкапсуляция)
            return self._attributes[item]
        else:
            return None

    def __setattr__(self, key, value):  #сохранение заново добавленных параметров в атрибуты
        if '_attributes' in self.__dict__: #список у текущего self экземпляра
            self._attributes[key] = value
        else:
            super().__setattr__(key, value) #иначе вызов родительских параметров

john = Person({"first_name": "John", "last_name": "Doe", "age": 30})
artur = Person({"first_name": "Artur", "last_name": "Doe", "age": 40})

#del john

users = [john, artur]
print(users)

print(john['first_name'])
print(artur['first_name'])
print(artur['age'])

john.job = "Developer"
print(john['job'])