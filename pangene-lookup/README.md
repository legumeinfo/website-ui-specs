# PanGene Lookup UI

This is the requirements doc for the LIS gene correspondence lookup UI.
Specifically, the pangene for a given set of gene IDs will be looked up using the pangene sets as a translator.

## Specification version
Version: 0.2

<details>
Version 0.1 of this spec was completed in June 2024. A web component prototyping the specified UI was implemented. Based on the prototype, requests for changes to the spec were made. These changes were implemented added to version 0.2 of the spec.

</details>

## Input

- input gene id list (required, can't contain more than 100 ids)
- genus (required selector, not "any"). In single-genus contexts (e.g. PeanutBase or SoyBase), allow this value to be pre-set.
- species (optional selector populated after genus selected)
- strain (optional selector populated after species selected)
- assembly version (optional selector populated after strain specified)
- annotation version (optional selector populated after assembly version specified)
- do the lookup button
- download all results (as TSV) button

Examples are shown below the gene id list input element. (Selectors are self-explanatory.)

## Output

The output will be in a paginated tabular layout, with the following content in each input gene-anchored row:

- full input gene identifier (linked to Gene Linkout Service) e.g. `glyma.Zh13.gnm2.ann1.SoyZH13_06G241600`
- matched PanGeneSet Id (linked to PanGeneSet Linkout Service) e.g. `Glycine.pan4.pan00079`
- target annotation gene identifier (linked to Gene Linkout Service) e.g. `glyma.Wm82.gnm4.ann1.Glyma.06G262100`

Note that an input gene may not have any matching genes in the target annotation (either because the input gene id is not present in a pangeneset or because it is not present in a pangeneset with one or more genes from the target annotation). Unmatched input ids should be reported in a notification element to make their lack of correspondence explicit.
Also note that in the case of multiple corresponding genes, we propose to create multiple output rows (i.e. multiple rows corresponding to the same input gene id), but this target gene id set could be "rolled up" in a future version if deemed preferable.

Future enhancements will include:
  - input gene list from file

### Mockup

![image](https://github.com/legumeinfo/website-ui-specs/raw/main/pangeneset-based-gene-id-translation/ui.png)


## Implementation notes

- the query will be a GraphQL query run by a web component, which in turn runs an InterMine path query against LegumeMine.
