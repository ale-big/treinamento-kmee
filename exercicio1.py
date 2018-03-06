#!/usr/bin/env python
# -*- coding: utf-8 -*-


# import dos modulos
import sys


def main():
    nome = 'Alexandre The Big' if len(sys.argv)<2 else sys.argv[1]
    print("Hello there {}".format(nome))

print("Fora do Main")

if __name__ == '__main__':
    main()
    #pass

