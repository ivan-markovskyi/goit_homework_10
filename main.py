from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = list()
        if phone:
            self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def remove_phone(self, phone):
        self.phones.remove(phone)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return self.data


if __name__ == "__main__":
    name = Name("Bill")
    phone = Phone("1234567890")
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab["Bill"], Record)
    assert isinstance(ab["Bill"].name, Name)
    assert isinstance(ab["Bill"].phones, list)
    assert isinstance(ab["Bill"].phones[0], Phone)
    assert ab["Bill"].phones[0].value == "1234567890"
    print("All Ok)")
