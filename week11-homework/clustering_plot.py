#!/usr/bin/env python

import scanpy as sc
from matplotlib.pyplot import rc_context

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5") # Read 10x dataset
adata.var_names_make_unique() # Make variable names (in this case the genes) unique

adata_filtered = sc.pp.recipe_zheng17(adata, copy = True) #filter most variable genes as they did in zheng17, copy puts them in adata_filtered instead of updating adata

sc.tl.pca(adata) #perform pca on adata, updates adata by default
sc.tl.pca(adata_filtered) #perform pca on adata_filtered

sc.pl.scatter(adata, basis='pca', save='_plot_pre_filter.png') #plot adata, tell function it was analyzed by pca so it knows how to plot, save
sc.pl.scatter(adata_filtered, basis='pca', save='_plot_post_filter.png') #plot adata_filtered, tell function it was analyzed by pca so it knows how to plot, save

sc.pp.neighbors(adata_filtered)
sc.tl.leiden(adata_filtered)

sc.tl.tsne(adata_filtered)
sc.pl.scatter(adata_filtered, basis='tsne', color='leiden', save='_plot.png')

sc.tl.umap(adata_filtered,maxiter=1000)
sc.pl.scatter(adata_filtered, basis='umap', color = 'leiden', save='_plot.png')

sc.tl.rank_genes_groups(adata_filtered,'leiden', method='t-test')
sc.pl.rank_genes_groups(adata_filtered, save='genes_ranked_ttest.png')

sc.tl.rank_genes_groups(adata_filtered,'leiden', method='logreg')
sc.pl.rank_genes_groups(adata_filtered, save='lower_resolution_genes_ranked_log.png')

marker_genes_dict = {
    'Pericyte': ['Abcc9', 'Rgs5'],
    'Microglia': ['Fcgr3', 'C1qb', 'C1qc'],
    'FB1' : ['Nr2f2','Nr2f1'],
    'FB2' : ['1500015O10Rik'],
    'Endothelial' : ['Egfl7', 'Cldn5'],
    'Oligodendrocyte': ['Olig1', 'Olig2'],
    'Astrocyte': ['Gria1', 'Sox1'],
}

sc.pl.stacked_violin(adata_filtered, marker_genes_dict, groupby='leiden', swap_axes=False, dendrogram=True, save='_plot')

# sc.set_figure_params(dpi=100, color_map = 'viridis_r')
# sc.settings.verbosity = 1
# sc.logging.print_header()
#
# with rc_context({'figure.figsize': (4, 4)}):
#     sc.pl.scatter(adata_filtered, basis='umap', color = ['Ndrg2', '1500015O10Rik', 'Vim', 'Wnt8b', 'Tnni3', 'Aldoc', 'Phgdh', 'Neurog2', 'Tnc', 'Dbi', 'Atp1a2', 'Ckb', 'Ptn', 'Parp3', 'Fabp7', 'Gas1', 'Mt3', 'Asb17os'], save='cluster_4_plot.png')
#
cluster2annotation = {
     '0': 'Unclear',
     '1': 'Astrocyte',
     '2': 'Unclear',
     '3': 'Unclear',
     '4': 'FB2',
     '5': 'Unclear',
     '6': 'Unclear',
     '7': 'Unclear',
     '8': 'Unclear',
     '9': 'Unclear',
     '10': 'Unclear',
     '11': 'Unclear',
     '12': 'Unclear',
     '13': 'FB1',
     '14': 'Unclear',
     '15': 'Unclear',
     '16': 'FB1',
     '17': 'Unclear',
     '18': 'Unclear',
     '19': 'Oligodendrocyte',
     '20': 'FB2',
     '21': 'Endothelial Cells',
     '22': 'FB1',
     '23': 'Pericyte',
     '24': 'Microglia',
     '25': 'Unclear',
     '26': 'Astrocyte',
     '27': 'Unclear',
}

adata_filtered.obs['cell type'] = adata_filtered.obs['leiden'].map(cluster2annotation).astype('category')

sc.pl.umap(adata_filtered, color='cell type', legend_loc='on data',
           frameon=False, legend_fontsize=10, legend_fontoutline=2, save='_cell_type_plot')

