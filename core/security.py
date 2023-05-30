from passlib.context import CryptContext

CRYPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(password: str, hash_password: str) -> bool:
    """
    Verify if the provided password matches the given hash password.

    Args:
        password (str): The plain text password to verify.
        hash_password (str): The hashed password to compare against.

    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    return CRYPTO.verify(password, hash_password)


def generate_hash_password(password: str) -> str:
    """
    Generate a hash for the provided password.

    Args:
        password (str): The plain text password to hash.

    Returns:
        str: The hashed password.
    """
    return CRYPTO.hash(password)
