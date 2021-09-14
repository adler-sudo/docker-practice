FROM continuumio/miniconda3

WORKDIR /home/james/docker-practice

# Create the environment:
COPY . .
RUN conda env create -f environment.yml -n myenv

# Make RUN commands use the new environment:
RUN echo "conda activate myenv" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# The code to run when container is started:
ENTRYPOINT ["./entrypoint.sh"]