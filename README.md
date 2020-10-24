# SHARE-seq-alignment
Pipeline for demultiplex and align both ATAC and RNA data generated in SHARE-seq

Dependencies: GNU parallel, Bcl2fastq, fastp, zcat, STAR, bowtie2, python2, umi_tools, samtools, picard, R, featureCounts, read_distribution.py from RSeQC, bedtools

After installing, update the general configuration section in main script "Split_seq_example.sh":
1) myPATH # change it to where the SHARE-seq scripts are installed. e.g. myPATH='/mnt/users/Script/share-seq-github-v1/'
2) pythohPATH # change it to where python2 is installed e.g. pythohPATH='/usr/bin/python' 
3) picardPATH # change it to where picard is installed e.g. picardPATH='/mnt/bin/picard/picard.jar'

# How to run the script?
A small set of fastq files for testing are in the test_fastq_nova/ folder
Before running, three sections in the main script "Split_seq_example.sh" need to be updated for each run, inlcuding 
A) paths B) sample configuration C) fastq configuration

## fastq configuration
Indexed=F # T or F; defaul is F, indicate if the fastq reads are already indexed

Start=Fastq_Merge # Bcl or Fastq_Merge (when fastq were generated per run) or Fastq_SplitLane (when fastq were generated per sequencing lane)

Runtype=full # QC or full;  QC only analyze 12M reads to get a quick sense of data

Sequencer=Novaseq # Novaseq or Nextseq;  miseq or nova-seq has the same sequencing direction, use "Novaseq" for either

## sample configuration
Project=(sp.rna sp.atac.first) # use differnt name for each sample

Type=(RNA ATAC)  # ATAC or RNA

Genomes=(hg19 both) # both mm10 hg19

RawReadsPerBarcode=(10 10) # reads cutoff for the unfiltered bam, use 100 to remove barcode with few reads for “full" run and speed up processing ; use 10 for QC runs

ReadsPerBarcode=(1 1) # reads cutoff for the filtered bam 100 for full run of ATAC and RNA, 1 for QC run \n
keepMultiMapping=(F F)  # T or F; default is F

## RNA-seq options
The pipeline also offers flexible RNA-seq specific options for advanced users. 

removeSingelReadUMI=F # T or F; default is F. If T, UMIs with single read will be removed.

keepIntron=T # T or F; default is T. If F, intronic RNA reads will be discarded.

matchPolyT=F # T or F; default is F. If T, will try to find match of TTTTTT (allowing 1 mis-match) in 11-16 bp position of biological read2. If match is not identified, read will be disgarded. Only works if Read2 is longer than 16 bp.

SkipPolyGumi=F # T or F; default is F, pipeline will remove polyG UMIs. If T, pipeline will keep polyG UMIs.

genename=gene_name # gene_name (official gene symbol) or gene_id (ensemble gene name), gene_name is default

refgene=gencode # gencode or genes; gencode is default; genes is UCSC refseq genes; gencode also annotates nc-RNA
