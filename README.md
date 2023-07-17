## Table of contents
 - [Overview](#overview)<br>
 - [Gene search query](#gene-search)<br>
 - [Trait association search (for GWAS and QTLs)](#trait-search)<br>
 - [Gene function search](#gene-function-search)<br>
 - [Browser landing/index page](#browser-landing)<br>
 - [Pangenes search](#pangenes-search)<br>

### Overview  <a name="overview"/>

This document provides specification for interactive search and reporting in interactive UI components to be used by the Legume Information System (LIS/Legumeinfo), SoyBase, and PeanutBase sites. Most (potentially all) of the specification content in this repository should be in the form of README documents, in appropriate subdirectories. The present README simply gives the overall objectives and approach.

The LIS, SoyBase, and PeanutBase sites are implemented using the Jekyll static site generator. Interactive features will be implemented using LIS Web Components, which are maintained in the [web-components](https://github.com/legumeinfo/web-components) repo, with documenmentation there and at [https://legumeinfo.github.io/web-components/](https://legumeinfo.github.io/web-components/). 

The specification will need to be somewhat iterative and flexible, as we learn about capabilities and constraints of the technology. Developing and maintining the spec in GitHub should help make this a living document, with changes and issues as needed.

#### Problem statement and proposed solution
Given user queries of a specified type, return results appropriate to the use case, structured appropriately. Both query forms and results will be implemented as web components. In general, results will consist of lists or tables, paginated as needed, with elements linking to other relevant tools or resources.

### Gene search <a name="gene-search"/>
See the specification in the [gene-search](gene-search/) directory.

### Trait search <a name="trait-search"/>
See the specification in the [trait-search](trait-search/) directory.

### Gene function search <a name="gene-function-search"/>
See the specification in the [gene-function-search](gene-function-search/) directory.

### Browser landing/index page <a name="browser-landing"/>
See the specification in the [browser-landing](browser-landing/) directory.

### Pangenes search <a name="pangenes-search"/>
See the specification in the [pangenes-search](pangenes-search/) directory.


