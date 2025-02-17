from Password import *

class StrongPassword(Password):
    def __init__(self, password):
        super().__init__(password)
        self.uppercase = False
        self.lowercase = False
        
    def check_length(self):
        if len(self.password) >= 12:
            self.valid_length = True
            
    def check_uppercase(self):
        for character in self.password:
            if character.isupper():
                self.uppercase = True
                
    def check_lowercase(self):
        for character in self.password:
            if character.islower():
                self.lowercase = True
            
    def is_uppercase(self):
        return self.uppercase
    
    def is_lowercase(self):
        return self.lowercase
            
    def valid_length_error(self):
        return "Error: The password must have at least 12 characters.\n"
            
    def uppercase_error(self):
        return "Error: The password must include uppercase characters.\n"
            
    def lowercase_error(self):
        return "Error: The password must include lowercase characters.\n"
        
    def is_valid_password(self):
        return self.is_valid_length() and self.is_alnum_only() and self.is_one_alnum() and self.is_uppercase() and self.is_lowercase()
        
    def compile_errors(self):
        message = ""
        if not self.is_valid_length():
            message += self.valid_length_error()
        if not self.is_alnum_only():
            message += self.alnum_only_error()
        if not self.is_one_alnum():
            message += self.one_alnum_error()
        if not self.is_uppercase():
            message += self.uppercase_error()
        if not self.is_lowercase():
            message += self.lowercase_error()
        return (False, message)
        
    def validation(self):
        self.check_length()
        self.check_alnum_presence()
        self.check_alnum_length()
        self.check_uppercase()
        self.check_lowercase()