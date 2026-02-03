#!/usr/bin/env python3
"""
Simple VCF Allele Extractor - Multiple Samples with Encoding Options
"""

import sys
import pysam

def get_vcf_genotype(genotype):
    """Get VCF-style genotype string (e.g., '0/1', '1/1')."""
    if genotype and None not in genotype:
        return "/".join(str(g) for g in genotype)
    else:
        return "./."

def get_hapmap_alleles(ref, alts, genotype):
    """Get HapMap-style allele string (e.g., 'AA', 'AT')."""
    if genotype and None not in genotype:
        all_alleles = [ref] + alts
        try:
            allele_seqs = [all_alleles[g] for g in genotype if g < len(all_alleles)]
            return "".join(allele_seqs)
        except IndexError:
            return "NN"
    else:
        return "NN"

def extract_alleles_multi_simple(vcf_file, sample_names, chromosome, start, end, encoding="hap"):
    """Simple version of the allele extractor for multiple samples with encoding options."""
    
    print(f"Extracting alleles for samples: {', '.join(sample_names)}")
    print(f"Region: {chromosome}:{start}-{end}")
    print(f"Encoding: {encoding}")
    print("-" * 80)
    
    with pysam.VariantFile(vcf_file) as vcf:
        # Check which samples exist
        available_samples = set(vcf.header.samples)
        valid_samples = [s for s in sample_names if s in available_samples]
        invalid_samples = [s for s in sample_names if s not in available_samples]
        
        if invalid_samples:
            print(f"Warning: Samples not found: {', '.join(invalid_samples)}")
            print(f"Available samples: {', '.join(sorted(available_samples))}")
            print()
        
        if not valid_samples:
            print("Error: No valid samples found!")
            return
        
        # Create header based on encoding - simplified without suffixes
        header = ["Position", "Ref", "Alt"]
        
        if encoding == "vcf":
            header.extend(valid_samples)
        elif encoding == "hap":
            header.extend(valid_samples)
        elif encoding == "both":
            # For "both", we need two columns per sample
            for sample in valid_samples:
                header.extend([sample, sample])
        
        print("\t".join(header))
        
        # Process variants in region
        for record in vcf.fetch(chromosome, start - 1, end):
            # Get alleles
            ref = record.ref
            alts = list(record.alts) if record.alts else []
            alt_str = ",".join(alts) if alts else "."
            
            # Start building the row
            row = [str(record.pos), ref, alt_str]
            
            # Add data for each valid sample based on encoding
            for sample_name in valid_samples:
                sample = record.samples[sample_name]
                genotype = sample['GT']
                
                # Get different formats
                vcf_gt = get_vcf_genotype(genotype)
                hapmap_alleles = get_hapmap_alleles(ref, alts, genotype)
                
                # Add columns based on encoding
                if encoding == "vcf":
                    row.append(vcf_gt)
                elif encoding == "hap":
                    row.append(hapmap_alleles)
                elif encoding == "both":
                    row.extend([vcf_gt, hapmap_alleles])
            
            print("\t".join(row))

def parse_encoding_flag(args):
    """Parse the --encoding flag from command line arguments."""
    encoding = "hap"  # default
    
    # Look for --encoding flag
    if "--encoding" in args:
        encoding_idx = args.index("--encoding")
        if encoding_idx + 1 < len(args):
            encoding_value = args[encoding_idx + 1]
            if encoding_value in ["vcf", "hap", "both"]:
                encoding = encoding_value
            # Remove the flag and its value from args
            args.pop(encoding_idx + 1)  # Remove value
            args.pop(encoding_idx)      # Remove flag
    
    return encoding, args

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python script.py <vcf_file> <sample1> [sample2 ...] <chromosome> <start> <end> [--encoding vcf|hap|both]")
        print("Note: Provide chromosome, start, and end as the last 3 arguments")
        print("      --encoding flag can be placed anywhere (default: hap)")
        sys.exit(1)
    
    # Parse encoding flag first
    encoding, remaining_args = parse_encoding_flag(sys.argv[1:])
    
    # Parse remaining arguments - last 3 are chromosome, start, end
    if len(remaining_args) < 5:
        print("Error: Not enough arguments after parsing --encoding flag")
        sys.exit(1)
    
    vcf_file = remaining_args[0]
    chromosome = remaining_args[-3]
    start = int(remaining_args[-2])
    end = int(remaining_args[-1])
    sample_names = remaining_args[1:-3]  # All arguments between vcf_file and chromosome
    
    if not sample_names:
        print("Error: At least one sample name must be provided")
        sys.exit(1)
    
    extract_alleles_multi_simple(vcf_file, sample_names, chromosome, start, end, encoding)
