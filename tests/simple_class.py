from logerator import before_and_after
class SimpleClass:
    _first_name = ''
    _last_name = ''
    _pet_name = ''
    _breed = ''
    _this = None

    def __init__(self, first_name, last_name, pet_name, breed):
        self._first_name = first_name
        self._last_name = last_name
        self._pet_name = pet_name
        self._breed = breed

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value


    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value


    @property
    def pet_name(self):
        return self._pet_name

    @pet_name.setter
    def pet_name(self, value):
        self._pet_name = value


    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        self._breed = value

    @before_and_after
    def save(self):
        print ("I am saving {} {} {} {}".format(self.first_name, self.last_name, self.pet_name, self.breed))
        return