echo "Configuring GP repository"

echo "Triplestore located at $TRIPLESTORE_HOST"

curl -X POST --header 'Content-Type: multipart/form-data' --header 'Accept: */*' \
-F "config=@gp_triplestore_config.ttl" \
"http://$TRIPLESTORE_HOST:7200/rest/repositories"

res=$?

if [ "$res" != "0" ]; then
  echo "Could not create repository ($res)"
  exit $res
fi

echo "Configuration done."



echo "Importing data"
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ "data": "https://www.wikidata.org/wiki/Special:EntityData/Q2934.ttl" }' "http://$TRIPLESTORE_HOST:7200/rest/data/import/upload/$REPOSITORY/url"

res=$?
if [ "$res" != "0" ]; then
  echo "Could not import data ($res)"
  exit $res
fi

echo "Done"
