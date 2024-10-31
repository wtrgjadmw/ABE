import random
"""
#num = random.randint(1, 2 ** 512)
num = 5621717594504069707814303841887966785022584757720793663951738727161947290103878123235803959312730434734528281241578858938114030211847333616391301375268667
p = 0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab
current_num = num // 2 ** 131
shift_reg = bin(num % (2 ** 131))[2:]
counter = 0
print("num", num)
print("shift_len", len(shift_reg))
while True:
    result = current_num - p
    if result < 0:
        next_num = current_num
    else:
        next_num = result
    print("counter:", counter)
    print(current_num)
    print((num // 2 ** (130 - counter)) % p)
    if(counter == 131):
        break
    counter += 1
    current_num = next_num * 2 + int(shift_reg[counter])

print(next_num)
print("correct_result", num % p)
"""
for j in range(10):
    num = random.randint(1, 2 ** 512)
    #num = 5621717594504069707814303841887966785022584757720793663951738727161947290103878123235803959312730434734528281241578858938114030211847333616391301375268667
    p = 0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab
    current_num = num // 2 ** (512 - 381)
    counter = 0
    shift_reg = format(num % (2 ** (512 - 381)), "0131b")
    print("j: ",  j)
    for i in range(len(shift_reg) + 1):
        #print("i:", i)
        result = current_num - p
        if result < 0:
            next_num = current_num
        else:
            next_num = result
        #print(current_num)
        #print(result)
        #print(next_num)
        #print((num // 2**(131 - i)) % p)
        if i != len(shift_reg):
            current_num = next_num * 2 + int(shift_reg[i])
    print(num)
    print(num % p)

    assert next_num == num % p