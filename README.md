# locust
easy locust test


docker run -d -p 8089:8089 --volume $PWD:/mnt/locust --name=locust -e LOCUSTFILE_PATH=/mnt/locust/locustfile.py -e TARGET_URL=https://www.website-to-test.com locustio/locust
