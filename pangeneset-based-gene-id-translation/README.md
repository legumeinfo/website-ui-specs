# PanGeneSet-based gene id translation UI

This is the requirements doc for the LIS gene correspondence pangeneset-based translator to be implemented on the LIS Jekyll web site.

## Specification version
Version: 0.1

<details>

</details>

## Input

- genus (required selector, not "any"). In single-genus contexts (e.g. PeanutBase or SoyBase), allow this value to be pre-set.
- Species (required selector populated after genus selected)
- strain (required selector populated after species selected)
- assembly version (required selector populated after strain specified)
- annotation version (required selector populated after assembly version specified)
- input gene id list
- do the lookup button

Examples are shown below the gene id list input element. (Selectors are self-explanatory.)

## Output

The output will be in a tabular layout, with the following content in each input gene-anchored row:

- full input gene identifier (linked to Gene Linkout Service) e.g. `glyma.Zh13.gnm2.ann1.SoyZH13_06G241600`
- matched PanGeneSet Id (linked to PanGeneSet Linkout Service) e.g. `Glycine.pan4.pan00079`
- target annotation gene identifier (linked to Gene Linkout Service) e.g. `glyma.Wm82.gnm4.ann1.Glyma.06G262100`

Note that an input gene may not have any matching genes in the target annotation (either because the input gene id is not present in a pangeneset or because it is not present in a pangeneset with one or more genes from the target annotation). Unmatched input ids should be given rows in the output table to make their lack of correspondence explicit.
Also note that in the case of multiple corresponding genes, we propose to create multiple output rows (ie multiple rows corresponding to the same input gene id), but this target gene id set could be "rolled up" in a future version if deemed preferable.

Pagination of the result sets seems less appropriate in this context than in queries, so we propose to display the full results in the table.

Future enhancements will include:
  - results table download
  - input gene list from file

### Mockup

![image](https://github.com/legumeinfo/website-ui-specs/raw/main/pangeneset-based-gene-id-translation/ui.png)


## Implementation notes

- the query will be a GraphQL query run by a web component, which in turn runs an InterMine path query against LegumeMine.
