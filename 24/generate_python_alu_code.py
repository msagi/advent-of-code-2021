# https://adventofcode.com/2021/day/24

def generate_code(lines):
    """
    Generate python code from ALU program lines
    :param lines: the ALU program lines
    :return: the python code equivalent
    """
    w_i = 0  # input of the input digit of the ALU program
    tab = '    '
    code = ''
    for index, line in enumerate(lines):
        command = line.strip().split(' ')
        if command[0] == 'inp':
            if code != '':
                code += f'{tab}return x, y, z\n\n\n'
            code += f'def monad_digit{w_i}(w, x, y, z):\n'
            w_i += 1
        elif command[0] == 'add':
            code += f'{tab}{command[1]} += {command[2]}\n'
        elif command[0] == 'mul':
            if command[2] == '0':
                code += f'{tab}{command[1]} = 0\n'
            else:
                code += f'{tab}{command[1]} *= {command[2]}\n'
        elif command[0] == 'div':
            code += f'{tab}{command[1]} //= {command[2]}\n'
        elif command[0] == 'mod':
            code += f'{tab}{command[1]} %= {command[2]}\n'
        elif command[0] == 'eql':
            code += f'{tab}{command[1]} = 1 if {command[1]} == {command[2]} else 0\n'
        else:
            print(f'invalid line:{index}: \'{line}\'')
            exit(-1)
    code += f'{tab}return x, y, z\n\n\n'

    # add main method
    code += 'def monad(number):\n'
    code += f'{tab}x = 0\n'
    code += f'{tab}y = 0\n'
    code += f'{tab}z = 0\n'
    for i in range(14):
        code += f'{tab}x, y, z = monad_digit{i}(int(number[{i}]), x, y, z)\n'
    code += f'{tab}print(\'MONAD: model number: {{}}, z = {{}}\'.format(number, z))\n'
    code += '\n\n'

    code += 'monad(\'29599469991739\')\n'
    code += 'monad(\'17153114691118\')'
    return code


def solve(input_file: str):
    # load file
    infile = open(input_file, 'r')
    lines = infile.readlines()
    infile.close()
    # parse input
    code = generate_code(lines)
    print(code)


solve("input.txt")
