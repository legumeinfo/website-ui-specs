## Table of contents
 - [Overview](#overview)<br>
 - [Gene search query](#gene-search)<br>
 - [QTL search](#target-urls)<br>

### Overview  <a name="overview"/>

This document provides specification for interactive search and reporting in interactive UI components to be used by the Legume Information System (LIS/Legumeinfo), SoyBase, and PeanutBase sites. Most (potentially all) of the specification content in this repository should be in the form of README documents, in appropriate subdirectories. The present README simply gives the overall objectives and approach.

The LIS, SoyBase, and PeanutBase sites are implemented using the Jekyll static site generator. Interactive features will be implemented using LIS Web Components, which are maintained in the [web-components](https://github.com/legumeinfo/web-components) repo, with documenmentation there and at [https://legumeinfo.github.io/web-components/](https://legumeinfo.github.io/web-components/). 

The specification will need to be somewhat iterative and flexible, as we learn about capabilities and constraints of the technology. Developing and maintining the spec in GitHub should help make this a living document, with changes and issues as needed.

#### Problem statement and proposed solution
Given user queries of a specified type, return results appropriate to the use case, structured appropriately. Both query forms and results will be implemented as web components. In general, results will consist of lists or tables, paginated as needed, with elements linking to other relevant tools or resources.

### Gene search query <a name="gene-search"/>
See the specification in the [gene-search](gene-search/) directory.

### QTL search query <a name="qtl-search"/>
See the specification in the [qtl-search](qtl-search/) directory.

