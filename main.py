class Users:
    def __init__(self):
        self.users = []

    def register_user(self, username, password, role):
        self.users.append({
            'username': username,
            'password': password,
            'role': role
        })

    def get_user_by_username(self, username):
        for user in self.users:
            if user['username'] == username:
                return user
        return None

    def update_user_data(self, username, new_data):
        user = self.get_user_by_username(username)
        if user:
            user.update(new_data)

    def remove_user(self, username):
        user = self.get_user_by_username(username)
        if user:
            self.users.remove(user)


class Cars:
    def __init__(self):
        self.cars = []

    def add_car(self, brand, model, year, color, price, features):
        self.cars.append({
            'brand': brand,
            'model': model,
            'year': year,
            'color': color,
            'price': price,
            'features': features
        })

    def remove_car(self, brand, model):
        for car in self.cars:
            if car['brand'] == brand and car['model'] == model:
                self.cars.remove(car)
                break

    def get_all_cars(self):
        return self.cars

    def filter_cars(self, keyword):
        filtered_cars = []
        for car in self.cars:
            if keyword.lower() in car['model'].lower() or keyword.lower() in car['brand'].lower():
                filtered_cars.append(car)
        return filtered_cars


class Orders:
    def __init__(self):
        self.orders = []

    def add_order(self, username, car):
        self.orders.append({
            'username': username,
            'car': car
        })

    def remove_order(self, username, car):
        for order in self.orders:
            if order['username'] == username and order['car'] == car:
                self.orders.remove(order)
                break

    def get_user_orders(self, username):
        user_orders = []
        for order in self.orders:
            if order['username'] == username:
                user_orders.append(order)
        return user_orders


class Database:
    def __init__(self):
        self.users = Users()
        self.cars = Cars()
        self.orders = Orders()

    def register_user(self, username, password, role):
        self.users.register_user(username, password, role)

    def login_user(self, username, password):
        user = self.users.get_user_by_username(username)
        if user and user['password'] == password:
            return user
        return None

    def add_car(self, brand, model, year, color, price, features):
        self.cars.add_car(brand, model, year, color, price, features)

    def remove_car(self, brand, model):
        self.cars.remove_car(brand, model)

    def get_all_cars(self):
        return self.cars.get_all_cars()

    def filter_cars(self, keyword):
        return self.cars.filter_cars(keyword)

    def add_order(self, username, car):
        self.orders.add_order(username, car)

    def remove_order(self, username, car):
        self.orders.remove_order(username, car)

    def get_user_orders(self, username):
        return self.orders.get_user_orders(username)


def main():
    database = Database()

    while True:
        print("Добро пожаловать!")
        print("1. Зарегистрироваться")
        print("2. Вход в аккаунт")
        print("3. Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            username = input("Введите имя: ")
            password = input("Введите пароль: ")
            role = input("Выберите роль (1 - Клиент, 2 - Сотрудник, 3 - Администратор): ")

            if role == '1':
                role = 'Клиент'
            elif role == '2':
                role = 'Сотрудник'
            elif role == '3':
                role = 'Администратор'

            database.register_user(username, password, role)
            print("Регистрация прошла успешно!")

        elif choice == '2':
            username = input("Введите имя: ")
            password = input("Введите пароль: ")

            user = database.login_user(username, password)

            if user:
                print(f"Добро пожаловать, {user['username']} ({user['role']})!")

                if user['role'] == 'Клиент':
                    while True:
                        print("\n Выберите действие:")
                        print("1. Просмотреть все автомобили")
                        print("2. Фильтрующие машины")
                        print("3. Добавить автомобиль в заказ")
                        print("4. Снять автомобиль с заказа")
                        print("5. Обновлять пользовательские данные")
                        print("6. Выход")

                        customer_choice = input("Выберите действие: ")

                        if customer_choice == '1':
                            cars = database.get_all_cars()
                            if cars:
                                print("\nДоступные автомобили:")
                                for car in cars:
                                    print(f"  - {car['brand']} {car['model']}")
                            else:
                                print("\nСвободных машин нет.")

                        elif customer_choice == '2':
                            keyword = input("Введите ключевое слово для фильтрации автомобилей: ")
                            filtered_cars = database.filter_cars(keyword)
                            if filtered_cars:
                                print(f"\nАвтомобили, соответствующие фильтру '{keyword}':")
                                for car in filtered_cars:
                                    print(f"  - {car['brand']} {car['model']}")
                            else:
                                print("\nНет машин, подходящих под фильтр.")

                        elif customer_choice == '3':
                            brand = input("Введите марку автомобиля: ")
                            model = input("Введите модель автомобиля: ")
                            database.add_order(username, f"{brand} {model}")
                            print("Автомобиль добавлен к заказу.")

                        elif customer_choice == '4':
                            brand = input("Введите марку автомобиля: ")
                            model = input("Введите модель автомобиля: ")
                            database.remove_order(username, f"{brand} {model}")
                            print("Автомобиль снят с заказа.")

                        elif customer_choice == '5':
                            new_username = input("Введите новое имя пользователя: ")
                            database.update_user_data(username, {'username': new_username})
                            print(" Пользовательские данные успешно обновлены.")

                        elif customer_choice == '6':
                            break

                        else:
                            print(" Неверный выбор. Пожалуйста, попробуйте снова.")

                elif user['role'] == 'Сотрудник':
                            while True:
                                print("\n Выберите действие:")
                                print("1. Просмотреть все автомобили")
                                print("2. Фильтрующие машины")
                                print("3. Добавить автомобиль")
                                print("4. Снять автомобиль")
                                print("5. Обновлять пользовательские данные")
                                print("6. Выход")

                                employee_choice = input("Выберите действие: ")

                                if employee_choice == '1':
                                    cars = database.get_all_cars()
                                    if cars:
                                        print("\nДоступные автомобили:")
                                        for car in cars:
                                            print(f"  - {car['brand']} {car['model']}")
                                    else:
                                        print("\nСвободных машин нет.")

                                elif employee_choice == '2':
                                    keyword = input("Введите ключевое слово для фильтрации автомобилей: ")
                                    filtered_cars = database.filter_cars(keyword)
                                    if filtered_cars:
                                        print(f"\nАвтомобили, соответствующие фильтру '{keyword}':")
                                        for car in filtered_cars:
                                            print(f"  - {car['brand']} {car['model']}")
                                    else:
                                        print("\nНет машин, подходящих под фильтр.")

                                elif employee_choice == '3':
                                    brand = input("Введите марку автомобиля: ")
                                    model = input("Введите модель автомобиля: ")
                                    year = input("Введите год выпуска автомобиля: ")
                                    color = input("Введите цвет автомобиля: ")
                                    price = input("Введите цену автомобиля: ")
                                    features = input("Введите характеристики автомобиля (через запятую): ")

                                    database.add_car(brand, model, year, color, price, features)
                                    print(" Автомобиль успешно добавлен.")

                                elif employee_choice == '4':
                                    brand = input("Введите марку автомобиля: ")
                                    model = input("Введите модель автомобиля: ")

                                    database.remove_car(brand, model)
                                    print(" Автомобиль успешно удален.")

                                elif employee_choice == '5':
                                    new_username = input("Введите новое имя пользователя: ")
                                    database.update_user_data(username, {'username': new_username})
                                    print(" Пользовательские данные успешно обновлены.")

                                elif employee_choice == '6':
                                    break

                                else:
                                    print(" Неверный выбор. Пожалуйста, попробуйте снова.")

                elif user['role'] == 'Администратор':
                        while True:
                                print("\n Выберите действие:")
                                print("1. Просмотреть все автомобили")
                                print("2. Фильтрующие машины")
                                print("3. Добавить автомобиль")
                                print("4. Снять автомобиль")
                                print("5. Обновлять пользовательские данные")
                                print("6. Удалить пользователя")
                                print("7. Выход")

                                admin_choice = input("Выберите действие: ")

                                if admin_choice == '1':
                                    cars = database.get_all_cars()
                                    if cars:
                                        print("\nДоступные автомобили:")
                                        for car in cars:
                                            print(f"  - {car['brand']} {car['model']}")
                                    else:
                                        print("\nСвободных машин нет.")

                                elif admin_choice == '2':
                                    keyword = input("Введите ключевое слово для фильтрации автомобилей: ")
                                    filtered_cars = database.filter_cars(keyword)
                                    if filtered_cars:
                                        print(f"\nАвтомобили, соответствующие фильтру '{keyword}':")
                                        for car in filtered_cars:
                                            print(f"  - {car['brand']} {car['model']}")
                                    else:
                                        print("\nНет машин, подходящих под фильтр.")

                                elif admin_choice == '3':
                                    brand = input("Введите марку автомобиля: ")
                                    model = input("Введите модель автомобиля: ")
                                    year = input("Введите год выпуска автомобиля: ")
                                    color = input("Введите цвет автомобиля: ")
                                    price = input("Введите цену автомобиля: ")
                                    features = input("Введите характеристики автомобиля (через запятую): ")

                                    database.add_car(brand, model, year, color, price, features)
                                    print(" Автомобиль успешно добавлен.")

                                elif admin_choice == '4':
                                    brand = input("Введите марку автомобиля: ")
                                    model = input("Введите модель автомобиля: ")

                                    database.remove_car(brand, model)
                                    print(" Автомобиль успешно удален.")

                                elif admin_choice == '5':
                                    new_username = input("Введите новое имя пользователя: ")
                                    database.update_user_data(username, {'username': new_username})
                                    print(" Пользовательские данные успешно обновлены.")

                                elif admin_choice == '6':
                                    remove_username = input("Введите имя пользователя для удаления: ")
                                    database.remove_user(remove_username)
                                    print(" Пользователь успешно удален.")

                                elif admin_choice == '7':
                                    break

                                else:
                                    print(" Неверный выбор. Пожалуйста, попробуйте снова.")

            else:
                print("Неверное имя пользователя или пароль. Пожалуйста, попробуйте снова.")

        elif choice == '3':
            print(" До свидания!")
            break

        else:
            print(" Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
