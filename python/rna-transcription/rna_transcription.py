def to_rna(dna_strand):
    rna_strand = ""
    for nucleotide in dna_strand:
        match nucleotide:
            case "G":
                rna_strand += "C"
            case "C":
                rna_strand += "G"            
            case "T":
                rna_strand += "A"            
            case "A":
                rna_strand += "U"
            #case _:
                #return raise ValueError("Unknown nucleotide in DNA sequence") 
    
    return rna_strand
            
