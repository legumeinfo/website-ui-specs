# Allele search query - to find variants (generally SNPs) around a gene or in a region, within a specified variant collection

This is the initial/draft requirements doc for the SoyBase allele search, to be implemented on the respective Jekyll web sites. This search component should enable search of specified variant collections (VCF files) in the vicinity of a specified gene or within a specified region. 
Note that the specification is for SoyBase first, partly because many VCF files are available for soybean. The specification and implementation may be generalized later for use with other species at LIS and PeanutBase.

## Specification version
Version: 0.7.0

<details>

The initial draft of this document (0.5.0), 2024-07-18, is essentially for a prototype implementation, probably using a combination of the GCV microservices to return gene coordinates and the fasta-api services to return alleles from a range in a VCF. The first implementation will probably be done in in-page javascript rather than in a web component, since the GraphQL schema is not yet described for fasta-api.

Some tweaks on 2024-07-25 (0.6.0), removing "Genes in this region" from the results.

A new version 2026-02-03 (0.7.0), with additional specification for a back-end service (to be written) that returns alleles for provided samples of interest, from a specified region.

</details>

## Input
A variant collection, as a VCF file
```
# Variant collections for assembly Wm82.a2 / Wm82.gnm2.ann1.RVB6
  Filename                                    ;                    Variant Collection                       ; Annotation Collection
  glyma.Wm82.gnm2.div.Song_Hyten_2015.vcf.gz ;                     Wm82.gnm2.div.Song_Hyten_2015            ; Wm82.gnm2.ann1.RVB6
  glyma.Wm82.gnm2.div.Torkamaneh_Laroche_2017.SNPdata.vcf.gz ;     Wm82.gnm2.div.Torkamaneh_Laroche_2017    ; Wm82.gnm2.ann1.RVB6
  glyma.Wm82.gnm2.div.Torkamaneh_Laroche_2019.NonSynSNPs.vcf.gz ;  Wm82.gnm2.div.Torkamaneh_Laroche_2019    ; Wm82.gnm2.ann1.RVB6
  glyma.Wm82.gnm2.div.Torkamaneh_Laroche_2019.SNPdata.vcf.gz ;     Wm82.gnm2.div.Torkamaneh_Laroche_2019    ; Wm82.gnm2.ann1.RVB6
  glyma.Wm82.gnm2.div.Valliyodan_Brown_2021.USB481.vcf.gz ;        Wm82.gnm2.div.Valliyodan_Brown_2021      ; Wm82.gnm2.ann1.RVB6
  glyma.Wm82.gnm2.div.Wickland_Battu_2017.SNPdata1.vcf.gz ;        Wm82.gnm2.div.Wickland_Battu_2017        ; Wm82.gnm2.ann1.RVB6
  glyma.Wm82.gnm2.div.Wickland_Battu_2017.SNPdata2.vcf.gz ;        Wm82.gnm2.div.Wickland_Battu_2017        ; Wm82.gnm2.ann1.RVB6
  glyma.Wm82.gnm2.div.Wickland_Battu_2017.SNPdata3.vcf.gz ;        Wm82.gnm2.div.Wickland_Battu_2017        ; Wm82.gnm2.ann1.RVB6
  glyma.Wm82.gnm2.div.Zhang_Jiang_2020.SNPdata_full.vcf.gz ;       Wm82.gnm2.div.Zhang_Jiang_2020           ; Wm82.gnm2.ann1.RVB6
  glyma.Wm82.gnm2.div.Zhang_Jiang_2020.SNPdata_maf01.vcf.gz ;      Wm82.gnm2.div.Zhang_Jiang_2020           ; Wm82.gnm2.ann1.RVB6

# Variant collections for assembly Wm82.a4 / Wm82.gnm4.ann1.T8TQ
  glyma.Wm82.gnm4.div.Song_Hyten_2015.vcf.gz ;                     Wm82.gnm4.div.Song_Hyten_2015            ; Wm82.gnm4.ann1.T8TQ
```

... and either 
- Gene ID, with prefix, e.g. "glyma.Wm82.gnm4.ann1.Glyma.16G044100" and size of left and right flanking regions (e.g. 50000)
or
- Genomic region, as chromosome:start-end, e.g. "Gm01:100000-200000"

... and optionally, one or more strain or sample IDs, populated by a dropdown list derived from the selected variant collection.

- SEARCH button

Examples are shown below each text input element. (Selectors are self-explanatory.)

### Mockup

![image](Allele_search.png)

<hr><br>

![image](Allele_search_results.png)


<hr><br>

When one or more strains are selected, the output should be a table in one of two encoding format (depending whether format "VCF" or "HapMap" is toggled; default HapMap):

HapMap encoding:
```
--------------------------------------------------------------------------------
Position	Ref	Alt	HN001	HN002	USB-002
324571	T	C	TT	CC	CC
377917	A	G	GG	GG	GG
437287	T	G	GG	GG	GG
474188	C	T	CC	TT	TT
```

VCF encoding
```
--------------------------------------------------------------------------------
Position	Ref	Alt	HN001	HN002	USB-002
324571	T	C	0/0	1/1	1/1
377917	A	G	1/1	1/1	1/1
437287	T	G	1/1	1/1	1/1
474188	C	T	0/0	1/1	1/1
```

## Implementation notes

The variant data sets are identified from the datastore-metadata, in the subrepository of jekyll-soybase.

This microservice can be called thus:
```
curl 'https://gcv.soybase.org/microservices/soybase/genes' --data-raw '{"genes":["glyma.Wm82.gnm4.ann1.Glyma.01G000322","glyma.Wm82.gnm4.ann1.Glyma.01G001000"]}'
```

### Notes from Alan:

> [https://github.com/legumeinfo/microservices/tree/main/genes](https://github.com/legumeinfo/microservices/tree/main/genes)

> You send it a list of gene names that you want info for (full yuck) and it returns a list of gene objects in the same order as the given list of names.

> The microservice supports both Protocal Buffers and HTTP requests. I recommend HTTP but the Protocol Buffers (i.e. .proto files) are useful for deciphering what the inputs/outputs of the service are. These files are located in the service's proto/ directory.

> [https://github.com/legumeinfo/microservices/tree/main/genes/proto](https://github.com/legumeinfo/microservices/tree/main/genes/proto)

Here is fasta-api:
[https://github.com/soybase/fasta-api](https://app.soybase.org/api/fasta-api/docs)

### Note from Steven ...
... with commandline prototype implementations that illustrate input data and options and output.

These scripts require the pysam library, which can be installed with e.g.
`pip install pysam`
or in a conda environment.

There are two versions of the script -- the [first one](prototypes/get_alleles_simple_S4_v03.py) being simpler and the [second one](prototypes/get_alleles_S4_v03.py) being more full-featured.

They are called thus (assuming, in these examples, a bgzipped and tabix-indexed VCF at the indicated location):
```
  ./get_alleles_simple_S4_v03.py -h
  #Usage: python script.py <vcf_file> <sample1> [sample2 ...] <chromosome> <start> <end>
  #Note: Provide chromosome, start, and end as the last 3 arguments

  ./get_alleles_simple_S4_v03.py data/USB481-25Kshared50Kpos.vcf.gz HN001 HN002 USB-002 Chr13 100000 500000
  ./get_alleles_simple_S4_v03.py --encoding hap data/USB481-25Kshared50Kpos.vcf.gz HN001 HN002 USB-002 Chr13 100000 500000
  ./get_alleles_simple_S4_v03.py --encoding vcf data/USB481-25Kshared50Kpos.vcf.gz HN001 HN002 USB-002 Chr13 100000 500000
```

```
  ./get_alleles_S4_v03.py -h
  #usage: get_alleles_S4_v03.py [-h] [-o OUTPUT] [--format {table,fasta}]
  #                             vcf_file sample_names [sample_names ...] chromosome start end

  ./get_alleles_S4_v03.py data/USB481-25Kshared50Kpos.vcf.gz HN001 HN002 USB-002 Chr13 100000 500000
  ./get_alleles_S4_v03.py --encoding hap data/USB481-25Kshared50Kpos.vcf.gz HN001 HN002 USB-002 Chr13 100000 500000
  ./get_alleles_S4_v03.py --encoding vcf data/USB481-25Kshared50Kpos.vcf.gz HN001 HN002 USB-002 Chr13 100000 500000
```

For both of the scripts above, the formats look like the following:
```
  Encoding: hap
  --------------------------------------------------------------------------------
  Position	Ref	Alt	HN001	HN002	USB-002
  324571	T	C	TT	CC	CC
  377917	A	G	GG	GG	GG
  437287	T	G	GG	GG	GG
  474188	C	T	CC	TT	TT
```

```
  Encoding: vcf
  --------------------------------------------------------------------------------
  Position	Ref	Alt	HN001	HN002	USB-002
  324571	T	C	0/0	1/1	1/1
  377917	A	G	1/1	1/1	1/1
  437287	T	G	1/1	1/1	1/1
  474188	C	T	0/0	1/1	1/1
```


