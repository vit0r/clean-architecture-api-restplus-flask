#!/usr/bin/env sh
FLASK_DB="flask db"
test ! -d "./migrations" && ${FLASK_DB} init || echo "migrations exists"
sudo docker-compose up
${FLASK_DB} migrate
${FLASK_DB} upgrade
exit 0