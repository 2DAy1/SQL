Student Management System with SQLAlchemy and Flask REST Framework

1. SQL and Database Setup:
- Create PostgreSQL user and database with necessary privileges.
- Prepare SQL files for creating tables and assigning privileges.

2. Python Application Development:
- Generate test data, including 10 groups with randomly generated names, 10 courses, and 200 students with randomly combined names.
- Assign students to groups randomly with varying group sizes.
- Establish a many-to-many relationship between students and courses, randomly assigning 1 to 3 courses for each student.

3. ORM Queries and Operations:
- Retrieve all groups with a student count less than or equal to a given value.
- Find all students associated with a course based on the course name.
- Add a new student to the system.
- Delete a student by their STUDENT_ID.
- Add a student to a course from a provided list.
- Remove a student from one of their enrolled courses.

4. Testing:
- Write tests using the Unittest module or py.test to ensure the functionality of the application, including ORM queries and operations.

5. Flask Rest Framework Integration:
- Modify the application to incorporate the Flask REST Framework for handling API requests and responses.

6. Testing of REST API:
- Write additional tests using the Unittest module or py.test to verify the functionality of the REST API endpoints.

Technologies Used:
- SQLAlchemy for database ORM (Object-Relational Mapping).
- Flask and Flask REST Framework for application development and REST API implementation.
- PostgreSQL as the database management system.
- Unittest module or py.test for writing tests.

