genelist = {}
complement = {'A':'T','C':'G','T':'A','G':'C'}
with open('Python_06.seq.txt','r') as seq_read, open('Python6_revcom.txt','w') as seq_write:
    for line in seq_read:
        line = line.rstrip() # remove empty lines
        gene_id, seq = line.split() # split on whitespace
        genelist[gene_id] = seq # build a dictionary file
        reverse_com =''.join(complement[base] for base in seq[::-1])# reverse complement seq
        nt_count = len(genelist[gene_id])
        seq_write.write(gene_id+'\t'+ reverse_com + '\t'+str(nt_count)+'\n')
print('done')