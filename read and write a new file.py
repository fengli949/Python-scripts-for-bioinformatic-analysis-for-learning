#!/usr/bin/env python3

total_nts = 0
# open two file objects, one for reading, one for writing
with open("seq.nt.txt","r") as seq_read, open("nt.counts.txt","w") as seq_write:
  for line in seq_read:
    line = line.rstrip()
    nt_count = len(line)
    total_nts += nt_count
    seq_write.write(str(nt_count) + "\n")

  seq_write.write("Total: " + str(total_nts) +"\n")

print("Wrote 'nt.counts.txt'")