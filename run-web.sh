cd web
docker run -p 3000:3000 -v $(pwd):/app --name resolve-rubiks-dev-container resolve-rubiks-dev-image

