"""
Numeral systems converter. Converts between systems with bases 2, 8, 10, 16.
"""
from os import sys

HEX_DIGITS = [str(j) for j in range(10)] +\
             [chr(k) for k in range(ord('A'), ord('F') + 1)]
NUM_SYS = {
    '2': ['0', '1'],
    '8': [str(i) for i in range(8)],
    '10': [str(j) for j in range(10)],
    '16': HEX_DIGITS
}
TRIADS = ['000', '001', '010', '011', '100', '101', '110', '111']
TETRADS = ['0' + key for key in TRIADS] +\
          ['1' + key for key in TRIADS]


def main():
    """
    The converter itself. It prints the converted number.

    :return: None
    :rtype: None
    """
    while True:
        while True:
            try:
                orig_sys, final_sys, num = user_input()
                valid(num, orig_sys, final_sys)
                break
            except ValueError as e:
                print(e)
                continue

        if orig_sys == '10':
            print('The converted number is', from_dec(num, final_sys))
        elif final_sys == '10':
            print('The converted number is', to_dec(num, orig_sys))
        elif orig_sys == '2':
            print('The converted number is', from_bin(num, final_sys))
        elif final_sys == '2':
            print('The converted number is', to_bin(num, orig_sys))
        elif orig_sys == '8':
            print('The converted number is', oct_to_hex(num))
        else:
            print('The converted number is', hex_to_oct(num))


def user_input():
    """
    The function handles user's input.

    :return: A convertible number;
             a base of the original numeral system;
             a base of the final numeral system.
    :rtype: tuple
    """
    print('Enter "exit" at any step to quit.')

    orig_sys = input(f'Enter a base of the original numeral system '
                     f'{list(NUM_SYS.keys())}: ')
    if orig_sys.upper() == 'EXIT':
        sys.exit()

    final_sys = input(f'Enter a base of the final numeral system '
                      f'{list(NUM_SYS.keys())}: ')
    if final_sys.upper() == 'EXIT':
        sys.exit()

    num = input('Enter a convertible number: ').upper()
    if num == 'EXIT':
        sys.exit()

    else:
        return orig_sys, final_sys, num


def to_dec(num, base):
    """
    Converts a number from binary, octal or hexadecimal systems to the decimal
    system.

    :param num: A number you wish to convert.
    :type num: str

    :param base: A base of the original numeral system.
    :type base: str

    :return: The converted number.
    :rtype: str
    """
    HEX_DEC = dict(zip(HEX_DIGITS, [i for i in range(16)]))
    power = len(num) - 1
    result = 0

    for digit in num:
        if base == '16':
            result += HEX_DEC[digit] * 16 ** power
        else:
            result += int(digit) * int(base) ** power
        power -= 1

    return result


def from_dec(num, base):
    """
    Converts a number from the decimal system to binary, octal or hexadecimal
    systems.

    :param num: A convertible number.
    :type num: str

    :param base: A base of the final numeral system.
    :type base: str

    :return: The converted number.
    :rtype: str
    """
    DEC_HEX = dict(zip([i for i in range(16)], HEX_DIGITS))
    result = ''
    num, base = int(num), int(base)

    while num != 0:
        if base == 16:
            result = DEC_HEX[num - num // base * base] + result
        else:
            result = str(num - num // base * base) + result
        num //= base

    return result


def from_bin(num, base):
    """
    Converts a number from the binary system to octal or hexadecimal systems.

    :param num: A convertible number.
    :type num: str

    :param base: A base of the final numeral system.
    :type base: str

    :return: The converted number.
    :rtype: str
    """
    BIN_OCT = dict(zip(TRIADS, [str(i) for i in range(8)]))
    BIN_HEX = dict(zip(TETRADS, [j for j in HEX_DIGITS]))
    result = ''

    if base == '8':
        while len(num) % 3 != 0:
            num = '0' + num
        for i in range(len(num) // 3):
            result += BIN_OCT[num[i * 3: i * 3 + 3]]
    else:
        while len(num) % 4 != 0:
            num = '0' + num
        for j in range(len(num) // 4):
            result += BIN_HEX[num[j * 4: j * 4 + 4]]

    return result


def to_bin(num, base):
    """
    Converts a number from octal or hexadecimal systems to the binary system.

    :param num: A convertible number.
    :type num: str

    :param base: A base of the original numeral system.
    :type base: str

    :return: The converted number.
    :rtype: str
    """
    OCT_BIN = dict(zip([str(i) for i in range(8)], TRIADS))
    HEX_BIN = dict(zip([j for j in HEX_DIGITS], TETRADS))
    BASES = {'8': OCT_BIN, '16': HEX_BIN}
    result = ''

    for digit in num:
        result += BASES[base][digit]

    return result


def hex_to_oct(num):
    """
    Converts a number from the hexadecimal system to the octal system.

    :param num: A convertible number.
    :type num: str

    :return: The converted number.
    :rtype: str
    """
    return from_bin(to_bin(num, '16'), '8')


def oct_to_hex(num):
    """
    Converts a number from the octal system to the hexadecimal system.

    :param num: A convertible number.
    :type num: str

    :return: The converted number.
    :rtype: str
    """

    return from_bin(to_bin(num, '8'), '16')


def valid(num, orig_base, final_base):
    """
    Checks a validity of the number and original and final systems.

    :param num: A convertible number.
    :type num: str

    :param orig_base: A base of the original numeral system.
    :type orig_base: str

    :param final_base: A base of the final numeral system.
    :type final_base: str

    :raise ValueError: If orig_base is invalid.
    :raise ValueError: If final_base is invalid.
    :raise ValueError: If orig_base == final_base.
    :raise ValueError: If num is invalid.

    :return: None
    :rtype: None
    """
    if orig_base not in NUM_SYS.keys():
        raise ValueError('Invalid original numeral system.')

    if final_base not in NUM_SYS.keys():
        raise ValueError('Invalid final numeral system.')

    if orig_base == final_base:
        raise ValueError('Numeral systems are equal.')

    for digit in num:
        if digit not in NUM_SYS[orig_base]:
            raise ValueError(f'The number must consists of '
                             f'{NUM_SYS[orig_base]}.')


if __name__ == '__main__':
    main()
