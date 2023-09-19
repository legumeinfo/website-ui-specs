# Genome browser landing/index page

**This spec is intended for Jekyll-soybase**. It may also be applicable for legumeinfo.org - but the comparable result may be accomplished there instead by lis-autocontent.

The main objective for this spec is to generate a page of links to genome browsers for a genus, following a specified ordering of the species and the accessions and annotations within each species. The requirement of specifying the ordering forces reliance on one or more hand-generated files that establish that ordering. Those files exist in the Datastore metadata, in two types of "description_....yml" files.

## Specification version
Version: 1.0.0

Notes: This specification was completed mid-July, 2023. Implementation of the page was completed by late July, and may differ in some details from this spec - e.g. in layout of the assembly descriptions, citation, and browser link.

## Implementation: 

Determine the species ordering using the `GENUS/description_[glycine].yml` files:
Example:
  * `_data/datastore-metadata/Glycine/GENUS/about_this_collection/description_Glycine.yml`


Determine the ordering of accessions and annotation versions using the `Genus/species/description_[genus]_[species].yml` files
Example:
  * `_data/datastore-metadata/Glycine/max/about_this_collection/description_Glycine_max.yml`

Construct the jbrowse link for each accessions and annotation using the Datastore directory layout patterns:
  * `assembly: genus/species/genomes/strain.gnmV.AKEY/gensp.strain.gnmV.GKEY.genome_main.fna.gz`
  * `annotation: genus/species/annotations/strain.gnmV.annV.GKEY/gensp.strain.gnmV.annV.AKEY.gene_models_main.gff3.gz`

Example:
  * `assembly: Glycine/max/genomes/Lee.gnm2.K7BV/glyma.Lee.gnm2.K7BV.genome_main.fna.gz`
  * `annotation: Glycine/max/annotations/Lee.gnm2.ann1.1FNT/glyma.Lee.gnm2.ann1.1FNT.gene_models_main.gff3.gz`

The jekyll code at the end of [this index page (commit d82f060)](https://github.com/soybase/jekyll-soybase/blob/main/tools/browsers/index.html) implements much of the concept above, but doesn't employ the two description_ files to order the links. That code is [rendered here (as of 2023-07-10)](https://dev.soybase.org/tools/browsers).


```
{% capture jbrowse_base_url %}/assets/js/jbrowse{% endcapture %}
{% assign genus = "Glycine" %}

{% for species_dir in site.data.datastore-metadata[genus] %}
  {% assign species = species_dir[0] %}
  {% if species == "GENUS" %}
    {% continue %}
  {% endif %}
  <h4><i>Glycine {{ species }}</i> accessions</h4>
  {% for datatype_dir in species_dir[1] %}
    {% assign datatype = datatype_dir[0] %}
    {% if datatype == "annotations" %} 
      {% for collection_dir in datatype_dir[1] %}
        {% assign collection = collection_dir[0] %}
        {% for metadata_file in collection_dir[1] %}
          {% if metadata_file[0] contains "README" %}
            {% assign readme = metadata_file[1] %}
            {% assign assembly = readme.identifier | split: '.' | slice: 0, 2 | join: '.' %}
            {% assign annotation = readme.identifier | split: '.' | slice: 0, 3 | join: '.' %}
            {% for datatype_dir in species_dir[1] %}
              {% assign datatype = datatype_dir[0] %}
              {% if datatype == "genomes" %} 
                {% for collection_dir in datatype_dir[1] %}
                  {% assign collection = collection_dir[0] %}
                  {% for metadata_file in collection_dir[1] %}
                    {% if metadata_file[0] contains "README" %}
                      {% assign readme_genome = metadata_file[1] %}
                      {% assign assembly_genome = readme_genome.identifier | split: '.' | slice: 0, 2 | join: '.' %}
                      {% if assembly_genome == assembly %}
                        {% assign chromosome_prefix = readme_genome.chromosome_prefix %}
                        {% assign synopsis = readme_genome.synopsis %}
                      {% endif %}
                    {% endif %}
                  {% endfor %}
                {% endfor %}
              {% endif %} 
            {% endfor %}
            <dt><a target="_blank" href="{{ jbrowse_base_url }}/?assembly={{ assembly }}&tracks={{ annotation }}&loc={{ readme.scientific_name_abbrev }}.{{ assembly }}.{{ chromosome_prefix }}01:1-1000000">{{ assembly }}</a></dt>
            <dd>{{ synopsis }}</dd>
          {% endif %}
        {% endfor %}
      {% endfor %}
    {% endif %}
  {% endfor %}
  <hr>
{% endfor %}
```

## Page output would look roughly like the following. 
Bold annotation.assembly items represent JBrowse links.

---

# Genome browsers

Genome browsers are available for most of the genome assemblies at SoyBase. These can be accessed from the GENOMICS tab, with browsers listed under each accession -- or directly from the links below.

## _Glycine max_

### Reference assemblies (current first)
**Wm82_ISU01.gnm2**  
Synopsis synopsis synopsis.  
**Wm82.gnm4**  
Synopsis synopsis synopsis.  
**Wm82.gnm2**  
Synopsis synopsis synopsis.  
**Wm82.gnm1**  
Synopsis synopsis synopsis.  
**Lee.gnm2**  
Synopsis synopsis synopsis.  
**Lee.gnm1**  
Synopsis synopsis synopsis.  
**FiskebyIII.gnm1**  
Synopsis synopsis synopsis.  
**Zh13.gnm2**  
Synopsis synopsis synopsis.  
**Zh13.gnm1**  
Synopsis synopsis synopsis.  
**Hwangkeum.gnm1**  
Synopsis synopsis synopsis.  

### Pangenome collection by Chu, Peng et al., 2021
**Hefeng25_IGA1002.gnm1**  
Synopsis synopsis synopsis.  
**Huaxia3_IGA1007.gnm1**  
Synopsis synopsis synopsis.  
**Jinyuan_IGA1006.gnm1**  
Synopsis synopsis synopsis.  
**Wenfeng7_IGA1001.gnm1**  
Synopsis synopsis synopsis.  
**Wm82_IGA1008.gnm1**  
Synopsis synopsis synopsis.  
**Zh13_IGA1005.gnm1**  
Synopsis synopsis synopsis.  
**Zh35_IGA1004.gnm1**  
Synopsis synopsis synopsis.  

### Pangenome collection by Liu, Du et al., 2020
**58-161.gnm1**  
Synopsis synopsis synopsis.  
**Amsoy.gnm1**  
Synopsis synopsis synopsis.  
**DongNongNo_50.gnm1**  
Synopsis synopsis synopsis.  
**FengDiHuang.gnm1**  
Synopsis synopsis synopsis.  
**HanDouNo_5.gnm1**  
Synopsis synopsis synopsis.  
**HeiHeNo_43.gnm1**  
Synopsis synopsis synopsis.  
**JiDouNo_17.gnm1**  
Synopsis synopsis synopsis.  
**JinDouNo_23.gnm1**  
Synopsis synopsis synopsis.  
**JuXuanNo_23.gnm1**  
Synopsis synopsis synopsis.  
**KeShanNo_1.gnm1**  
Synopsis synopsis synopsis.  
**PI_398296.gnm1**  
Synopsis synopsis synopsis.  
**PI_548362.gnm1**  
Synopsis synopsis synopsis.  
**QiHuangNo_34.gnm1**  
Synopsis synopsis synopsis.  
**ShiShengChangYe.gnm1**  
Synopsis synopsis synopsis.  
**TieFengNo_18.gnm1**  
Synopsis synopsis synopsis.  
**TieJiaSiLiHuang.gnm1**  
Synopsis synopsis synopsis.  
**TongShanTianEDan.gnm1**  
Synopsis synopsis synopsis.  
**WanDouNo_28.gnm1**  
Synopsis synopsis synopsis.  
**XuDouNo_1.gnm1**  
Synopsis synopsis synopsis.  
**YuDouNo_22.gnm1**  
Synopsis synopsis synopsis.  
**ZhangChunManCangJin.gnm1**  
Synopsis synopsis synopsis.  
**Zhutwinning2.gnm1**  
Synopsis synopsis synopsis.  
**ZiHuaNo_4.gnm1**  
Synopsis synopsis synopsis.  

## _Glycine soja_
### Chu, Peng et al., 2021
**F_IGA1003.gnm1**  
Synopsis synopsis synopsis.  

### Liu, Du et al., 2020
**PI_549046.gnm1**  
Synopsis synopsis synopsis.  
**PI_562565.gnm1**  
Synopsis synopsis synopsis.  
**PI_578357.gnm1**  
Synopsis synopsis synopsis.  

### Valliyodan, Cannon et al., 2019
**PI483463.gnm1**  
Synopsis synopsis synopsis.  

### Xie, Chung et al.,
**W05.gnm1**  
Synopsis synopsis synopsis.  

## _Glycine D3-tomentella_
**G1403.gnm1**  
Synopsis synopsis synopsis.  

## _Glycine dolichocarpa_
**G1134.gnm1**  
Synopsis synopsis synopsis.  

## _Glycine falcata_
**G1718.gnm1**  
Synopsis synopsis synopsis.  

## _Glycine stenophita_
**G1974.gnm1**  
Synopsis synopsis synopsis.  

## _Glycine syndetika_
**G1300.gnm1**  
Synopsis synopsis synopsis.  

