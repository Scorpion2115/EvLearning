# Build a Dockerfile
1. Create a `Dockerfile`

2. Build the image
```bash
sudo docker build -t evan21/train-schedule .
```
3. Run the image
```bash
sudo docker run -p 3000:3000 -d evan21/train-schedule
```
4. Push the image to Dockerhub
```bash
docker login --username=evan21
sudo docker push evan21/train-schedule
```
