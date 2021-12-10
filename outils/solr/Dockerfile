#FROM solr:8.2
FROM solr:8.5

USER root
RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-fra python pip
RUN apt-get install -y imagemagick

#https://cwiki.apache.org/confluence/display/tika/tikaocr
RUN pip3 install numpy scikit-image

# Clean up
RUN apt-get autoremove
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#COPY security.json /var/solr/data/security.json
COPY publication_config /opt/solr/server/solr/configsets/publication_config

RUN chown -R solr:solr /opt/solr/server/solr/configsets/publication_config
USER solr

ENV TESSDATA_PREFIX="/usr/share/tesseract-ocr/4.00/tessdata/"
