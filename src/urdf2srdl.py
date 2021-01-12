#!/usr/bin/env python
from __future__ import print_function
import argparse
import sys
from srdfdom.srdf import SRDF

if __name__ == "__main__":

    parser = argparse.ArgumentParser(usage='Load an SRDF file')
    parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=None, help='File to load')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=None, help='Dump file to XML')
    args = parser.parse_args()

    robot = SRDF.from_xml_file(args.file.read())
    if args.output is not None:
        args.output.write(robot.to_xml_string())
