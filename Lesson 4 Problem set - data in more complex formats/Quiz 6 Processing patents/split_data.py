#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.
    
    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """
    
    f = open(filename, 'r')
    # num_of_file = 0
    # for line in f.readlines():
    #     if line.startswith("<?xml"):
    #         num_of_file += 1
    # print num_of_file
    
    flag = False
    n = 0
    file_name = open("{}-{}".format(filename, n), 'w')
    for line in f.readlines():
        if line.startswith("<?xml") and flag == True:
            file_name.close()
            n += 1
            file_name = open("{}-{}".format(filename, n), 'w')
            file_name.write("%s\n" % line)

        else:
            # file.append(line)
            flag = True
            file_name.write(line)


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()