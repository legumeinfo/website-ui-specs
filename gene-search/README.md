# Gene search query

## Input

This is the requirements doc for the type of gene search that Andrew proposed for the LIS site. It differs from the main-branch version in that it is not merely a gene identifier lookup -- it searches against various attributes of genes, namely:

- genus (selector with "any" on top)
- species (selector populated if genus specified, otherwise only "any")
- strain (selector populated if species specified, otherwise only "any")
- gene identifier (text input)
- gene name (text input)
- gene description (text input)
- gene family identifiers (text input)

The heading of each attribute filter will have a tool tip that provides an example.

### Mockup

![input-mockup](https://user-images.githubusercontent.com/5657219/228373027-6d5bb124-8d5f-4cb4-9a8c-98c9852920d5.png)

## Output

The output will be a paginated list of search results in tabular form, containing:

- full LIS identifier (linked to Linkout Service) e.g. `aesev.CIAT22838.gnm1.ann1.Ae01g16390`
- gene name (typically originating from Name attribute in LIS GFF) e.g. `Ae01g16390`
- gene description (typically originating from Note attribute in LIS GFF) e.g. `oxygen-evolving enhancer protein; IPR008797 (Photosystem II PsbQ, oxygen evolving ...`
- genomic location (chromosome:start-finish, strand) e.g. `aesev.CIAT22838.gnm1.Ae01:20407086-20408460 (+)`
- gene family identifiers (each linked to Linkout Service) e.g. `legfed_v1_0.L_KK1G2X`

### Mockup

| identifier | name | description | location | gene families |
| ---------- | ---- | ----------- | -------- | ------------- |
| aesev.CIAT22838.gnm1.ann1.Ae01g16390 | Ae01g16390 | oxygen-evolving enhancer protein; IPR008797 (Photosystem II PsbQ, oxygen evolving complex), ... | aesev.CIAT22838.gnm1.Ae01:20407086-20408460 (+) | legfed_v1_0.L_KK1G2X |
| aesev.CIAT22838.gnm1.ann1.Ae01g27100 | Ae01g27100 | ultraviolet-B-repressible protein; IPR009518 (Photosystem II PsbX); GO:0009523 (photosystem II), ... | aesev.CIAT22838.gnm1.Ae01:29888045-29888416 (+) | legfed_v1_0.L_26Y4PS |
| aesev.CIAT22838.gnm1.ann1.Ae02g00560 | Ae02g00560 | oxygen-evolving enhancer protein; IPR008797 (Photosystem II PsbQ, oxygen evolving complex), ... | aesev.CIAT22838.gnm1.Ae02:337689-339097 (-) | legfed_v1_0.L_DWGMND |

## Implementation notes

- the query will be a GraphQL query run by a web component, which in turn runs an InterMine path query against LegumeMine.
- the links are not specified here -- those are the purview of the Linkout Service specification, which also specifies how they are implemented on web components like this.
