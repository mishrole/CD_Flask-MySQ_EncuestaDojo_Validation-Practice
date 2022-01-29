Create database dojo_survey_schema;
Use dojo_survey_schema;

Create table dojos (
	id int primary key auto_increment,
    name varchar(45),
    created_at datetime,
    updated_at datetime
);

Create table languages (
	id int primary key auto_increment,
    name varchar(45),
	created_at datetime,
    updated_at datetime
);

Create table surveys (
	id int primary key auto_increment,
    name varchar(100),
    dojo_id int not null,
    language_id int not null,
    comment varchar(200),
    created_at datetime,
    updated_at datetime,
    foreign key (dojo_id) references dojos(id),
    foreign key (language_id) references languages(id)
);

Insert into dojos(name, created_at, updated_at) values 
('Chicago', NOW(), NOW()),
('Seattle', NOW(), NOW()),
('Online', NOW(), NOW()),
('Burbank', NOW(), NOW()),
('Bellevue', NOW(), NOW());

Insert into languages(name, created_at, updated_at) values 
('HTML', NOW(), NOW()),
('CSS', NOW(), NOW()),
('JavaScript', NOW(), NOW()),
('Python', NOW(), NOW()),
('C#', NOW(), NOW());