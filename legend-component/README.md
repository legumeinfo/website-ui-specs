# Species legend (web component)

This is the requirements doc for the species legend web component, with labels and interactive dots/symbols.

## Specification version
Version: 0.1.0

<details>

The initial spec (0.1.0) was drafted 2025-04-02.

</details>

## Objective
The purpose of this component is to provide a legend that associated named entities (e.g. species) with symbols (e.g. colored dots or squares).
It is presumed that this component will be paired with others on a webpage. Current applications would be the phylotree viewer and the Genome Context Viewer.


## Essential features:

  - Layout options suited to the envisioned applications
  - Ability to receive data to be used for labels and associated symbols
  - Ability to communicate actions to other components (actions being clicks or rollovers, depending on context)

## Desirable but not essential features:
  - Snapshot to SVG

## Desired layout options:

### Tabular layout, horizontally-arrayed:

  |                      |                   |                      |                     |
  | ---------------------| ----------------- | -------------------- | ------------------- |
  | [o] Genus species    | [o] Genus speci   | [o] Genus species    | [o] Genus speciess  |
  | [o] Genus spec       | [o] Genus spe     | [o] Genus speciess   | [o] Genus spec      |
  | [o] Genus speciesss  | [o] Genus sp


<img src="legend_phylotree.png" alt="legend_phylotree.png" width="318px" >



### Vertical layout, X-before:

  |                     |
  | :------------------ |
  | [o] Genus species   |
  | [o] Genus spec      |
  | [o] Genus speciesss |
  | [o] Genus speci     |
  | [o] Genus spe       |
  | [o] Genus sp        |
  | [o] Genus species   |
  | [o] Genus speciess  |
  | [o] Genus spec      |


### Vertical layout, X-after:

  |                      |
  | -------------------: |
  | Genus species    [o] |
  | Genus spec       [o] |
  | Genus speciesss  [o] |
  | Genus speci      [o] |
  | Genus spe        [o] |
  | Genus sp         [o] |
  | Genus species    [o] |
  | Genus speciess   [o] |
  | Genus spec       [o] |


<img src="legend_gcv.png" alt="legend_gcv.png" width="174px" >




