FROM python:2.7

MAINTAINER Fredy Ramos (fredy.rx@gmail.com)

RUN mkdir -p /opt/src/app

COPY app /opt/src/app

# no funciona, setear durante creacion de contaner(run -v)
#VOLUME ["/Users/fredy/projects/movilidad-escolar/app:/opt/src/app"]

WORKDIR /opt/src/app/

RUN pip install -r requirements.txt

ENV IP "0.0.0.0"
ENV PORT 5000

EXPOSE 5000

# Se ejecuta al inicio del container(run)
ENTRYPOINT ["python"]

CMD ["app.py"]