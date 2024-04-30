#!/usr/bin/env python3
import subprocess
import sys
query = sys.argv[1]
out_file = query + '_bed_out.fa'
cmd = 'bedtools '+'getfasta '+'-name '+'-s '+'-fi '+ 'chr123.fas ' + '-bed ' + query + ' -fo ' + out_file
subprocess.run(cmd, shell=True)
# automate bedtools run