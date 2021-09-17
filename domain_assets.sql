create table domain_assets
(
    id_name          uuid         default uuid_generate_v1()      not null
        constraint test_table_pk
            primary key,
    domain_name      varchar(100) default NULL::character varying not null,
    doamin_ip        varchar(100) default NULL::character varying,
    date_saved       date,
    last_day_changed date
);

alter table domain_assets
    owner to craig;

create unique index domain_assets1_domain_name_uindex
    on domain_assets (domain_name);