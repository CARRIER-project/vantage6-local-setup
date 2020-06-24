echo "Add repository to local graphdb instance"
curl -X POST\
    http://localhost:7200/rest/repositories\
    -H 'Content-Type: multipart/form-data'\
    -F "config=@nodes/escience/repo-config.ttl"

echo "Load sample transaction data into repo1"
curl -X POST -H "Content-Type:application/x-turtle" -T "nodes/escience/sample-transaction-data.ttl" \
  http://localhost:7200/repositories/repo1/statements
