class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        password_set = set(password)
        if len(password) < 8:
            return False
        if not set(ascii_lowercase).intersection(password_set):
            return False
        if not set(ascii_uppercase).intersection(password_set):
            return False
        if not set(digits).intersection(password_set):
            return False
        if not {
            "!", "@", "#", "$",
            "%", "^", "&", "*",
            "(", ")", "-", "+",
            }.intersection(password_set):
            return False
        for i in range(1, len(password)):
            if password[i] == password[i - 1]:
                return False
        
        return True
        
