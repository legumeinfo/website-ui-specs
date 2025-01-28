# GRIN trait data query and explorer - to search or explorer the GRIN trait data 

This is the requirements doc for the SoyBase GRIN data explorer. This component should be enable users to select one or more traits from a selected "traitClass" or "traitName". For the users to learn more info about the traits, the "traitDescription" from the traits-Genus.json file, should be available to view.

## Specification version
Version: 0.2

<details>
This specification (Version 0.2) was completed in late January 2025 and was initally designed for a single species. 

</details>

## Input
  - Limited search to choosen GRIN accessions
    - Text box for choosen GRIN accessions
    - Same input as below
  - Search all GRIN accessions
    - Select at least one trait
    - Select value of trait
      - Use two text boxes for the user entered Min and Max trait score the user wantx (numerical)
      - Use a multi select dropdown if the trait value is a character (alphabetical)

### Input Mockup Images
![GRIN Explorer ALL accessions](https://github.com/legumeinfo/website-ui-specs/blob/GRIN-data-explorer/grin-data-explorer/GRIN_Explorer_Names.png "Search all accessions")

![GRIN Explorer SELECTED accessions](https://github.com/legumeinfo/website-ui-specs/blob/GRIN-data-explorer/grin-data-explorer/GRIN_Explorer_selected_acessions.png "Search selected accessions")

## Output

The output will be in a tabular layout, with the following content in each GRIN accession anchored row:
  - GRIN accession (PI ##; example: PI 567571)
  - traitName selected with values assiocated with the PI #
  - traitName selected with values assiocated with the PI #
  - traitName selected with values assiocated with the PI #
    - ? Not sure if we should limit the number of columns ?


### Output Mockup Images
![GRIN Explorer output](https://github.com/legumeinfo/website-ui-specs/blob/GRIN-data-explorer/grin-data-explorer/GRIN_Explorer_output.png "GRIN Data Explorer Results Table")

## Implementation notes

  - The data behind this tool comes from two files: traits-'Genus'.json and observations-'Genus'.json
    - (example: traits-Glycine.json and observations-Glycine.json).
      
  - The best way to link the two files is by using the "DbId" variable
    - In the traits-'Genus'.json this variable is called "traitDbId" (Example: "traitDbId": "51009")
    - In the observations-'Genus'.json this variable is called "observationVariableDbId" (Example: "observationVariableDbId": "51009")

  - Within traits-'Genus'.json file the values need for this spec are:
    - traitClass
    - traitName
    - traitDescription
    - traitDbId

  - Within observations-'Genus'.json file the values need for this spec are:
    - observationVariableDbId
    - germplasmName
    - observationVariableName
    - value







