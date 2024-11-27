import hashlib

# Simulated hash_password function for SHA256 hashing
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Stored logins where email is the key and the hashed password is the value
stored_logins = {
    "user@example.com": hash_password("mypassword123"),
    "admin@example.com": hash_password("adminpass")
}

def login(email: str, password_to_check: str) -> bool:
    # Check if the email exists in the stored logins
    if email in stored_logins:
        # Hash the password entered by the user
        hashed_password_to_check = hash_password(password_to_check)
        
        # Compare the hashed password with the stored one
        if hashed_password_to_check == stored_logins[email]:
            return True
        else:
            return False
    else:
        return False

# Example usage:
print(login("user@example.com", "mypassword123"))  # Should return True
print(login("user@example.com", "wrongpassword"))  # Should return False
print(login("admin@example.com", "adminpass"))     # Should return True
print(login("admin@example.com", "wrongadmin"))    # Should return False
