from encrypt import encrypt
from decrypt import decrypt


def test_encrypt_decrypt_roundtrip():
    text = "hola mundo"
    key = "clave-super-secreta"

    iv, ciphertext = encrypt(text, key)
    plaintext = decrypt(ciphertext, key, iv)

    assert plaintext == text


def test_encrypt_returns_strings():
    iv, ciphertext = encrypt("abc", "key")

    assert isinstance(iv, str)
    assert isinstance(ciphertext, str)
    assert iv
    assert ciphertext


def test_decrypt_with_wrong_key_fails():
    text = "mensaje"
    key = "key-correcta"
    wrong_key = "key-incorrecta"

    iv, ciphertext = encrypt(text, key)

    try:
        decrypt(ciphertext, wrong_key, iv)
        assert False, "Decrypting with the wrong key should fail"
    except ValueError:
        assert True
