# NUST query portal

This is the requirements doc for the SoyBase **NUST** (Northern Uniform Soybean Trials). 

## Specification version
Version: 0.1 

<details>
This specification (Version 0.1) was taken from legacy SoyBase and was initially designed for only NUST data. 

</details>

## Input Data

### Input Mockup Images

#### General Phenotype Search Tool
<img width="910" height="558" alt="NUST-GPST" src="https://github.com/user-attachments/assets/722ea173-22d8-4bc5-9e3b-e8f08f216e3a" />

#### Strain Search Tool
<img width="880" height="317" alt="NUST-SST" src="https://github.com/user-attachments/assets/6b3fd136-a8cb-4acd-ae50-a4d280a8e5f0" />

#### Specific Strain Phenotype Search Tool 
<img width="855" height="550" alt="NUST-SSPST" src="https://github.com/user-attachments/assets/f5ba9857-f7f4-451d-bf71-60b59c9838d0" />

#### Common Test Tool
<img width="885" height="317" alt="NUST-CTT" src="https://github.com/user-attachments/assets/7a095121-f68f-4a0b-a57e-f28e12a613b2" />

## Output
#### General Phenotype Search Table

5 separate tables are presented in the output
**Check Stains Table**
| YEAR | TEST | STRAIN    | PHENOTYPE   |
| ---- | ---- | --------  | ----------- |
| 2025 | UTII |  IA2102   |    MG II    |
| 2025 | UTII | MN1905CN  | Early-MG II |

**Phenotype Location Means Table**
| YEAR | TEST | LOCATION  |   STRAIN   | PHENOTYPE |    VALUE    |
| ---- | ---- | --------  | ---------- | --------- | ----------- |
| 2025 | UTII | Ames, IA  |   IA2102   | YieldBuA  | 64.7Bu/Acre |
| 2025 | UTII | Ames, IA  |  MN1905CN  | YieldBuA  | 63.8Bu/Acre |

**Replicates Table**
| YEAR | TEST | LOCATION  |   STRAIN   | REP # | PHENOTYPE | VALUE |
| ---- | ---- | --------  | ---------- | ------| --------- | ----- |
| 2025 | UTII | Ames, IA  |   IA2102   |   1   | YieldBuA  |  53.7 |
| 2025 | UTII | Ames, IA  |   IA2102   |   2   | YieldBuA  |  69.9 |
| 2025 | UTII | Ames, IA  |   IA2102   |   3   | YieldBuA  |  70.3 |
| 2025 | UTII | Ames, IA  |  MN1905CN  |   1   | YieldBuA  |  55.4 |
| 2025 | UTII | Ames, IA  |  MN1905CN  |   2   | YieldBuA  |  62.7 |
| 2025 | UTII | Ames, IA  |  MN1905CN  |   3   | YieldBuA  |  73.3 |
 
**Locations Table**
| YEAR| TEST | LOCATION| LAT |  LONG| CONDUCTOR | PLANTING DATE | ROW SPACING | MATURITY DATE |
| ----| ---- | ------- | --- | -----| --------- | ------------- | ----------- | ------------- |   
| 2025| UTII | Ames,IA | 42.0| -93.7|   Singh   |      132      |     30      |      149      |
| 2025| UTII | Ames,IA | 40.9| -93.4|   Singh   |      126      |     30      |      164      |

  - Columns included are: YEAR, TEST, LOCATION, LAT, LONG, CONDUCTOR, PLANTING DATE, ROW SPACING, MATURITY DATE, DAYS TO MATURITY, DAYS TO MATURITY
5. Strains Table
  - Columns included are: YEAR, TEST, STRAIN, DESCRIPTIVE CODE, UNIQUE TRAITS, GENERATION COMPOSITION (GEN. COMP)



### Output Mockup Images


#### General Phenotype Search Table

#### Strain Search Table

#### Specific Strain Phenotype Search Table

#### Common Test Table




## Implementation notes


