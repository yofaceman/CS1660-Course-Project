# CS1660-Course-Project
 
# How to run application on client side
To preface, this program is not able to communicate with GCP to dynamically create inverted indices given different files. This application is running off a pre-made inverted index based off the files in shakespeare.tar.gz 
1. To build the project, In terminal type "docker build -t mattarndt/project2 ."
2. To run the project, in terminal type "docker run -i mattarndt/project2"
3. When entering files the only acceptable files are {shakespeare.tar.gz, Hugo.tar.gz, Tolstoy.tar.gz}
4. When selecting a top-N value the value must be an integer

# How to run inverted index algorithm
1. Upload InvertedIndex.java to staging bucket
2. Open SSH with Master Cluster
3. input "gsutil cp -r gs://dataproc-staging-us-east1-1006853791664-q5dte3pd/Shakespeare ./Project2/ "
4. gsutil cp -r gs://dataproc-staging-us-east1-1006853791664-q5dte3pd/InvertedIndex.java ./Project2/ 
5. hadoop fs -put ./Project2/Shakespeare /ShakespeareInput
6. cd Project2
7. javac InvertedIndex*.java -cp $(hadoop classpath)
8. jar cf invert.jar InvertedIndex*.class
9. hadoop jar invert.jar InvertedIndex /ShakespeareInput /ShakespeareOutput
10. hadoop fs -getmerge /ShakespeareOutput ShakeOut
11. gsutil cp ShakeOut gs://dataproc-staging-us-east1-1006853791664-q5dte3pd/
12. Now the file ShakeOut which contains the inverted index should be in your GCP bucket 
13. Download ShakeOut to your local machine and store it where you build your dockerfile


# Problems with Application
This application has no way to send data between the GCP VM, which runs the MapReduce algorithm that produces the inverted index, and the Docker container which sends to GCP which files it would like count and index.Due to this I have to manually add files to the GCP Bucket, open an SSH, compile and run the Inverted Index MapReduce algorithm on the input files uploaded to GCP. Then download the output file to my local machine to be used and interpreted by the client application.


# Assumptions Made
-Users can only upload from the following files{shakespeare.tar.gz, Hugo.tar.gz, Tolstoy.tar.gz}
-Users do not make mistakes when entering information into terminal
-User is able to run docker containers on their computer