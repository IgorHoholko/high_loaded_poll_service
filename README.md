# High Loaded Poll Service

docker exec -it high_load_distributor_1 bash


curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"xyz","password":"xyz", "vote":"1"}' \
  http://localhost:5000/pool