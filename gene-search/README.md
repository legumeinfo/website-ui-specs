# Gene search query

This is the requirements doc for the LIS gene search to be implemented on the LIS Jekyll web site.

## Specification version
Version: 1.2.0

<details>

A draft of this specification was completed in March 2023. Based on initial implementation of the spec and review of that implementation [issue #128](https://github.com/legumeinfo/web-components/issues/128), additional changes were made to better handle pagination and back-navigation from the modal linkouts results window.

After another round of review in mid-July 2023, the intermediate output was changed from vertical layout of the results for each gene to a tabular layout per gene, based on this rationale from Alan (Aug 4, lis-developers discussion thread): <i>"... the generic paginated search class the component is based on draws results using a table, but the gene search component overrides this to draw results as a list. While the list is aesthetically pleasing, it can only be configured by forking the repository and modifying the code, whereas the table can be configured at run-time, i.e. no forking necessary."</i>

Initial public release of this web component at legumeinfo.org was on August 9. Code for this spec-1.1 release is [documented here](https://legumeinfo.github.io/web-components/classes/user_components.LisGeneSearchElement.html).

The history above predates a versioning system for these website-ui specs. In September 2023, semantic versioning was added, with 1.1.0 being used in this spec to reflect the first production release of this gene-search web component -- minor version 1 indicating that significant changes were made in June-July after review of the initial implementation in March.

September 19: update spec version to 1.1.1 -- the minor version increment reflecting that the Gene search field should be parameterizable in the web component, to allow fixing the genus to e.g. Arachis or Glycine, for use at a genus-specific site or context.  **Note: This was a new feature and should have bumped the version to 1.2.0.**

November 17: similar to the September 19 update, the spec was updated to allow the species parameter to also be parameterizable. As such, the spec version was incremented to 1.2.0.
</details>

## Input

- genus (selector with "any" on top). In single-genus contexts (e.g. PeanutBase or SoyBase), allow this value to be pre-set.
- Species (selector populated if genus specified, otherwise only "any" - unless pre-set to some value, e.g. max)
- strain (selector populated if species specified, otherwise only "any")
- gene identifier (text input)
- gene description (text input)
- gene family identifier (text input)
- search button

Examples are shown below each text input element. (Selectors are self-explanatory.)

### Mockup

![image](https://user-images.githubusercontent.com/5657219/231203688-f7493a37-f98a-42ef-a1f8-66b1395fbd76.png)

## Output

The output will be in a tabular layout, with the following content in each gene-anchored row:

- gene name (typically originating from Name attribute in LIS GFF) e.g. `Ae01g16390`
- full LIS identifier (linked to Linkout Service) e.g. `aesev.CIAT22838.gnm1.ann1.Ae01g16390`
- locations, e.g. `glyma.Wm82.gnm2.Gm13:44545582-44550666 (1) (chromosome)`
- gene description (typically originating from Note attribute in LIS GFF) e.g. `oxygen-evolving enhancer protein; IPR008797 (Photosystem II PsbQ, oxygen evolving ...`
- gene family identifier (linked to Linkout Service) e.g. `legfed_v1_0.L_KK1G2X`
- genus, e.g. *Glycine*
- species, e.g. *max*
- strain, e.g. Wm82

Note that this tabular layout differs from the initial specification of a vertical list layout per gene. See rationale under the specification version notes.

### Mockup

<img width="1397" alt="output_mockup_v1 1" src="https://github.com/legumeinfo/website-ui-specs/assets/3588740/a37bc154-5038-4024-b1dc-7dc471fecbcb">

## Implementation notes

- the query will be a GraphQL query run by a web component, which in turn runs an InterMine path query against LegumeMine.
- the linkouts are not specified here -- those are the purview of the Linkout Service specification, which also specifies how they are implemented on web components like this.
