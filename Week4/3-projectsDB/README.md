# Projects DB Exercises

## Setup

1. Enter psql shell:

        $ psql

2. Create `projects_db` database:

        =# CREATE DATABASE projects_db;

3. Exit psql shell

4. Clone Repository:

        $ git clone https://github.com/egarcia410/digitalCraft.git

5. Change Directory:

        $ cd /digitalCraft/Week4/3-projectsDB

6. In terminal, restore databse:

        $ psql projects_db -f projects.sql

7. Run Queries:

        $ psql projects_db -f projects_db.sql

## Problems

Write queries to find the answers below:

1. What are all projects that use JavaScript?
2. What are all technologies used by the Personal Website?
3. Perform a left outer join from the tech table to the project_uses_tech table - which techs has no associated project?
4. Based on the previous query, get the count of the number of techs used by each project.
5. Perform a left outer join from the project table to the project_users_tech table - which projects has no associated tech?
6. Based on the previous query, get the count of the number of projects that use each tech.
7. List all projects along with each technology used by it. You will need to do a three-way join.
8. List all the distinct techs that are used by at least one project.
9. List all the distinct techs that are not used by any projects.
10. List all the distinct projects that use at least one tech.
11. List all the distinct projects that use no tech.
12. Order the projects by how many tech it uses.
13. Order the tech by how many projects use it.
14. What is the average number of techs used by a project?