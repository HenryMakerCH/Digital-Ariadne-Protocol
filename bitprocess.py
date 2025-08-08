
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

mapping_rev = {
        '000': '0',
        '001': '1',
        '011': '2',
        '010': '3',
        '110': '4',
        '100': '5',
        '101': '6',
        '111': '7'
    }
    
def channel_to_bit(channel):
    result = ''.join(
            mapping.get(char, '') 
            for char in "{:058}".format(channel)
        )
    return result


def bit_to_channel(bit):
    result = ''.join(
            mapping_rev.get(bit[i:i+3],'')
            for i in range(0, len(bit), 3)
        )
    return result

if __name__ == "__main__":
    channel = input()
    print (bit_to_channel(channel_to_bit(channel)) == channel)