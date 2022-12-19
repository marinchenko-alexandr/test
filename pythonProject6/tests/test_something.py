import requests

from configuration import SERVICE_URL

from src.enums.global_enums import GlobalErrorMessages


def test_getting_post():
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()
    received_posts = [{'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}, {'id': 1, 'title': 'Post 1'}]
    print(received_posts)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_code.value
    assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
    assert received_posts.id[2]["title"] == 'Post 2'
    assert received_posts[2]["id"] == 1

