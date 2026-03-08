from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Tecno", "10", "+79490076312"))
catalog.append(Smartphone("Honor", "View 10", "+79637310839"))
catalog.append(Smartphone("Xiaomi", "Poco M7", "+79995553322"))
catalog.append(Smartphone("Samsung", "Galaxy S25", "+79815097946"))
catalog.append(Smartphone("Apple", "Iphone 17 pro", "+79125159673"))

for item in catalog:
    print(item)