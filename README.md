pipeline for raw fastq to vcf

How to run this pipeline:

0. Install miniconda3

You can check for an installation with ```which conda```
If it returns an empty line, follow the instructions starting from step 1 at this link:
http://snakemake.readthedocs.io/en/stable/tutorial/setup.html

1. Clone this repository to your working environment

```
https://github.com/kramundson/nico-snp
cd nico-snp
```

2. Build and activate a conda environment using the included environment.yaml file.
As an example, I named the environment nico-snp, but you can call it whatever you want.

```conda env create --name nico-snp -f environment.yaml
source activate nico-snp
```

3. Change units.tsv to suit your needs

Sample column corresponds to a unique biological entity. Specify the ploidy before the
name of the sample as follows:

ploidy_samplename

where ploidy is either 2x or 4x. For example, a dihaploid sample named plant-77 would be:

2x-plant-77

Unit corresponds to the unique combination of biological entity, sequencing library, and
sequencing run. This enables libraries and runs to be merged later on.

For example, if two gDNA libraries from plant_77 were made and sequenced, add two
rows to units.tsv, one for each sequenced library:

sample  unit
2x-plant-77 SRR7809119
2x-plant-77 SRR7809120

NCBI SRR id numbers are a convenient choice for the units column.

Column fq1 specifies the name of the forward read fastq file (assuming uninterleaved files)
Column fq2 specifies the corresponding reverse reads.

4. Copy reads specified by fq1 and fq2 in your units.tsv to data/reads. The pipeline will
look for files located there.

5. Edit config.yaml to specify target files. For larger projects, you'll want to make a
file that contains the corresponding target files to prevent an overly long config.yaml.

Note: An example framework using SRA data with appropriately formatted units.tsv and
config.yaml is included.

todo: read targets in from file or expand from output

6. Once files have been configured, execute Snakemake dry run

```snakemake -np```

7. Run pipeline

```snakemake --cores 16```