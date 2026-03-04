# Docker Notes — Day 9

## Docker Version
Docker version 29.2.1, build a5c7197

## Hello World Test
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
17eec7bbc9d7: Pull complete
ea52d2000f90: Download complete
Digest: sha256:ef54e839ef541993b4e87f25e752f7cf4238fa55f017957c2eb44077083d7a6a
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/


## Postgres Container
docker run -d \
  --name pg-prework \
  -e POSTGRES_PASSWORD=prework \
  -p 5432:5432 \
  postgres:15-alpine
20ec7031ec03e2a9b54084988380bce06f33d8df9b385e0aa0c1ad4c93bd4547

## Startup Logs
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default time zone ... UTC
creating configuration files ... ok
running bootstrap script ... ok
sh: locale: not found
2026-03-04 08:02:06.987 UTC [36] WARNING:  no usable system locales were found
performing post-bootstrap initialization ... ok
syncing data to disk ... ok


Success. You can now start the database server using:

    pg_ctl -D /var/lib/postgresql/data -l logfile start

initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
waiting for server to start....2026-03-04 08:02:07.471 UTC [42] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-03-04 08:02:07.472 UTC [42] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-03-04 08:02:07.476 UTC [45] LOG:  database system was shut down at 2026-03-04 08:02:07 UTC
2026-03-04 08:02:07.480 UTC [42] LOG:  database system is ready to accept connections
 done
server started

/usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*

waiting for server to shut down....2026-03-04 08:02:07.570 UTC [42] LOG:  received fast shutdown request
2026-03-04 08:02:07.573 UTC [42] LOG:  aborting any active transactions
2026-03-04 08:02:07.574 UTC [42] LOG:  background worker "logical replication launcher" (PID 48) exited with exit code 1
2026-03-04 08:02:07.574 UTC [43] LOG:  shutting down
2026-03-04 08:02:07.577 UTC [43] LOG:  checkpoint starting: shutdown immediate
2026-03-04 08:02:07.585 UTC [43] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.003 s, sync=0.002 s, total=0.011 s; sync files=2, longest=0.001 s, average=0.001 s; distance=0 kB, estimate=0 kB
2026-03-04 08:02:07.587 UTC [42] LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

2026-03-04 08:02:07.693 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-03-04 08:02:07.693 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-03-04 08:02:07.693 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-03-04 08:02:07.698 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-03-04 08:02:07.701 UTC [56] LOG:  database system was shut down at 2026-03-04 08:02:07 UTC
2026-03-04 08:02:07.705 UTC [1] LOG:  database system is ready to accept connections

## Stop and Restart

### docker stop pg-prework
pg-prework
### docker restart pg-prework
pg-prework
## docker logs pg-prework (after restart)
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default time zone ... UTC
creating configuration files ... ok
running bootstrap script ... ok
sh: locale: not found
2026-03-04 08:02:06.987 UTC [36] WARNING:  no usable system locales were found
performing post-bootstrap initialization ... ok
syncing data to disk ... ok


Success. You can now start the database server using:

    pg_ctl -D /var/lib/postgresql/data -l logfile start

initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
waiting for server to start....2026-03-04 08:02:07.471 UTC [42] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-03-04 08:02:07.472 UTC [42] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-03-04 08:02:07.476 UTC [45] LOG:  database system was shut down at 2026-03-04 08:02:07 UTC
2026-03-04 08:02:07.480 UTC [42] LOG:  database system is ready to accept connections
 done
server started

/usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*

waiting for server to shut down....2026-03-04 08:02:07.570 UTC [42] LOG:  received fast shutdown request
2026-03-04 08:02:07.573 UTC [42] LOG:  aborting any active transactions
2026-03-04 08:02:07.574 UTC [42] LOG:  background worker "logical replication launcher" (PID 48) exited with exit code 1
2026-03-04 08:02:07.574 UTC [43] LOG:  shutting down
2026-03-04 08:02:07.577 UTC [43] LOG:  checkpoint starting: shutdown immediate
2026-03-04 08:02:07.585 UTC [43] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.003 s, sync=0.002 s, total=0.011 s; sync files=2, longest=0.001 s, average=0.001 s; distance=0 kB, estimate=0 kB
2026-03-04 08:02:07.587 UTC [42] LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

2026-03-04 08:02:07.693 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-03-04 08:02:07.693 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-03-04 08:02:07.693 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-03-04 08:02:07.698 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-03-04 08:02:07.701 UTC [56] LOG:  database system was shut down at 2026-03-04 08:02:07 UTC
2026-03-04 08:02:07.705 UTC [1] LOG:  database system is ready to accept connections
2026-03-04 08:07:07.817 UTC [54] LOG:  checkpoint starting: time
2026-03-04 08:07:11.848 UTC [54] LOG:  checkpoint complete: wrote 43 buffers (0.3%); 0 WAL file(s) added, 0 removed, 0 recycled; write=4.015 s, sync=0.008 s, total=4.031 s; sync files=11, longest=0.004 s, average=0.001 s; distance=252 kB, estimate=252 kB
2026-03-04 08:13:56.486 UTC [1] LOG:  received fast shutdown request
2026-03-04 08:13:56.488 UTC [1] LOG:  aborting any active transactions
2026-03-04 08:13:56.490 UTC [1] LOG:  background worker "logical replication launcher" (PID 59) exited with exit code 1
2026-03-04 08:13:56.491 UTC [54] LOG:  shutting down
2026-03-04 08:13:56.493 UTC [54] LOG:  checkpoint starting: shutdown immediate
2026-03-04 08:13:56.498 UTC [54] LOG:  checkpoint complete: wrote 0 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.002 s, sync=0.001 s, total=0.008 s; sync files=0, longest=0.000 s, average=0.000 s; distance=0 kB, estimate=227 kB
2026-03-04 08:13:56.502 UTC [1] LOG:  database system is shut down

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-03-04 08:14:20.326 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-03-04 08:14:20.326 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-03-04 08:14:20.326 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-03-04 08:14:20.330 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-03-04 08:14:20.334 UTC [29] LOG:  database system was shut down at 2026-03-04 08:13:56 UTC
2026-03-04 08:14:20.339 UTC [1] LOG:  database system is ready to accept connections