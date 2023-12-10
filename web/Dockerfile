# Use an official Node.js runtime as a base image
FROM node:alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock) files
COPY package*.json ./
# If you use yarn, uncomment the following line and remove the above line
# COPY package.json yarn.lock ./

# Install dependencies
RUN npm install
# If you use yarn, use the following command instead
# RUN yarn install

# Bundle the app source inside the Docker image
COPY . .

# Map the port to the Docker daemon
EXPOSE 3000

# Define the command to run the app using npm or yarn
CMD ["npm", "run", "dev"]
# If you use yarn, use the following command instead
# CMD ["yarn", "dev"]
