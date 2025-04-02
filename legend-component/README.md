# Legend (web component)

This is the requirements doc for a legend web component, with labels and interactive dots/symbols.

## Specification version
Version: 0.1.0

<details>

The initial spec (0.1.0) was drafted 2025-04-02.

</details>

## Objective
The purpose of this component is to provide a legend that associated named entities (e.g. species or gene family IDs) 
with symbols (e.g. colored dots or squares).
It is presumed that this component will be paired with others on a webpage. 
Current applications would be the phylotree viewer and the Genome Context Viewer.

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



### Vertical layout, symbol before:

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


### Vertical layout, symbol after:

  |                        |
  | ---------------------: |
  |  Legume.fam3.00470 [o] |
  |  Legume.fam3.00505 [o] |
  |  Legume.fam3.00735 [o] |
  |  Legume.fam3.00761 [o] |
  |  Legume.fam3.00764 [o] |
  |  Legume.fam3.00859 [o] |
  |  Legume.fam3.00926 [o] |
  |  Legume.fam3.01028 [o] |
  |  Legume.fam3.01096 [o] |


<img src="legend_gcv.png" alt="legend_gcv.png" width="174px" >




