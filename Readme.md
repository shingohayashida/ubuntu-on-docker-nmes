# ubuntu-on-docker-nmes

## Step 1. Install Docker
### Windows/Mac
 * [Download Docker Desktop](https://www.docker.com/)
 * Open `Windows PowerShell`(**Windows**) or `Terminal`(**Mac**) and try to check with [hello-world](https://hub.docker.com/_/hello-world).
   * `$ docker pull hello-world`
   * `$ docker run hello-world`
   * `$ docker rm -f {CONTAINER ID}`

## Step2. Download and edit docker setting files.
 * Download this repository.
   * `$ git clone https://github.com/shingohayashida/ubuntu-on-docker-nmes.git`
 * Open `Windows PowerShell`(**Windows**) or `Terminal`(**Mac**) and move to `ubuntu` in the downloaded file.
 * Edit `docker-compose.yml` to suit you. At least, the following four lines must be set by your hands.
   * `USERNAME`
   * `PASSWORD`
   * `TIMEZONE`
   * `volumes`:
     * Setting for sharing the directory in the docker container to your Windows or Mac.
     * This directory will not be deleted at closing the docker container. I highly recommend you to work inside the directory you set here.
     * '(A path on Windows or Mac):(A path on Ubuntu in the docker container)' 
   * (Optional) If you want to install **PyTorch** and **PyTorch Lightninig**, please put `Dockerfile_ubuntu22.04_PyTorch_cpu` on `dockerfile`.

## Step3. Build and run a docker container
 * Build a docker image
   * `$ docker compose up -d`
 * Make sure the docker container running healthy.
   * `$ docker ps -a`
 * Start a bash shell on Ubuntu. You can exit Ubuntu by `exit`.
   * `$ docker exec -it ubuntu-vm-1 /bin/bash`
 * Copy a check script to the docker container.
   * `$ docker cp ../ml_examples/quick_check.py ubuntu-vm-1:/home/your_username/`
 * Make sure you get **"All liberaries are available!"**.
   * `$ python3 quick_ckeck.py`

## Step4. Stop a docker image
 * Stop the docker container.
   * `$ docker compose down`
   * **Warning** All settings and files outside the shared directries (you set at `volumes` in `docker-compose.yml`) will be reset at stopping. 

## (Optional) Step5. Virtual Studio Code (VSCode)
  * **VSCode** is a source code editor with many useful extensions.
    * [Download VSCode](https://code.visualstudio.com/)
    * Essential extensions
      * **Dev Containers**
      * **Python**: **Note** You need to install this in Container.
      * **Jupyter**: **Note** You need to install this in Container.
   * Try to run a check notebook on your VSCode.
     * `$ code example-k-means.ipynb`
