from field import Fp

p = 4002409555221667393417789825735904156556882819939007885332058136124031650490837864442687629129015664037894272559787
p_3_div4 = (p - 3) // 4
exp_bin = bin(p_3_div4)[2:]
R0 = Fp(1, 0)
R0.Mont_change()
R1 = Fp(0x9bb1464bc860e8c087d3351f6b0fa4e8315d707b2c1c29641b971a0395db482d33a9bca9a5582da55987ded3ab6a920, 1)
print(exp_bin)
for i in range(len(exp_bin)):
    print(378 - i)
    if(exp_bin[i] == "1"):
        print("R1", hex(R1.value))
        R0, R1 = R0 * R1, R1 * R1
        
    else:
        print("R0", hex(R0.value))
        R0, R1 = R0 * R0, R0 * R1
        