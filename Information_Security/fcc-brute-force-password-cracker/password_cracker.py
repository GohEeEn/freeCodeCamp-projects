import hashlib


def crack_sha1_hash(hash, use_salts=False):

    with open("top-10000-passwords.txt", 'rb') as wordlist:
        dictionary = wordlist.readlines()

    if(use_salts):  # Salted
        with open("known-salts.txt", 'rb') as saltlist:
            salts = saltlist.readlines()
        for word in dictionary:
            for salt in salts:
                appended_word = salt.strip() + word.strip()
                appended_hash = hashlib.sha1(appended_word).hexdigest()
                prepended_word = word.strip() + salt.strip()
                prepended_hash = hashlib.sha1(prepended_word).hexdigest()
                if(appended_hash == hash or prepended_hash == hash):
                    return word.strip().decode('utf-8')
    else:  # Unsalted
        for word in dictionary:
            current_hash = hashlib.sha1(word.strip()).hexdigest()
            if(current_hash == hash):
                return word.strip().decode('utf-8')

    return("PASSWORD NOT IN DATABASE")
