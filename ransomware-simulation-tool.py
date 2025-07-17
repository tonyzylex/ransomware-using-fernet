from cryptography.fernet import Fernet
import os 

file_path = "c:/Users/topiary/Documents/tester path/testtxt.txt"
if os.path.exists(file_path):

        key = Fernet.generate_key()
        with open('c:/Users/topiary/Documents/tester path/secretkey.txt', 'wb') as key_file:
            key_file.write(key)

        def load_key():
             return open ('c:/Users/topiary/Documents/tester path/secretkey.txt', 'rb').read()
        



        def encrypt_file(filename):
            key = load_key()
            fernet = Fernet(key)
            with open(filename, 'rb') as file:
                 original_Data = file.read()
                 encrypted_Data = fernet.encrypt(original_Data)

            with open(filename,'wb') as file:
                 file.write(encrypted_Data)
        encrypt_file(file_path)
                
else:
    print('file doesnt exist')




# def create_key():
#             key = Fernet.generate_key()
#             with open('secret.key', 'wb') as key_file:
#                 key_file.write(key)

# def load_key():
#              return open ('c:/Users/topiary/Documents/tester path/secretkey.txt', 'rb').read()
        


# def encrypt_file(filename):
#             key = load_key()
#             fernet = Fernet(key)
#             with open(filename, 'rb') as file:
#                  original_Data = file.read()
#                  encrypted_Data = fernet.encrypt(original_Data)

#             with open(filename,'wb') as file:
#                  file.write(encrypted_Data)
# encrypt_file('c:/Users/topiary/Documents/tester path/testtxt.txt')