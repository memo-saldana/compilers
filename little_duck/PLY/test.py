from ld_parser import parser

def test():
    print("Testing...")
    f = open('test.ld')
    s = f.read()
    f.close()

    parser.parse(s)

    print('Code is okay.')

if __name__ == "__main__":
    test()
