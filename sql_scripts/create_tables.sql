CREATE TABLE IF NOT EXISTS machine_links(
    ccn VARCHAR(50) NOT NULL,
    state_or_region varchar(50) NOT NULL, 
    reporting_entity_name_common varchar(200) NOT NULL,
    machine_readable_url varchar(5000),
    csv_headers text[],
    meets_standard BOOLEAN,
    PRIMARY KEY (ccn)
);

CREATE TABLE IF NOT EXISTS features(
    bed_count INT NOT NULL,
    zip_code varchar(10),
    medicare_medicaid_eligible BOOLEAN NOT NULL,
    ccn VARCHAR(50) NOT NULL,
    CONSTRAINT fk_ccn
        FOREIGN KEY(ccn)
            REFERENCES machine_links(ccn)
);