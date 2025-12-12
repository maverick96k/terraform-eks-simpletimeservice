FROM python:3.12-slim

ARG APP_USER=appuser
ARG APP_UID=1000
ARG APP_GID=1000

RUN groupadd --gid ${APP_GID} ${APP_USER} \
 && useradd --uid ${APP_UID} --gid ${APP_GID} --no-create-home --shell /usr/sbin/nologin ${APP_USER} \
 && mkdir -p /app

WORKDIR /app

COPY app.py /app/app.py
COPY .dockerignore /app/.dockerignore

RUN chown -R ${APP_UID}:${APP_GID} /app \
 && chmod 755 /app/app.py

USER ${APP_UID}:${APP_GID}

ENV PORT=8080
EXPOSE 8080

CMD ["python", "/app/app.py"]
