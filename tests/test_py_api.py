class TestStudents:
    def test_get_students(self, client):
        response = client.get('http://127.0.0.1:5000/api/v1/students')
        assert response.status_code == 200

    def test_get_student(self, client):
        response = client.get('http://127.0.0.1:5000/api/v1/students/123')
        assert response.status_code == 200
        assert response.json == {'first_name': 'Robert', 'group_id': 8, 'id': 123, 'last_name': 'White'}

    def test_post_students(self, client):
        data = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = client.post('http://127.0.0.1:5000/api/v1/students', json=data)
        assert response.status_code == 201

    def test_put_student(self, client):
        # Define updated data for the student
        updated_student = {'first_name': 'Jane', 'last_name': 'Doe', 'group_id': 2, 'id':2}

        # Make a PUT request to update the student's data
        response = client.put(f'http://127.0.0.1:5000/api/v1/students/2', json=updated_student)

        # Assert that the response status code is 200 OK
        assert response.status_code == 200

        # Assert that the response JSON data matches the updated data
        assert response.json == updated_student

    def test_delete_student(self, client):
        # Make a DELETE request to delete the student with ID 2
        response = client.delete('http://127.0.0.1:5000/api/v1/students/2')

        # Assert that the response status code is 204 NO CONTENT, indicating success
        assert response.status_code == 204

        # Attempt to get the student by ID, expecting a 404 NOT FOUND response
        response = client.get('http://127.0.0.1:5000/api/v1/students/2')
        assert response.status_code == 404

class TestGroups:
    def test_get_groups(self, client):
        response = client.get('http://127.0.0.1:5000/api/v1/groups')
        assert response.status_code == 200

    def test_get_group(self, client):
        response = client.get('http://127.0.0.1:5000/api/v1/groups/1')
        assert response.status_code == 200
        assert response.json == {'name': 'XU-36', 'id': 1}

    def test_post_groups(self, client):
        data = {
            'name': 'Group C',

        }
        response = client.post('http://127.0.0.1:5000/api/v1/groups', json=data)
        assert response.status_code == 201

    def test_put_group(self, client):
        # Define updated data for the group
        updated_group = {'name': 'Group B', 'id': 2}

        # Make a PUT request to update the group's data
        response = client.put(f'http://127.0.0.1:5000/api/v1/groups/2', json=updated_group)

        # Assert that the response status code is 200 OK
        assert response.status_code == 200

        # Assert that the response JSON data matches the updated data
        assert response.json == updated_group

    def test_delete_group(self, client):
        # Delete the group and assert that the response status code is 200 OK
        response = client.delete(f'http://127.0.0.1:5000/api/v1/groups/2')
        assert response.status_code == 200

        # Try to retrieve the group from the database and assert that it doesn't exist
        response = client.get('http://127.0.0.1:5000/api/v1/groups/2')
        assert response.status_code == 404


class TestCourses:
    def test_get_courses(self, client):
        response = client.get('http://127.0.0.1:5000/api/v1/courses')
        assert response.status_code == 200

    def test_get_course(self, client):
        response = client.get('http://127.0.0.1:5000/api/v1/courses/1')
        assert response.status_code == 200
        assert response.json == {'description': 'Description for Math', 'id': 1, 'name': 'Math'}

    def test_post_courses(self, client):
        data = {
            'name': 'Course C',
            'description': 'foqahfdhaugfa'
        }
        response = client.post('http://127.0.0.1:5000/api/v1/courses', json=data)
        assert response.status_code == 201

    def test_put_course(self, client):
        # Define updated data for the course
        updated_course = {'description': 'Description for Biology', 'id': 2, 'name': 'Course B'}

        # Make a PUT request to update the course's data
        response = client.put(f'http://127.0.0.1:5000/api/v1/courses/2', json=updated_course)

        # Assert that the response status code is 200 OK
        assert response.status_code == 200

        # Assert that the response JSON data matches the updated data
        assert response.json == updated_course

    def test_delete_courses(self, client):
        # Delete the group and assert that the response status code is 200 OK
        response = client.delete(f'http://127.0.0.1:5000/api/v1/courses/2')
        assert response.status_code == 204

        # Try to retrieve the group from the database and assert that it doesn't exist
        response = client.get('http://127.0.0.1:5000/api/v1/courses/2')
        assert response.status_code == 404
