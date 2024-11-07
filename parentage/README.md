# Parentage and pedigree report page

This is the initial/draft requirements doc for the SoyBase parentage and pedigree report page. Implementation will probably be as a Jekyll page, calling a back-end service similar to
https://www.soybase.org/tools/analysis/go.html

Page address (to replace current content at that location): pedigree/index.html


## Specification version
Version: 0.5.0

<details>

First draft on 2024-11-07.

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
    
  https://app.soybase.org/api/parentage/<query>/pedigree.helium.zip
 
Example:
  https://app.soybase.org/api/parentage/Gnome/pedigree.helium.zip

Pass that result to helium.hutton.ac.uk like so:
  https://helium.hutton.ac.uk/#/pedigree?germinateUrl=[URL-to-pedigree.helium.zip]

Example:
  https://helium.hutton.ac.uk/#/pedigree?germinateUrl=https://app.soybase.org/api/parentage/Gnome/pedigree.helium.zip

