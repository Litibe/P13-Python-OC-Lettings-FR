build:
  docker:
    web: Dockerfile
run:
  web: gunicorn oc_lettings_site.wsgi:application --port 8000 --host 0.0.0.0 