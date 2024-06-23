from fastapi.testclient import TestClient
from agentfile.message_queues.simple import SimpleMessageQueue
from agentfile.message_consumers.remote import (
    RemoteMessageConsumerDef,
)


def test_register_consumer() -> None:
    # arrange
    mq = SimpleMessageQueue()
    remote_consumer_def = RemoteMessageConsumerDef(
        message_type="mock_type", url="https://mock-url.io"
    )
    test_client = TestClient(mq._app)

    # act
    response = test_client.post(
        "/register_consumer", json=remote_consumer_def.model_dump()
    )

    # assert
    assert response.status_code == 200
    assert response.json() == {"consumer": remote_consumer_def.id_}
