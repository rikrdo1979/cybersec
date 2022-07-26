#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "rikrdo"
__copyright__ = "Copyright 2022, Bootcamp Cybersec "
__credits__ = ["rikrdo"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "rikrdo"
__email__ = "rikrdo@rikrdo.es"
__status__ = "Production"

from cryptography.fernet import Fernet
 
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m' 

def write_key():
    # generamos ftp_otp.key
    key = Fernet.generate_key()
    with open("ftp_otp.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()
# generate and write a new key
write_key()
# opening the key
with open('ftp_otp.key', 'rb') as filekey:
    key = filekey.read()
# using the generated key
fernet = Fernet(key)
# opening the original file to encrypt
with open('nba.csv', 'rb') as file:
    original = file.read()
   
# encrypting the file
encrypted = fernet.encrypt(original)
# opening the file in write mode and
# writing the encrypted data
with open('nba.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g")
    parser.add_argument("-k")

    args = parser.parse_args()

    if args.g:
        key = args.g

    if args.l:
        if int(args.l) > 5:
            i = 5
        else:
            i = args.l
    else:
        i = 5
    if args.p:
        dirpath = args.p
    else:
        dirpath = "./data/"

    print("\n\033[93m ---------------------------------------------------------------- \033[0m\n")
    print (" URL:\t\033[1m"+ domain + "\033[0m")
    print (" Deep:\t\033[1m"+ str(i) + "\033[0m")
    print (" Path:\t\033[1m"+ dirpath + "\033[0m")
    print("\n\033[93m ---------------------------------------------------------------- \033[0m\n")
    find_links([domain], i, dirpath)

if __name__=="__main__":
    main()