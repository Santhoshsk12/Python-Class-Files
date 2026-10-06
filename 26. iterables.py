class OldPhone:
  def __init__(self, brand):
    self.brand = brand

  def call(self):
    print(f"{self.brand} is calling...")


class SmartPhone(OldPhone):
  def __init__(self, brand, os):
    super().__init__(brand)
    self.os = os  

  def browse(self):
    print(f"Browsing on {self.os} using my {self.brand}!")



my_phone = SmartPhone("Apple", "iOS")
my_phone.call()  # Apple is calling...
my_phone.browse()  # Browsing on iOS using my Apple!