build:
  docker:
    web: Dockerfile
run:
  web: gunicorn oc_lettings_site.wsgi:application --host=0.0.0.0 --port=${PORT}