
mapping = {
    '0': '000',
    '1': '001',
    '2': '011',
    '3': '010',
    '4': '110',
    '5': '100',
    '6': '101',
    '7': '111'
    }

def channel_to_bit(channel):
    result = ''.join(mapping.get(char, '') for char in "{:058d}".format(channel))
    return result


#def bit_to_channel(bit)


if __name__ == "__main__":
    print (channel_to_bit(int(input())))