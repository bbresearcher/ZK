## Picus
[https://github.com/Veridise/Picus](https://github.com/Veridise/Picus)

Picus is used to run verification tasks on r1cs files.

## Follow the instructions on the github link above to clone the repo, build the docker file and run the docker container.

## Copy files into the container
1. To run the docker container ```docker run -it --rm picus:v0 bash```
2. Once the docker container is running you will be presented with a commandline prompt in the docker container.
3. On the host pc get the docker container id: ```sudo docker container ls```
4. Inside the Docker contianer create a directory in the container for your test files eg. ```mkdir tester``` and then ```mkdir r1cs```
5. From your host pc copy the r1cs files into the docker container ```sudo docker cp myr1csfile.r1cs CONTAINERID:/Picus/tester/r1cs/myr1csfile.r1cs```
6. in the docker container you can now run any of the verification ```.rkt``` scripts against your r1cs file to verify it. eg. ```racket ./test-v1-uniqueness.rkt --r1cs ./tester/r1cs/myr1csfile.r1cs```
