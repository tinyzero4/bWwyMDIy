FROM continuumio/miniconda3

RUN mkdir -p /opt/prediction-service
WORKDIR /opt/prediction-service

COPY common.py .
COPY predict.py .
COPY vectorizer.out .
COPY model.out .
COPY conda-environment.yml .

RUN conda env create -f conda-environment.yml

EXPOSE 8080
CMD ["conda", "run", "-n", "ml", "gunicorn", "--bind=0.0.0.0:8080", "predict:app"]