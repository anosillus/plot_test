FROM continuumio/miniconda3:4.8.2

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
RUN mkdir -p ~/.jupyter && { \
    echo "c.NotebookApp.allow_root = True"; \
    echo "c.NotebookApp.ip = '0.0.0.0'"; \
    echo "c.NotebookApp.token = ''"; \
    echo "c.JupyterLabTemplates.template_dirs = ['/root/template']"; \
    echo "c.JupyterLabTemplates.include_default = True"; \
    } | tee ~/.jupyter/jupyter_notebook_config.py
ENV PATH /opt/conda/bin:$PATH
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends fonts-ipafont fonts-ipaexfont fonts-noto-cjk build-essential sudo \
    inkscape jed  libsm6  libxext-dev  libxrender1  lmodern  netcat  python-dev \
    # ---- nbconvert dependencies ----
    texlive-xetex  texlive-fonts-recommended  texlive-generic-recommended  tzdata unzip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
ENV CONDA_DIR=/opt/conda
RUN $CONDA_DIR/bin/conda install -c conda-forge \
      pandas
RUN $CONDA_DIR/bin/conda install -c conda-forge \
      # geoplot \
      # ggplot \
      matplotlib \
      matplotlib-venn \
      nodejs \
      pandas \
      scikit-learn \
      seaborn
      # pandoc
RUN conda install notebook ipywidgets
RUN $CONDA_DIR/bin/conda install -c conda-forge \
      numpy \
      ipyleaflet \
      ipympl \
      brewer2mpl \
      dask \
      folium \
      altair \
      vega_datasets \
      pydotplus \
      graphviz \
      python-graphviz \
      networkx \
      bqplot
RUN $CONDA_DIR/bin/conda install -c bokeh jupyter_bokeh bokeh && \
    $CONDA_DIR/bin/conda install -c pyviz holoviz
RUN pip install japanize_matplotlib optuna
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends git nodejs build-essential \
    emacs \
    git \
    inkscape \
    jed \
    libsm6 \
    libxext-dev \
    libxrender1 \
    lmodern \
    netcat \
    python-dev \
    # ---- nbconvert dependencies ----
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-generic-recommended \
    texlive-fonts-extra \
    tzdata \
    unzip \
    wget \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    fonts-liberation

RUN $CONDA_DIR/bin/conda install -c plotly plotly plotly-geo chart-studio plotly-orca psutil
# RUN $CONDA_DIR/bin/conda install tini
# RUN pip install jupyter_contrib_nbextensions && \
# RUN $CONDA_DIR/bin/conda install -c conda-forge jupyter_contrib_nbextensions && \
    # jupyter contrib nbextension install --user && \
    # jupyter nbextension enable codefolding/main && \
    # jupyter contrib nbextensions migrate
# RUN $CONDA_DIR/bin/conda install -c conda-forge jupyterlab
# RUN $CONDA_DIR/bin/conda install -c conda-forge jupyterlab==1.2
# RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix
# RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build && \
#     jupyter lab build --dev-build=True --minimize=True
# RUN jupyter labextension install bqplot  && \
#     jupyter labextension install @bokeh/jupyter_bokeh
# RUN jupyter labextension install @jupyterlab/vega5-extension && \
#     # jupyter labextension install @pyviz/jupyterlab_pyviz && \
#     jupyter labextension install jupyter-leaflet && \
#     jupyter labextension install jupyter-matplotlib && \
#     jupyter labextension install @jupyterlab/fasta-extension
# RUN jupyter labextension install @jupyterlab/geojson-extension && \
#     jupyter labextension install @jupyterlab/katex-extension && \
#     jupyter labextension install @jupyterlab/mathjax3-extension && \
#     jupyter labextension install @jupyterlab/vega2-extension && \
#     jupyter labextension install @jupyterlab/vega3-extension && \
#         # jupyter labextension install jupyterlab-plotly@1.5.4 && \
#     # jupyter labextension install plotlywidget@1.5.4 && \
#     # Contents Table https://github.com/jupyterlab/jupyterlab-toc
#     jupyter labextension install @jupyterlab/toc

# RUN jupyter labextension install plotlywidget@1.5.4 && \
    # jupyter labextension install jupyterlab-plotly@1.5.4
# RUN jupyter labextension install bqplot --no-build  && \
#     jupyter labextension install @bokeh/jupyter_bokeh --no-build && \
#     jupyter labextension install @jupyterlab/vega5-extension --no-build && \
#     # jupyter labextension install @pyviz/jupyterlab_pyviz --no-build && \
#     jupyter labextension install jupyter-leaflet --no-build && \
#     jupyter labextension install jupyter-matplotlib --no-build && \
#     jupyter labextension install @jupyterlab/fasta-extension && \
#     jupyter labextension install @jupyterlab/geojson-extension && \
#     jupyter labextension install @jupyterlab/katex-extension && \
#     jupyter labextension install @jupyterlab/mathjax3-extension && \
#     jupyter labextension install @jupyterlab/vega2-extension && \
#     jupyter labextension install @jupyterlab/vega3-extension && \
#     jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.1 --no-build && \
#     jupyter labextension install plotlywidget@1.5.4 --no-build && \
#     jupyter labextension install jupyterlab-plotly@1.5.4 --no-build && \
#     # jupyter labextension install jupyterlab-plotly@1.5.4 --no-build && \
#     # jupyter labextension install plotlywidget@1.5.4 --no-build && \
#     # Contents Table https://github.com/jupyterlab/jupyterlab-toc
#     jupyter labextension install @jupyterlab/toc --no-build && \
#     # Template Reader https://github.com/jpinzonc/jupyterlab_templates
#     # jupyter labextension install jupyterlab_templates --no-build && \
#     # jupyter serverextension enable --py jupyterlab_templates && \
#     jupyter lab build && \
#     jupyter lab clean && \
#     npm cache clean --force && \
#     rm -rf $HOME/.node-gyp && \
#     rm -rf $HOME/.local && \
#     find /opt/conda/ -follow -type f -name '*.a' -delete
#     # find /opt/conda/ -follow -type f -name '*.js.map' -delete
EXPOSE 8888
# ENTRYPOINT [ "/usr/bin/tini", "--" ]
