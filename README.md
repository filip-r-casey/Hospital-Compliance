# Hospital-Compliance

This repository exists as a complement to our final paper Clustering Analysis of US Hospital Data Availability Compliance.

## Files

* `cleaning_scripts` contains the scripts we used to clean the csv data and import it to postgres
* `data` contains the source files from: [Hospital Transparency](https://github.com/TPAFS/transparency-data)\
* `sql_scripts` simply contains the code we used to initialize the tables, **NOT** to initialize the entire data base
* `analysis.ipynb` contains the code for web scraping headers from the machine-readable files
* `EM.ipynb` contains the GMM code to actually process the data and produce plots
* `init.sql` is the initialization file for the database with data included (used by `docker compose`)
  
## Running Code

To do analysis on this data simply run `docker compose up` to initialize the database. This will load it with all the data from `init.sql` and map the container port to localhost:5432 on your local machine.

From there `analysis.ipynb` contains a tutorial for usign psycopg2 to collect data from the instance.

## Contact

For any questions email filip.r.casey@gmail.com
