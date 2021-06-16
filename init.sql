create table if not exists Lorries (
       id text primary key,
       location text
);

create table if not exists Containers (
       id text primary key,
       location text,
       loaded integer,
       destination text
);

create table if not exists Nodes (
       name text primary key,
       location text,
       capacity integer,
       costPerUnit real,
       type text
);

create table if not exists TrafficNetwork (
       node1 text,
       node2 text,
       cost real,
       primary key (node1, node2)
);

create table if not exists Schedule (
       lorryId text primary key,
       containerId text,
       nodeName text
);

insert into Lorries values ('ABC 123', 'Coventry');
insert into Lorries values ('ABC 456', 'Coventry');
insert into Lorries values ('ABC 789', 'Liverpool');
insert into Lorries values ('ABC 321', 'Coventry');

insert into Containers values ('1', 'Coventry', 1, 'Westminster');
insert into Containers values ('2', 'Liverpool', 1, 'Watford');
insert into Containers values ('3', 'Liverpool', 1, 'City of London');
insert into Containers values ('4', 'Watford', 0, 'Liverpool');
insert into Containers values ('5', 'Watford', 0, 'Liverpool');

select * from Containers;
