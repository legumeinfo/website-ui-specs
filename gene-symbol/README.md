# Gene Symbols page

This is the initial/draft requirements doc for the SoyBase parentage and pedigree report page. Implementation will probably be as a Jekyll page, calling a back-end service similar to
https://www.soybase.org/tools/parentage/

Page address (to replace current content at that location): tools/parentage/index.html


## Specification version
Version: 0.5.0

<details>

v0.5.0 First draft, 2025-04-16. Initial UI spec
</details>

## Input

**Page text:**

Gene Symbols

The table below shows gene symbols that have been published or have been submitted to SoyBase. The associated gene IDs are as reported in the scientific literature. Click a gene ID to access tools and resources, including corresponding genes from other accessions.

All 0-9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 

Search: [   ]

| Symbol  |  Symbol full name  |  Gene model IDs |
|--|--|--|
| 2A6 |	| <a href="https://www.soybase.org/tools/search/gene.html?genus=Glycine&species=&strain=&identifier=glyma.Wm82.gnm1.ann1.Glyma02g09290&description=&family=&page=1">Glyma02g09290</a> |
| 4CL  |  4-coumarate--CoA ligase-like 7-like  |  <a href="https://www.soybase.org/tools/search/gene.html?genus=Glycine&species=&strain=&identifier=glyma.Wm82.gnm2.ann1.Glyma.13g323000&description=&family=&page=1">Glyma.13g323000</a> |
| 4CL1  |  4-coumarate:coenzyme A ligase gene 1  |  <a href="https://www.soybase.org/tools/search/gene.html?genus=Glycine&species=&strain=&identifier=glyma.Wm82.gnm2.ann1.Glyma.17g064600&description=&family=&page=1">Glyma.17g064600</a> |
| 4CL2  |  4-coumarate:coenzyme A ligase gene 2  |  <a href="https://www.soybase.org/tools/search/gene.html?genus=Glycine&species=&strain=&identifier=glyma.Wm82.gnm2.ann1.Glyma.13g372000&description=&family=&page=1">Glyma.13g372000</a> |
| 4CL3  |  4-coumarate:coenzyme A ligase gene 3  |  <a href="https://www.soybase.org/tools/search/gene.html?genus=Glycine&species=&strain=&identifier=glyma.Wm82.gnm2.ann1.Glyma.11g010500&description=&family=&page=1">Glyma.11g010500</a> |
| 4CL4  |  4-coumarate:coenzyme A ligase gene 4  |  <a href="https://www.soybase.org/tools/search/gene.html?genus=Glycine&species=&strain=&identifier=glyma.Wm82.gnm2.ann1.Glyma.01g232400&description=&family=&page=1">Glyma.01g232400</a> |
| A1  |  albumin 1  |  <a href="https://www.soybase.org/tools/search/gene.html?genus=Glycine&species=&strain=&identifier=glyma.Wm82.gnm2.ann1.Glyma.13g194400&description=&family=&page=1">Glyma.13g194400</a> |
| AAH  |  allantoate amidohydrolase  |  <a href="https://www.soybase.org/tools/search/gene.html?genus=Glycine&species=&strain=&identifier=glyma.Wm82.gnm2.ann1.Glyma.15g156900&description=&family=&page=1">Glyma.15g156900</a> |
| AAH2  |  allantoate deiminase 2 |<a href="https://www.soybase.org/tools/search/gene.html?genus=Glycine&species=&strain=&identifier=glyma.Wm82.gnm2.ann1.Glyma.09g050800&description=&family=&page=1">Glyma.09g050800</a> |


## Implementation

The data will be in a four-column flatfile, probably stored in Jekyll _data/gene_symbols.tsv (see file [here](gene_symbols.tsv)).
Of those columns, the first three will be displayed. The fourth should not be displayed, but is the full, prefixed form of the gene identifier that 
should be used for accessing the modal report via GraphQL.

The table will have approximately 4,000 rows; so some custom javascript would be best for 
rendering the table with pagination and allowing for searching.

The gene model IDs (e.g. Glyma.13g323000) should link to a modal linkout for that identifier, similar to the linkouts from [a gene search page](https://www.soybase.org/tools/search/gene.html?genus=Glycine&species=&strain=&identifier=glyma.Wm82.gnm2.ann1.Glyma.13g323000&description=&family=&page=1).

As a fall-back (in case there are difficulties in calling the modal), populated links to the gene page would be acceptable (though modal would be preferred).

