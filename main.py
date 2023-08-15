from collections import UserDict


class Name:
    def __init__(self, name):
        self.name = name


class Phone:
    def __init__(self, value):
        self.value = value


class Record:
    def __init__(self, name: Name, *args):
        self.name = name
        self.phones = list(args)

    def add_phone(self, phone):
        phone_num = Phone(phone)
        if phone_num not in self.phones:
            self.phones.append(phone_num)

    def change_phone(self, old_phone, new_phone):
        # new_phones = list(map(lambda x: x.replace(old_phone, new_phone), self.phones))
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def remove_phone(self, phone):
        self.phones.remove(phone)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.name] = record
        return self.data


class Field:
    pass


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
