class customer():
    def __init__(self, id, first_name=None, last_name=None, phone=None, email=None, address=None) -> None:
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.email=email
        self.address=address

    def to_JSON(self):
        return{
            'id' : self.id,
            'fisrt_name' : self.first_name,
            'last_name' : self.last_name,
            'phone' : self.phone,
            'email' : self.email,
            'address' : self.address
        }