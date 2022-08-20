#!/bin/bash

# poetry_download_model.sh

# Full path of the file
DEST="resources/lib/en_core_web_sm-3.3.0.tar.gz"

if [ -f ${DEST} ]; then
    echo "Model $DEST has already been downloaded."
else
     SOURCE="https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.3.0/en_core_web_sm-3.3.0.tar.gz"
     mkdir -p resources/libs
    cd resources/libs
    curl --location $SOURCE --remote-name --output $DEST
    cd ../..
    echo "Model $DEST has been downloaded."
fi
