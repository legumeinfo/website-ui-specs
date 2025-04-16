# Gene Symbols page

This is the initial/draft requirements doc for the SoyBase parentage and pedigree report page. Implementation will probably be as a Jekyll page, calling a back-end service similar to
https://www.soybase.org/tools/analysis/go.html

Page address (to replace current content at that location): tools/parentage/index.html


## Specification version
Version: 0.6.0

<details>

v0.5.0 First draft, 2024-11-07. Initial UI spec and back-end service implementation. The API has two endpoints: one generating a zip file to be passed to the Helium web application, and the other being plain-text to be used for the report on the website.

v0.6.0 Second draft, 2024-11-25. Update back-end code and API. In this version, the text report is in JSON format. 

</details>

## Input

**Page text:**

Gene Symbols

The table below shows gene symbols that have been published or have been submitted to SoyBase. The associated gene IDs are as reported in the scientific literature. Click a gene ID to access tools and resources, including corresponding genes from other accessions.

All 0-9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 

Search: [   ]

| Symbol  |  Symbol full name  |  Gene model |
|--|--|--|
| 2A6 |	| Glyma02g09290 |
| 4CL  |  4-coumarate--CoA ligase-like 7-like  |  Glyma.13g323000 |
| 4CL1  |  4-coumarate:coenzyme A ligase gene 1  |  Glyma.17g064600 |
| 4CL2  |  4-coumarate:coenzyme A ligase gene 2  |  Glyma.13g372000 |
| 4CL3  |  4-coumarate:coenzyme A ligase gene 3  |  Glyma.11g010500 |
| 4CL4  |  4-coumarate:coenzyme A ligase gene 4  |  Glyma.01g232400 |
| A1  |  albumin 1  |  Glyma.13g194400 |
| AAH  |  allantoate amidohydrolase  |  Glyma.15g156900 |
| AAH2  |  allantoate deiminase 2 |Glyma.09g050800 |

