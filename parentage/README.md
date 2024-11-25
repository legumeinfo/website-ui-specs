# Parentage and pedigree report page

This is the initial/draft requirements doc for the SoyBase parentage and pedigree report page. Implementation will probably be as a Jekyll page, calling a back-end service similar to
https://www.soybase.org/tools/analysis/go.html

Page address (to replace current content at that location): tools/parentage/index.html


## Specification version
Version: 0.6.0

<details>

v0.5.0 First draft, 2024-11-07. Initial UI spec and back-end service implementation. The API has two endpoints: one generating a zip file to be passed to the Helium web application, and the other being plain-text to be used for the report on the website.

v0.6.0 Second draft, 2024-11-25. Update back-end code and API. In this version, the text report is in JSON format. 

</details>

## Input

**Page text:**

Soy Parentage and Pedigrees

Enter the name of a soybean line to get a report of its parents, pedigree, synonyms, and notes for that line.

Soybean line: [  ]
  Examples: Franklin, Flyer, Maverick, Jack

You may also browse and search accessions beginning with ...

 0-9  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  R  S  T  U  V  W  X  Y  Z 


### Report:

**Report:**

```
Pedigree:
  [Pedigree viewer]
    For an interactive plot of the pedigree, click the "Pedigree viewer" button, then choose "Import".

Text representaton of pedigree for Hardin (showing first the immediate parents, then progressively earlier crosses):
  Hardin ==	( Corsoy 3 , Cutler 71 )
  Hardin ==	( Corsoy 3 , ( Cutler 4 , SL5 ) )
  Hardin ==	( Corsoy 3 , ( Cutler 4 , ( ( Kent 7 , L49-4196 ) , ( Kent 8 , Mukden ) ) ) )


Hardin is in the pedigree of these lines: 05KL119276, 05KL135608, Asgrow A2242, MT002989, OW1012750, PI 669396, Syngenta S16-Y6, XP1928

Alternate names for Hardin: PI 548526, A76-102009

Comments for Hardin: PVP 8100052
```


## Implementation notes

For the code that generates the pedigrees and reports, see
https://github.com/soybase/parentage/

Calculate the pedigree for use in the Helium application using this API:

  https://app.soybase.org/api/parentage/

... which has two types of endpoints:

1. Text content for the report above, in JSON format, called as:

   `https://app.soybase.org/api/parentage/<query>`
   
   https://app.soybase.org/api/parentage/Essex

   See https://github.com/soybase/parentage/ for a description of the JSON data structure. 
   Briefly, it is a hash of arrays. The hash keys are: 
     `table`, `query`, `comments`, `synonyms`, `matches`, `construction`
  The value of `table` can be ignored, since this is the same as the contents of pedigree.helium.zip.
  All other elements are to be used to populate the report.


3. A file named `pedigree.helium.zip` that can be passed, as a URL address, to the [Helium](https://helium.hutton.ac.uk/#/pedigree) application, like so:

   `https://helium.hutton.ac.uk/#/pedigree?germinateUrl=[URL-to-pedigree.helium.zip]`
  
   https://helium.hutton.ac.uk/#/pedigree?germinateUrl=https://app.soybase.org/api/parentage/Gnome/pedigree.helium.zip
    
   https://helium.hutton.ac.uk/#/pedigree?germinateUrl=https://app.soybase.org/api/parentage/N17-31531/pedigree.helium.zip


For the data used for browsing ("browse and search accessions beginning with"), the accessions/lines 
used to populate the alphabetical lists are at 
[data/parentage.tsv](https://github.com/soybase/parentage/blob/main/data/parentage.tsv) 
in the https://github.com/soybase/parentage repository.
