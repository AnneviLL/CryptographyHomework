import sys
# import os


def encrypt():
    m = input("请输入明文m: ")
    k = input("请输入密钥k: ")
    k = int(k)
    if not isinstance(k,int):
        print("密钥输入有误。")
        exit(1)
    d = 0
    d1 = 0
    c = ''
    for i in m:
        d = ord(i)-ord('a')
        # print(d)
        d1 = (d + k) % 26
        c += chr(d1+ord('a'))
    print("加密结果: \n" + c + '\n')
    main()

def decrypt():
    c = input("请输入密文: ")
    k = input("请输入密钥: ")
    k = int(26-int(k))
    if not isinstance(k,int):
        print("密钥输入有误。")
        exit(1)
    d = 0
    d1 = 0
    m = ''
    for i in c:
        d = ord(i)-ord('a')
        # print(d)
        d1 = (d + k) % 26
        m += chr(d1+ord('a'))
    print("解密结果: \n" + m + '\n')
    main()

def main():
    select = input("功能选择:\n1. 加密\n2. 解密\n")
    print("")
    if select is '1':
        encrypt()
    elif select is '2':
        decrypt()

print("""
     ____                           
    / ___|__ _  ___  ___  __ _ _ __ 
    | |   / _` |/ _ \/ __|/ _` | '__|
    | |__| (_| |  __/\__ \ (_| | |   
    \____\__,_|\___||___/\__,_|_|   
    """)
main()