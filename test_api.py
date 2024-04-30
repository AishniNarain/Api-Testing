import requests
import uuid

ENDPOINT = 'https://todo.pixegami.io/'

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    
    return {
        "content": content,
        "user_id": user_id,
        "is_done": False
    }
    
def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")
    
#test cases
def test_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    # assert create_task_response.status_code == 200
    
    data = create_task_response.json()
    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)
    # assert get_task_response.status_code == 200
    
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]
    
def test_update_task():
    #create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()["task"]["task_id"]
    # assert create_task_response.status_code == 200
    
    #update the task
    new_payload = {
        "content": "test updated content",
        "user_id": payload["user_id"],
        "task_id": task_id,
        "is_done": True
    }
    update_task_response = update_task(new_payload)
    # assert update_task_response.status_code == 200
    
    #get and validate the changes
    get_task_response = get_task(task_id)
    get_task_data = get_task_response.json()
    print(get_task_data)
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["user_id"] == new_payload["user_id"]
    
def test_list_tasks():
    #create n tasks
    payload = new_task_payload()
    user_id = payload["user_id"]
    
    n = 3
    for _ in range(n):
        create_task_response = create_task(payload)
        # assert create_task_response.status_code == 200
        
    #List tasks and check that there are n items
    list_task_response = list_tasks(user_id)
    assert list_task_response.status_code == 200
    
    list_task_data = list_task_response.json()
    tasks = list_task_data["tasks"]
    
    assert len(tasks) == n
    
def test_delete_tasks():
    #create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()["task"]["task_id"]
    
    #delete the task
    delete_task_response = delete_task(task_id)
    # assert delete_task_response.status_code == 200
    
    #get the task and check that it's not found
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404