
all_cap = [chr(cap) for cap in range(65,91)]
all_num = [chr(num) for num in range(48,58)]

a2 = all_num.copy()
a2.extend(all_cap)
a1 = a2.copy()
a1.insert(0," ")
a3 = all_num.copy()
a4 = all_cap.copy()
a4.insert(0," ")
c = a1.copy()
c.append("/")

ntokens = 2063592
max22 = 4194304
maxchar4=32400
nprime = 47055833459
nbits = [10, 12, 22]
crc_poly=[1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1] #0x6757

def std_call_to_c28(std_call):
    ind = []
    call_len = len(std_call)
    if str.isdigit(std_call[2]):
        std_call = "{:<6}".format(std_call)
    else:
        std_call = " {:<6}".format(std_call)
    splitcall = list(std_call)
    ind.append(a1.index(splitcall[0]))
    ind.append(a2.index(splitcall[1]))
    ind.append(a3.index(splitcall[2]))
    ind.append(a4.index(splitcall[3]))
    ind.append(a4.index(splitcall[4]))
    ind.append(a4.index(splitcall[5]))
    n28 = ntokens + max22 + 36*10*27**3*ind[0] + 10*27**3*ind[1] + 27**3*ind[2] + 27**2*ind[3] + 27*ind[4] + ind[5]
    n28 = "{:028b}".format(n28)
    return n28

def char4_to_g15(char4):
    is_char4 = (char4[0] >= 'A' and char4[0] <= 'R' and
            char4[1] >= 'A' and char4[1] <= 'R' and
            char4[2] >= '0' and char4[2] <= '9' and
            char4[3] >= '0' and char4[3] <= '9')
    if is_char4 and char4 != 'RR73':
        j1 = (ord(char4[0]) - ord('A')) * 18 * 10 * 10
        j2 = (ord(char4[1]) - ord('A')) * 10 * 10
        j3 = (ord(char4[2]) - ord('0')) * 10
        j4 = (ord(char4[3]) - ord('0'))
        g15 = j1 + j2 + j3 + j4
    else:
        if not char4:  # Empty string
            rpt = 1
        elif char4 == 'RRR':
            rpt = 2
        elif char4 == 'RR73':
            rpt = 3
        elif char4 == '73':
            rpt = 4
        elif char4[0] in ('+', '-'):
            rpt = int(char4) + 35
        g15 = maxchar4 + rpt
    g15 = "{:015b}".format(g15)
    return g15

def hashcodes(call,htype='h22b'):
    call = call.ljust(11)
    n8 = 0
    for char in call:
        pos = c.index(char)
        n8 = n8 * 38 + pos
    hashes = []
    for k in range(3):
        product = nprime * n8
        shift_amount = 64 - nbits[k]
        if shift_amount > 0:
            low_64 = product & 0xFFFFFFFFFFFFFFFF
            if low_64 & 0x8000000000000000:
                shifted = ~((~low_64) >> shift_amount)
            else:
                shifted = low_64 >> shift_amount
        else:
            shifted = product
        hashes.append(shifted)
    h22_bias = hashes[2] + ntokens
    h10 = "{:010b}".format(hashes[0])
    h12 = "{:012b}".format(hashes[1])
    h22 = "{:022b}".format(hashes[2])
    h22b = "{:028b}".format(h22_bias)
    if htype == 'h10':
        result = h10
    elif htype == 'h12':
        result = h12
    elif htype == 'h22':
        result = h22
    else:
        result = h22b
    return result
    
def gen_crc14(msg77):
    msg96 = [int(bit) for bit in msg77] + [0] * 19
    r = msg96[:15]
    for i in range(82):
        r[14] = msg96[14 + i]
        if r[0] == 1:
            for j in range(15):
                r[j] ^= crc_poly[j]
        r.append(0)
        del r[0]
    crc_bits = r[:14]
    crc_str = ''.join(str(bit) for bit in crc_bits)
    crc_int = int(crc_str, 2)
    crc_bits = "{:014b}".format(crc_int)
    return crc_bits

#def nonstd_to_c58():


#def free_text_to_f71():


#def grid6_to_g25():


#print (gen_crc14(input()))