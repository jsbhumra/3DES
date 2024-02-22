''' Done by Jagjit Singh Bhumra, Praneel Bora, Dhruv Dedhia '''
import string, random
import tkinter as tk
from tkinter import messagebox

class getInput:
    def strToBin(userIn):
        userBin = ''.join(format(ord(i), '08b') for i in userIn)
        extra = (64-len(userBin)%64)
        if (extra==64):
            extra = 0
        newBin = userBin
        for i in range(extra):
            k = str(random.randint(0,1))
            newBin = newBin + k
        return newBin

    def binToStr(binIn):
        newStr = ''
        for i in range(0,len(binIn),8):
            temp1 = binIn[i:i+8]
            decTemp = int(temp1,2)
            newStr = newStr + chr(decTemp)
        return newStr


    def binToArr(newBin):
        list = []
        for i in range(int(len(newBin)/64)):
            str = ''
            for j in range(64*i,(64*i)+64):
                str = str+ newBin[j]
            list.append(str)
        return list


class getKey:
    def keytoBin(userKey):
        UserKeyBin = ''.join(format(ord(i), '08b') for i in userKey)
        newKey = ''
        for i in range(64):
            newKey = newKey + UserKeyBin[i]
        return newKey

    def keySeed(newKey):
        perm1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
        newKey_56 = ''
        C = []
        D = []
        for i in perm1:
            newKey_56 = newKey_56 + newKey[i-1]
        C.append(newKey_56[:28])
        D.append(newKey_56[28:])
        return C, D

    def keyGen(C,D):
        perm2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
        lshift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        K = ['' for i in range(16)]
        E = []
        for i in range(1,17):
            temp1 = ''
            temp2 = ''
            for j in range(28):
                t = j+lshift[i-1]
                if (t>15):
                    t -= 16
                temp1 = temp1 + C[i-1][t]
                temp2 = temp2 + D[i-1][t]
            temp = temp1 + temp2
            C.append(temp1)
            D.append(temp2)
            E.append(temp)
        for i in range(16):
            for j in perm2:
                K[i] = K[i] + E[i][j-1]
        return K

class des:
    def initPerm(binStr):
        initialperm = [58, 50, 42, 34, 26, 18, 10, 2,
                       60, 52, 44, 36, 28, 20, 12, 4,
                       62, 54, 46, 38, 30, 22, 14, 6,
                       64, 56, 48, 40, 32, 24, 16, 8,
                       57, 49, 41, 33, 25, 17,  9, 1,
                       59, 51, 43, 35, 27, 19, 11, 3,
                       61, 53, 45, 37, 29, 21, 13, 5,
                       63, 55, 47, 39, 31, 23, 15, 7]
        newStr = ''
        L = []
        R = []
        for i in initialperm:
            newStr = newStr + binStr[i-1]
        L.append(newStr[:32])
        R.append(newStr[32:])
        return L, R

    def firstStep(binStr,roundKey):
        expan = [32,  1,  2,  3,  4,  5,
                 4,  5,  6,  7,  8,  9,
                 8,  9, 10, 11, 12, 13,
                 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21,
                 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29,
                 28, 29, 30, 31, 32,  1]
        tempE = ''
        E = ''
        for i in expan:
            tempE = tempE + binStr[i-1]
        for i in range(len(tempE)):
            if tempE[i] == roundKey[i]:
                E = E + '0'
            else:
                E = E + '1'
        return E

    def subBoxes(E):
        S = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
             [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
             [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
             [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
             [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
             [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
             [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
             [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
        newPerm = [16,  7, 20, 21,
                   29, 12, 28, 17,
                    1, 15, 23, 26,
                    5, 18, 31, 10,
                    2,  8, 24, 14,
                   32, 27,  3,  9,
                   19, 13, 30,  6,
                   22, 11,  4, 25]
        initB = []
        B = ''
        newB = ''
        for i in range(0,48,6):
            initB.append(E[i:i+6])
        for i in range(0,8):
            r = int(initB[i][0])*2 + int(initB[i][5])
            c = int(initB[i][4]) + int(initB[i][3])*2 + int(initB[i][2])*4 + int(initB[i][1])*8
            t = S[i][r][c]
            t = str(bin(t))[2:]
            while (len(t)!=4):
                t = '0' + t
            B = B + t
        for i in newPerm:
            newB = newB + B[i-1]
        return newB

    def exor(L,R,B,roundNum):
        newR = ''
        for j in range(len(B)):
            if L[roundNum-1][j] == B[j]:
                newR = newR + '0'
            else:
                newR = newR + '1'
        R.append(newR)
        L.append(R[roundNum-1])
        return L, R

    def finalPerm(newLine):
        finalPermutation = [40,  8, 48, 16, 56, 24, 64, 32,
                            39,  7, 47, 15, 55, 23, 63, 31,
                            38,  6, 46, 14, 54, 22, 62, 30,
                            37,  5, 45, 13, 53, 21, 61, 29,
                            36,  4, 44, 12, 52, 20, 60, 28,
                            35,  3, 43, 11, 51, 19, 59, 27,
                            34,  2, 42, 10, 50, 18, 58, 26,
                            33,  1, 41,  9, 49, 17, 57, 25]
        encrpytText = ''
        for i in finalPermutation:
            encrpytText = encrpytText + newLine[i-1]
        return encrpytText

def encryptDES(K,blockArr):
    cipherText = ''
    blockNum = len(blockArr)
    for num in range(blockNum):
        L, R = des.initPerm(blockArr[num])
        for roundNum in range(1,17):
            E = des.firstStep(R[roundNum-1], K[roundNum-1])
            B = des.subBoxes(E)
            L,R = des.exor(L, R, B, roundNum)
        newLine = R[16] + L[16]
        encryptText = des.finalPerm(newLine)
        cipherText = cipherText + encryptText
    return cipherText

def decryptDES(K,blockArr):
    blockNum = len(blockArr)
    plainText = ''
    for num in range(blockNum):
        L, R = des.initPerm(blockArr[num])
        for roundNum in range(1,17):
            E = des.firstStep(R[roundNum-1], K[16-roundNum])
            B = des.subBoxes(E)
            L,R = des.exor(L, R, B, roundNum)
        newLine = R[16] + L[16]
        encryptText = des.finalPerm(newLine)
        plainText = plainText + encryptText
    return plainText

class DESGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DES Encryption and Decryption")

        self.root.geometry("600x300")

        self.key_label0 = tk.Label(root, text="Enter Key 1:")
        self.key_entry0 = tk.Entry(root, show='*')
        self.key_label0.pack()
        self.key_entry0.pack()

        self.key_label1 = tk.Label(root, text="Enter Key 2:")
        self.key_entry1 = tk.Entry(root, show='*')
        self.key_label1.pack()
        self.key_entry1.pack()

        self.key_label2 = tk.Label(root, text="Enter Key 3:")
        self.key_entry2 = tk.Entry(root, show='*')
        self.key_label2.pack()
        self.key_entry2.pack()

        self.text_label = tk.Label(root, text="Enter Data:\n(Text for encryption and Binary for decryption)")
        self.text_entry = tk.Entry(root)
        self.text_label.pack()
        self.text_entry.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt)
        self.encrypt_button.pack()
        self.decrypt_button.pack()

        self.toggle_button = tk.Button(root, text="Toggle Key Visibility", command=self.toggle_password)
        self.toggle_button.pack()

    def toggle_password(self):
        current_show_state0 = self.key_entry0.cget("show")
        current_show_state1 = self.key_entry1.cget("show")
        current_show_state2 = self.key_entry2.cget("show")
        new_show_state0 = "" if current_show_state0 else "*"
        new_show_state1 = "" if current_show_state1 else "*"
        new_show_state2 = "" if current_show_state2 else "*"
        self.key_entry0.config(show=new_show_state0)
        self.key_entry1.config(show=new_show_state1)
        self.key_entry2.config(show=new_show_state2)


    def encrypt(self):
        userKey = ['','','']
        key0 = self.key_entry0.get()
        key1 = self.key_entry1.get()
        key2 = self.key_entry2.get()
        userKey[0] = getKey.keytoBin(key0)
        userKey[1] = getKey.keytoBin(key1)
        userKey[2] = getKey.keytoBin(key2)
        newKey = [getKey.keytoBin(userKey[i]) for i in range(3)]
        C0, D0 = getKey.keySeed(newKey[0])
        C1, D1 = getKey.keySeed(newKey[1])
        C2, D2 = getKey.keySeed(newKey[2])
        K=['','','']
        K[0] = getKey.keyGen(C0, D0)
        K[1] = getKey.keyGen(C1, D1)
        K[2] = getKey.keyGen(C2, D2)
        data = self.text_entry.get()
        newBin = getInput.strToBin(data)
        blockArr = getInput.binToArr(newBin)

        if not K or not data:
            messagebox.showwarning("Error", "Please enter both key and data.")
            return

        cipherText = encryptDES(K[2],getInput.binToArr(decryptDES(K[1],getInput.binToArr(encryptDES(K[0],blockArr)))))
        newCipherText = getInput.binToStr(cipherText).replace("\n", "")
        messagebox.showinfo("Encrypted Data", f"Binary:\n{cipherText}\nText:\n{newCipherText}\n\n(P.S.: The string output of ciphertext would not be perfect always. Neglect it since the important part is the binary output above it!)")

    def decrypt(self):
        userKey = ['','','']
        key0 = self.key_entry0.get()
        key1 = self.key_entry1.get()
        key2 = self.key_entry2.get()
        userKey[0] = getKey.keytoBin(key0)
        userKey[1] = getKey.keytoBin(key1)
        userKey[2] = getKey.keytoBin(key2)
        newKey = [getKey.keytoBin(userKey[i]) for i in range(3)]
        C0, D0 = getKey.keySeed(newKey[0])
        C1, D1 = getKey.keySeed(newKey[1])
        C2, D2 = getKey.keySeed(newKey[2])
        K=['','','']
        K[0] = getKey.keyGen(C0, D0)
        K[1] = getKey.keyGen(C1, D1)
        K[2] = getKey.keyGen(C2, D2)
        data = self.text_entry.get()
        newBin = data
        blockArr = getInput.binToArr(newBin)

        if not K or not data:
            messagebox.showwarning("Error", "Please enter both key and data.")
            return

        plainText = decryptDES(K[0],getInput.binToArr(encryptDES(K[1],getInput.binToArr(decryptDES(K[2],blockArr)))))
        plainText = getInput.binToStr(plainText).replace("\\n", "\n")
        messagebox.showinfo("Decryption Result", f"Decrypted Data:\n{plainText}\n\n(P.S.: There can be some extra characters added to the end of the original message! Ignore them.)")


if __name__ == "__main__":
    root = tk.Tk()
    des_gui = DESGUI(root)
    root.mainloop()