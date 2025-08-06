
all_cap = [chr(cap) for cap in range(65,91)]
all_num = [chr(num) for num in range(48,58)]

a2 = all_num.copy()
a2.extend(all_cap)
a1 = a2.copy()
a1.insert(0," ")
a3 = all_num.copy()
a4 = all_cap.copy()
a4.insert(0," ")

ntokens = 2063592
max22 = 4194304
maxchar4=32400

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
        ichar4 = j1 + j2 + j3 + j4
    else:
        # Handle special cases
        if not char4:  # Empty string
            irpt = 1
        elif char4 == 'RRR':
            irpt = 2
        elif char4 == 'RR73':
            irpt = 3
        elif char4 == '73':
            irpt = 4
        elif char4[0] in ('+', '-'):
            irpt = int(char4) + 35
        ichar4 = maxchar4 + irpt
    g15 = "{:015b}".format(ichar4)
    return g15

#def hashcodes():


#def gen_crc14():


#def nonstd_to_c58():


#def free_text_to_f71():


#def grid6_to_g25():


print (char4_to_g15(input()))