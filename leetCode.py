# mencari int yang hanya muncul satu kali
nums = list(map(int, input("Masukan Array: ").split()))
hasil = []
T = False
for num in nums:
    if num in hasil:
        T = True
        break
    hasil.append(num)
print(T)