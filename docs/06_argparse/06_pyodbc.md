##### Deploying MySQL via Docker

1. Install dependencies

```bash
sudo apt install unixodbc unixodbc-dev odbc-mariadb
```

2. Verify the driver installation
```bash
odbcinst -q -d | grep MariaDB
```

3. Run a container:
```bash
docker run --name fridge \
  -e MYSQL_ROOT_PASSWORD=$PASSWORD \
  -e MYSQL_DATABASE=fridge \
  -p 3306:3306 \
  -d mysql:latest
```

- `--name fridge` names the container `fridge`. This name will be used in subsequent commands
- `-e MYSQL_ROOT_PASSWORD=$PASSWORD` sets the root password for the MySQL container.
- `-e MYSQL_DATABASE=fridge` creates a database named `fridge` on startup.
- `-p 3306:3306` exposes port 3306 from the container to port 3306 on the host.
- `-d` runs the container in detached mode (does not output logs).
- `mysql:latest` uses the latest MySQL image.

**Note:** this config can be saved as a `compose.yaml` file to achieve Infrastructure as Code.

##### Accessing MySQL CLI

1. Create a network and connect the container to it:

```bash
docker network create fridge-network
docker network connect fridge-network fridge
```

2. Connect to the container via CLI.
```bash
docker run -it --network fridge-network --rm mysql mysql -hfridge -uroot -p
```

You should see a prompt like this:
```
mysql>
```
