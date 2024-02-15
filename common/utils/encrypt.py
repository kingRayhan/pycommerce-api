import bcrypt


def encrypt(text) -> str:
    # converting password to array of bytes
    text_bytes = text.encode('utf-8')

    # generating the salt
    salt = bcrypt.gensalt()

    return bcrypt.hashpw(text_bytes, salt).decode('utf-8')


def compare(text, hashed_text) -> bool:
    # converting password to array of bytes
    text_bytes = text.encode('utf-8')

    # converting hashed password to array of bytes
    hashed_text_bytes = hashed_text.encode('utf-8')

    return bcrypt.checkpw(text_bytes, hashed_text_bytes)
