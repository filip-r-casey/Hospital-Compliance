CREATE TABLE IF NOT EXISTS machine_links(
    ccn INT NOT NULL,
    state_or_region varchar(50) NOT NULL, 
    name varchar(200) NOT NULL,
    machine_readable_url varchar(500),
    PRIMARY KEY (ccn)
);

CREATE TABLE IF NOT EXISTS features(
    bed_count INT NOT NULL,
    zipcode varchar(10),
    medicare BOOLEAN NOT NULL,
    ccn INT NOT NULL,
    CONSTRAINT fk_ccn
        FOREIGN KEY(ccn)
            REFERENCES machine_links(ccn)
);