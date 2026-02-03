#!/usr/bin/env python3
"""
VCF Allele Extractor - Multiple Samples with Encoding Options

This script extracts alleles for multiple samples within a chromosomal region
from a VCF file using the pysam library with different encoding formats.
"""

import argparse
import sys
import pysam
from typing import List, Tuple, Optional, Dict

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Extract alleles from VCF file for specified samples and region"
    )
    parser.add_argument(
        "vcf_file",
        help="Path to the VCF file"
    )
    parser.add_argument(
        "sample_names",
        nargs='+',
        help="One or more sample/strain names from the VCF file"
    )
    parser.add_argument(
        "chromosome",
        help="Chromosome ID (e.g., 'chr1', '1', 'X')"
    )
    parser.add_argument(
        "start",
        type=int,
        help="Start position (1-based coordinates)"
    )
    parser.add_argument(
        "end",
        type=int,
        help="End position (1-based coordinates, inclusive)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file (default: stdout)"
    )
    parser.add_argument(
        "--format",
        choices=["table", "fasta"],
        default="table",
        help="Output format (default: table)"
    )
    parser.add_argument(
        "--encoding",
        choices=["vcf", "hap", "both"],
        default="hap",
        help="Allele encoding format: vcf (0/1), hap (AA/AT), or both (default: hap)"
    )
    
    return parser.parse_args()

def validate_samples(vcf_file: pysam.VariantFile, sample_names: List[str]) -> Tuple[List[str], List[str]]:
    """
    Validate that samples exist in the VCF file.
    
    Returns:
        Tuple of (valid_samples, invalid_samples)
    """
    available_samples = set(vcf_file.header.samples)
    valid_samples = []
    invalid_samples = []
    
    for sample in sample_names:
        if sample in available_samples:
            valid_samples.append(sample)
        else:
            invalid_samples.append(sample)
    
    if invalid_samples:
        print(f"Warning: Samples not found in VCF: {', '.join(invalid_samples)}", file=sys.stderr)
        print(f"Available samples: {', '.join(sorted(available_samples))}", file=sys.stderr)
    
    return valid_samples, invalid_samples

def get_vcf_genotype(genotype: Tuple[int, ...]) -> str:
    """Get VCF-style genotype string (e.g., '0/1', '1/1')."""
    if genotype is None or None in genotype:
        return "./."
    return "/".join(str(g) for g in genotype)

def get_hapmap_alleles(ref: str, alt_list: List[str], genotype: Tuple[int, ...]) -> str:
    """Get HapMap-style allele string (e.g., 'AA', 'AT')."""
    if genotype is None or None in genotype:
        return "NN"
    
    alleles = [ref] + alt_list
    
    try:
        # Get the actual alleles for this genotype
        sample_alleles = [alleles[gt] for gt in genotype if gt < len(alleles)]
        return "".join(sample_alleles)
    except (IndexError, TypeError):
        return "NN"

def get_allele_sequence(ref: str, alt_list: List[str], genotype: Tuple[int, ...]) -> str:
    """
    Get the actual DNA sequence for the alleles based on genotype (for FASTA output).
    
    Args:
        ref: Reference allele
        alt_list: List of alternative alleles
        genotype: Tuple of allele indices (0=ref, 1=first alt, etc.)
    
    Returns:
        String representation of the alleles
    """
    alleles = [ref] + alt_list
    
    # Handle missing genotypes
    if any(gt is None for gt in genotype):
        return "N/N"
    
    try:
        # Get the actual alleles for this genotype
        sample_alleles = [alleles[gt] for gt in genotype if gt < len(alleles)]
        return "/".join(sample_alleles)
    except (IndexError, TypeError):
        return "N/N"

def extract_alleles_multi(vcf_file: str, sample_names: List[str], chromosome: str, 
                         start: int, end: int) -> Tuple[List[str], List[Tuple]]:
    """
    Extract alleles from VCF file for the specified region and multiple samples.
    
    Returns:
        Tuple of (valid_samples, results)
        Results: List of tuples: (position, ref, alt, {sample: (vcf_gt, hapmap_alleles, fasta_alleles)})
    """
    results = []
    valid_samples = []
    
    try:
        with pysam.VariantFile(vcf_file) as vcf:
            # Validate samples exist
            valid_samples, invalid_samples = validate_samples(vcf, sample_names)
            
            if not valid_samples:
                print("Error: No valid samples found in VCF file.", file=sys.stderr)
                return valid_samples, results
            
            # Fetch variants in the specified region
            try:
                for record in vcf.fetch(chromosome, start - 1, end):
                    # Get reference and alternative alleles
                    ref = record.ref
                    alts = list(record.alts) if record.alts else []
                    
                    # Collect data for all valid samples
                    sample_data = {}
                    for sample_name in valid_samples:
                        sample = record.samples[sample_name]
                        genotype = sample['GT']
                        
                        # Get different encodings
                        vcf_gt = get_vcf_genotype(genotype)
                        hapmap_alleles = get_hapmap_alleles(ref, alts, genotype)
                        fasta_alleles = get_allele_sequence(ref, alts, genotype)
                        
                        sample_data[sample_name] = (vcf_gt, hapmap_alleles, fasta_alleles)
                    
                    results.append((
                        record.pos,  # 1-based position
                        ref,
                        ",".join(alts) if alts else ".",
                        sample_data
                    ))
                    
            except Exception as e:
                print(f"Error fetching region {chromosome}:{start}-{end}: {e}", file=sys.stderr)
                
    except Exception as e:
        print(f"Error opening VCF file: {e}", file=sys.stderr)
    
    return valid_samples, results

def format_output_table(results: List[Tuple], sample_names: List[str], 
                       chromosome: str, start: int, end: int, encoding: str) -> str:
    """Format results as a table with columns for each sample based on encoding."""
    output = []
    output.append(f"# VCF Allele Extraction Results")
    output.append(f"# Samples: {', '.join(sample_names)}")
    output.append(f"# Region: {chromosome}:{start}-{end}")
    output.append(f"# Encoding: {encoding}")
    output.append(f"# Found {len(results)} variants")
    output.append("")
    
    # Create header based on encoding - simplified without suffixes
    header = ["Position", "Ref", "Alt"]
    
    if encoding == "vcf":
        header.extend(sample_names)
    elif encoding == "hap":
        header.extend(sample_names)
    elif encoding == "both":
        # For "both", we need two columns per sample, so we'll repeat each name twice
        for sample in sample_names:
            header.extend([sample, sample])
    
    output.append("\t".join(header))
    
    # Add data rows
    for pos, ref, alt, sample_data in results:
        row = [str(pos), ref, alt]
        
        for sample in sample_names:
            if sample in sample_data:
                vcf_gt, hapmap_alleles, fasta_alleles = sample_data[sample]
                
                if encoding == "vcf":
                    row.append(vcf_gt)
                elif encoding == "hap":
                    row.append(hapmap_alleles)
                elif encoding == "both":
                    row.extend([vcf_gt, hapmap_alleles])
            else:
                if encoding == "vcf":
                    row.append("./.")
                elif encoding == "hap":
                    row.append("NN")
                elif encoding == "both":
                    row.extend(["./.", "NN"])
        
        output.append("\t".join(row))
    
    return "\n".join(output)

def format_output_fasta(results: List[Tuple], sample_names: List[str], 
                       chromosome: str, start: int, end: int) -> str:
    """Format results as FASTA-like output with one sequence per sample."""
    output = []
    
    for sample in sample_names:
        output.append(f">{sample}_{chromosome}:{start}-{end}")
        
        # Create allele representation for this sample
        allele_strings = []
        for pos, ref, alt, sample_data in results:
            if sample in sample_data:
                vcf_gt, hapmap_alleles, fasta_alleles = sample_data[sample]
                # For FASTA output, show the first allele if heterozygous
                if "/" in fasta_alleles and fasta_alleles != "N/N":
                    first_allele = fasta_alleles.split("/")[0]
                    allele_strings.append(f"{pos}:{first_allele}")
                else:
                    allele_strings.append(f"{pos}:{fasta_alleles}")
            else:
                allele_strings.append(f"{pos}:N")
        
        # Group into lines of reasonable length
        line_length = 60
        current_line = ""
        for allele_str in allele_strings:
            if len(current_line) + len(allele_str) + 1 > line_length:
                if current_line:
                    output.append(current_line)
                current_line = allele_str
            else:
                if current_line:
                    current_line += " " + allele_str
                else:
                    current_line = allele_str
        
        if current_line:
            output.append(current_line)
        output.append("")  # Empty line between samples
    
    return "\n".join(output)

def main():
    """Main function."""
    args = parse_arguments()
    
    # Validate arguments
    if args.start > args.end:
        print("Error: Start position must be less than or equal to end position", file=sys.stderr)
        sys.exit(1)
    
    # Extract alleles
    valid_samples, results = extract_alleles_multi(
        args.vcf_file, 
        args.sample_names, 
        args.chromosome, 
        args.start, 
        args.end
    )
    
    if not valid_samples:
        print("No valid samples found.", file=sys.stderr)
        sys.exit(1)
    
    if not results:
        print("No variants found in the specified region.", file=sys.stderr)
        sys.exit(1)
    
    # Format output
    if args.format == "fasta":
        output_text = format_output_fasta(results, valid_samples, 
                                        args.chromosome, args.start, args.end)
    else:
        output_text = format_output_table(results, valid_samples, 
                                        args.chromosome, args.start, args.end, args.encoding)
    
    # Write output
    if args.output:
        try:
            with open(args.output, 'w') as f:
                f.write(output_text)
            print(f"Results written to {args.output}")
        except Exception as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(output_text)

if __name__ == "__main__":
    main()
