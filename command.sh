 docker run -d \
	--name some-postgres \
	-e POSTGRES_PASSWORD=password \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v /home/data:/var/lib/postgresql/data \
	-p 5432:5432 \
	postgres

