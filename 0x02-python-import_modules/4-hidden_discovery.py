#!/usr/bin/python3

if __name__ == "__main__":

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":  #for all the names that does not start with __
            print(name)