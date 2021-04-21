class Entity:
    def __init__(self):
        self.__name__ = ''
        self._phone = ''
        self._email = ''
        self._addr = ''

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def addr(self) -> str:
        return self._addr

    @addr.setter
    def addr(self, addr):
        self._addr = addr

    def to_string(self):
        return f'이름 {self._name}, 전화번호 {self._phone}, 이메일 {self._email}, 주소 {self._addr}'


class Service:
    def __init__(self):
        self._contacts = []

    def add_contact(self, payload):
        self._contacts.append(payload)

    def get_contacts(self):
        contacts = []
        for i in self._contacts:
            contacts.append(i.to_string())
        return ' '.join(contacts)

    def del_contact(self, name):
        for i, t in enumerate(self._contacts):
            if t.name == name:
                del self._contacts[i]


class Controller:
    def __init__(self):
        self.service = Service()

    def register(self,name, phone, email, addr ):
        entity = Entity()
        entity.name = name
        entity.phone = phone
        entity.email = email
        entity.addr = addr

        self.service.add_contact(entity)

    def list(self):
        return self.service.get_contacts()

    def remove(self, name):
        self.service.del_contact(name)


if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 등록')
        print('2. 목록')
        print('3. 삭제')
        return input('메뉴 선택 \n')


    app = Controller()
    while 1:
        menu = print_menu()
        if menu == '0':
            break
        if menu == '1':
            app.register(input('이름\n'),input('전화번호\n'),input('이메일\n'),input('주소\n'))
        if menu == '2':
            print(app.list())
        if menu == '3':
            app.remove(input('이름\n'))
        elif menu == '0':
            break
