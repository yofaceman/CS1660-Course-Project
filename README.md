# CS1660-Course-Project
 
# How to run application on client side
1. To build the project, In terminal type "docker build -t mattarndt/project2 ."
2. To run the project, in terminal type "docker run -i mattarndt/project2"
3. You will then be presented with a simple terminal based program

# Step to be used to connect to GCP
In my main application I would create a secure connection with GCP using the JSON file with authentication keys. I would send each files 
contents over to be used analyzed and indexed by the second application. However I have yet to make that secure connection in my code.
I am also unsure if we are to deploy our Docker container on GCP or if it will be deployed on the clientside. If it is to be deployed on 
then changes will have to be made to the Dockerfile RUN command to work on a linux system and I will need to figure out how to make 
the cloudbuild.yaml file interactive when building it in the GCP console. 


# Assumptions Made
An assumption is made that the user can only choose from the files from the sample directory labeled "Data".
Additionally, all files in the Data directory would be in the format .tar.gz