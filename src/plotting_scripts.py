import numpy as np
import matplotlib.pyplot as plt

def feat_importance_plot(model,names,filename,color='g',alpha=0.5,fig_size=(10,10),dpi=250):
    '''
    horizontal bar plot of feature importances
    works for sklearn models that have a .feature_importances_ method (e.g. RandomForestRegressor)
    required packages:
        numpy, matplotlib.pyplot

    imputs
    ------
    model:    class:     a fitted sklearn model
    names:    list:      list of names for all features
    filename: string:    name of file to write, with appropriate path and extension (e.g. '../figs/feat_imp.png')
    optional imputs to control plot
    ---------------
    color(default='g'), alpha(default=0.8), fig_size(default=(10,10)), dpi(default=250)
    '''
    ft_imp = 100*model.feature_importances_ / np.sum(model.feature_importances_) # funny cause they sum to 1
    ft_imp_srt, ft_names, ft_idxs = zip(*sorted(zip(ft_imp, names, range(len(names)))))

    idx = np.arange(len(names))
    plt.figure(figsize=(10,10))
    plt.barh(idx, ft_imp_srt, align='center', color=color,alpha=alpha)
    plt.yticks(idx, ft_names)

    plt.title("Feature Importances in {}".format(model.__class__.__name__))
    plt.xlabel('Relative Importance of Feature', fontsize=14)
    plt.ylabel('Feature Name', fontsize=14)
    plt.tight_layout()
    plt.savefig(filename,dpi=dpi)
    plt.close()

def output_histograms(y_true, preds):
    fig, ax = plt.subplots(1,2, figsize=(12,6))
    ax[0].hist(y_true[0][y_true[0] > 0],20, color='b', label='true')
    ax[0].hist(preds[0][preds[0] > 0],20, color='g', label='predicted')
    ax[0].set_title('slab')
    ax[0].set_xlabel('# of avalanches')
    ax[0].set_ylabel('count')

    ax[1].hist(y_true[1][y_true[1] > 0],20, color='b', label='true')
    ax[1].hist(preds[1][preds[1] > 0],20, color='g', label='predicted')
    ax[1].set_title('wet')
    ax[1].set_xlabel('# of avalanches')
    ax[1].set_ylabel('count')

    plt.legend()
    plt.show()
