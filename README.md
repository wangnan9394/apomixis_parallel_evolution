# apomixis_parallel_evolution
## Cite:Structural variation and parallel evolution of apomixis in citrus during domestication and diversification
<https://doi.org/10.1093/nsr/nwac114>
## About the data
see:https://doi.org/10.5281/zenodo.5748662

A groups of data and scripts in the analysis

Multi_test.py //perform multiple test

Specific_Species_marker_step1.py //prepare a specific species marker file, I divided it into three steps.
Specific_Species_marker_step2.py
Specific_Species_marker_step3.py

admixture_sorted_on_tree.py //sort the admixture results based on a phylogeny

deleterious_sites.txt //a file including deleterious sites

deletrious_stats.py // statistic the deleterious sites in each samples, there are three models as the paper

hemizygosity_stats.py //count the hemizygosity regions(genes) in the genome

reduce_ref_bias_on_outgroup.py //reduce the reference bias by outgroup variants

used_docker.list // a list including software in docker, I make a lot of docker imgaes which could be directly used, 3ks!! ):

Anno.SIFT.bed // a bed file used in SIFT statistics.

apomixis_transition.slim // a slim3 scripts for apomxixis transiton after admixture

## work_flows
BSA.pipeline //a pipeline for bulked segregant analysis(BSA) analysis

Dsuite.pipeline //a pipeline for Dsuite analysis

SV_detects.pipeline //a pipeline for SV_detect using delly and lumpy

popoTE2.pipeline //a pipeline for MITE insertion analysis

population_strcture.pipeline  //a pipeline for population strcture analysis

smcpp.pipeline  //a pipeline for effective population size anlysis

