class Password:
    def __init__(self, password=""):
        self.password = password
        self.valid_length = False
        self.alnum_only = False
        self.one_alnum = False
    
    def check_length(self):
        if (len(self.password) >= 8 and len(self.password) <= 12):
            self.valid_length = True
    
    def check_alnum_presence(self):
        non_alnum = [character for character in self.password if not character.isalnum()]
        if len(non_alnum) == 0:
            self.alnum_only = True
    
    def check_alnum_length(self):
        digit, letter = 0, 0

        for character in self.password:
            if character.isdigit():
                digit += 1
            if character.isalpha():
                letter += 1
        if digit > 0 and letter > 0:
            self.one_alnum = True
            
    def is_valid_length(self):
        return self.valid_length
    
    def is_alnum_only(self):
        return self.alnum_only
    
    def is_one_alnum(self):
        return self.one_alnum
    
    def is_valid_password(self):
        return self.is_valid_length() and self.is_alnum_only() and self.is_one_alnum()
            
    def valid_length_error(self):
        return "Error: The password must have at least 8 characters and at most 12 characters.\n"
            
    def alnum_only_error(self):
        return "Error: The password must consist of only letters and digits.\n"
            
    def one_alnum_error(self):
        return "Error: The password must contain at least one letter and one digit.\n"
    
    def compile_errors(self):
        message = ""
        if not self.is_valid_length():
            message += self.valid_length_error()
        if not self.is_alnum_only():
            message += self.alnum_only_error()
        if not self.is_one_alnum():
            message += self.one_alnum_error()
        return (False, message)
                
    def validation(self):
        self.check_length()
        self.check_alnum_presence()
        self.check_alnum_length()
        
    def validate_password(self):  
        self.validation()
        
        if self.is_valid_password():
            message = "Password has been validated successfully."
            return (True, message)
        else:
            return self.compile_errors()
    
    def verify_password(self, password):
        if self.password == password:
            return True
        else:
            return False