import encoder as en

if __name__ == '__main__':
    #msg1. c28a r1 c28b r1 R1 g15 n3 i3 crc14
    call1 = input ("Call 1 as c28")
    call2 = input ("Call 2 as c28")
    msg4 = input ("Report msg")
    
    c28a = en.std_call_to_c28(call1)
    c28b = en.std_call_to_c28(call2)
    g15 = en.char4_to_g15(msg4)
    r1 = 0
    R1 = 0
    i3 = 1
    
    
    msg77 = "{:028}{:01b}{:028}{:01b}{:01}{:015}{:03b}".format(c28a,r1,c28b,r1,R1,g15,i3)
    msg91 = "{:077}{:014}".format(msg77,en.gen_crc14(msg77))
    