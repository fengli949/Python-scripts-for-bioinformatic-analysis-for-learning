# output an integration file with upstream 21 bp and downstream 19 bp genomic flanks (Tf1-INfs
with open ('true_integration_BC5040.v12str_HL046.txt', 'r') as seq_read, open ('integration_up_down.txt','w') as seq_write:
    for line in seq_read:
        line = line.rstrip()
        Id, chrs, position, strand, dupl = line.split()
        up = int(position)-21
        down = int(position)+19
        seq_write.write(chrs+'\t'+str(up)+'\t'+str(down)+'\t'+dupl+'\t'+Id+'\t'+strand+'\n')
    print('done')