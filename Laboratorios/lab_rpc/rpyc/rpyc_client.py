import rpyc

def noisy(string):
    print('Noisy:', repr(string))

def client():
    config = {'allow_public_attrs': True}
    proxy = rpyc.connect('localhost', 18861, config=config)
    fileobj = open('testfile.txt')
    linecount = proxy.root.line_counter(fileobj, noisy)
    print('The number of lines in the file was', linecount)
    nome = linecount = proxy.root.print_name("André", "Bessa")
    print(nome)
