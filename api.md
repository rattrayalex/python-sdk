# Agents

Types:

```python
from julep.types import (
    Agent,
    AgentCreateResponse,
    AgentUpdateResponse,
    AgentListResponse,
    AgentDeleteResponse,
    AgentSearchResponse,
)
```

Methods:

- <code title="post /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">create</a>(agent_id, \*\*<a href="src/julep/types/agent_create_params.py">params</a>) -> <a href="./src/julep/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">retrieve</a>(agent_id) -> <a href="./src/julep/types/agent.py">Agent</a></code>
- <code title="put /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/julep/types/agent_update_params.py">params</a>) -> <a href="./src/julep/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /agents">client.agents.<a href="./src/julep/resources/agents/agents.py">list</a>(\*\*<a href="src/julep/types/agent_list_params.py">params</a>) -> <a href="./src/julep/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">delete</a>(agent_id) -> <a href="./src/julep/types/agent_delete_response.py">AgentDeleteResponse</a></code>
- <code title="post /agents/{agent_id}/search">client.agents.<a href="./src/julep/resources/agents/agents.py">search</a>(agent_id, \*\*<a href="src/julep/types/agent_search_params.py">params</a>) -> <a href="./src/julep/types/agent_search_response.py">AgentSearchResponse</a></code>

## Tools

Types:

```python
from julep.types.agents import (
    ToolCreateResponse,
    ToolUpdateResponse,
    ToolListResponse,
    ToolDeleteResponse,
)
```

Methods:

- <code title="post /agents/{agent_id}/tools">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">create</a>(agent_id, \*\*<a href="src/julep/types/agents/tool_create_params.py">params</a>) -> <a href="./src/julep/types/agents/tool_create_response.py">ToolCreateResponse</a></code>
- <code title="put /agents/{agent_id}/tools/{tool_id}">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">update</a>(tool_id, \*, agent_id, \*\*<a href="src/julep/types/agents/tool_update_params.py">params</a>) -> <a href="./src/julep/types/agents/tool_update_response.py">ToolUpdateResponse</a></code>
- <code title="get /agents/{agent_id}/tools">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">list</a>(agent_id, \*\*<a href="src/julep/types/agents/tool_list_params.py">params</a>) -> <a href="./src/julep/types/agents/tool_list_response.py">ToolListResponse</a></code>
- <code title="delete /agents/{agent_id}/tools/{tool_id}">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">delete</a>(tool_id, \*, agent_id) -> <a href="./src/julep/types/agents/tool_delete_response.py">ToolDeleteResponse</a></code>

## Docs

Types:

```python
from julep.types.agents import DocCreateResponse, DocListResponse, DocDeleteResponse
```

Methods:

- <code title="post /agents/{agent_id}/docs">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">create</a>(agent_id, \*\*<a href="src/julep/types/agents/doc_create_params.py">params</a>) -> <a href="./src/julep/types/agents/doc_create_response.py">DocCreateResponse</a></code>
- <code title="get /agents/{agent_id}/docs">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">list</a>(agent_id, \*\*<a href="src/julep/types/agents/doc_list_params.py">params</a>) -> <a href="./src/julep/types/agents/doc_list_response.py">DocListResponse</a></code>
- <code title="delete /agents/{agent_id}/docs/{doc_id}">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">delete</a>(doc_id, \*, agent_id) -> <a href="./src/julep/types/agents/doc_delete_response.py">DocDeleteResponse</a></code>

## Tasks

Types:

```python
from julep.types.agents import TaskCreateResponse, TaskListResponse
```

Methods:

- <code title="post /agents/{agent_id}/tasks">client.agents.tasks.<a href="./src/julep/resources/agents/tasks.py">create</a>(agent_id, \*\*<a href="src/julep/types/agents/task_create_params.py">params</a>) -> <a href="./src/julep/types/agents/task_create_response.py">TaskCreateResponse</a></code>
- <code title="get /agents/{agent_id}/tasks">client.agents.tasks.<a href="./src/julep/resources/agents/tasks.py">list</a>(agent_id, \*\*<a href="src/julep/types/agents/task_list_params.py">params</a>) -> <a href="./src/julep/types/agents/task_list_response.py">TaskListResponse</a></code>

# Sessions

Types:

```python
from julep.types import (
    History,
    Session,
    SessionCreateResponse,
    SessionUpdateResponse,
    SessionListResponse,
    SessionDeleteResponse,
)
```

Methods:

- <code title="post /sessions">client.sessions.<a href="./src/julep/resources/sessions/sessions.py">create</a>(\*\*<a href="src/julep/types/session_create_params.py">params</a>) -> <a href="./src/julep/types/session_create_response.py">SessionCreateResponse</a></code>
- <code title="get /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions/sessions.py">retrieve</a>(session_id) -> <a href="./src/julep/types/session.py">Session</a></code>
- <code title="put /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions/sessions.py">update</a>(session_id, \*\*<a href="src/julep/types/session_update_params.py">params</a>) -> <a href="./src/julep/types/session_update_response.py">SessionUpdateResponse</a></code>
- <code title="get /sessions">client.sessions.<a href="./src/julep/resources/sessions/sessions.py">list</a>(\*\*<a href="src/julep/types/session_list_params.py">params</a>) -> <a href="./src/julep/types/session_list_response.py">SessionListResponse</a></code>
- <code title="delete /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions/sessions.py">delete</a>(session_id) -> <a href="./src/julep/types/session_delete_response.py">SessionDeleteResponse</a></code>
- <code title="get /sessions/{session_id}/history">client.sessions.<a href="./src/julep/resources/sessions/sessions.py">history</a>(session_id) -> <a href="./src/julep/types/history.py">History</a></code>

## Chats

Types:

```python
from julep.types.sessions import ChatCreateResponse
```

Methods:

- <code title="post /sessions/{session_id}/chat">client.sessions.chats.<a href="./src/julep/resources/sessions/chats.py">create</a>(session_id, \*\*<a href="src/julep/types/sessions/chat_create_params.py">params</a>) -> <a href="./src/julep/types/sessions/chat_create_response.py">ChatCreateResponse</a></code>

# Users

Types:

```python
from julep.types import (
    User,
    UserCreateResponse,
    UserUpdateResponse,
    UserListResponse,
    UserDeleteResponse,
    UserSearchResponse,
)
```

Methods:

- <code title="post /users">client.users.<a href="./src/julep/resources/users/users.py">create</a>(\*\*<a href="src/julep/types/user_create_params.py">params</a>) -> <a href="./src/julep/types/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">retrieve</a>(user_id) -> <a href="./src/julep/types/user.py">User</a></code>
- <code title="put /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">update</a>(user_id, \*\*<a href="src/julep/types/user_update_params.py">params</a>) -> <a href="./src/julep/types/user_update_response.py">UserUpdateResponse</a></code>
- <code title="get /users">client.users.<a href="./src/julep/resources/users/users.py">list</a>(\*\*<a href="src/julep/types/user_list_params.py">params</a>) -> <a href="./src/julep/types/user_list_response.py">UserListResponse</a></code>
- <code title="delete /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">delete</a>(user_id) -> <a href="./src/julep/types/user_delete_response.py">UserDeleteResponse</a></code>
- <code title="post /users/{user_id}/search">client.users.<a href="./src/julep/resources/users/users.py">search</a>(user_id, \*\*<a href="src/julep/types/user_search_params.py">params</a>) -> <a href="./src/julep/types/user_search_response.py">UserSearchResponse</a></code>

## Docs

Types:

```python
from julep.types.users import DocCreateResponse, DocListResponse, DocDeleteResponse
```

Methods:

- <code title="post /users/{user_id}/docs">client.users.docs.<a href="./src/julep/resources/users/docs.py">create</a>(user_id, \*\*<a href="src/julep/types/users/doc_create_params.py">params</a>) -> <a href="./src/julep/types/users/doc_create_response.py">DocCreateResponse</a></code>
- <code title="get /users/{user_id}/docs">client.users.docs.<a href="./src/julep/resources/users/docs.py">list</a>(user_id, \*\*<a href="src/julep/types/users/doc_list_params.py">params</a>) -> <a href="./src/julep/types/users/doc_list_response.py">DocListResponse</a></code>
- <code title="delete /users/{user_id}/docs/{doc_id}">client.users.docs.<a href="./src/julep/resources/users/docs.py">delete</a>(doc_id, \*, user_id) -> <a href="./src/julep/types/users/doc_delete_response.py">DocDeleteResponse</a></code>

# Jobs

Types:

```python
from julep.types import JobStatus
```

Methods:

- <code title="get /jobs/{job_id}">client.jobs.<a href="./src/julep/resources/jobs.py">retrieve</a>(job_id) -> <a href="./src/julep/types/job_status.py">JobStatus</a></code>

# Docs

Types:

```python
from julep.types import Doc, EmbedQueryResponse
```

Methods:

- <code title="post /embed">client.docs.<a href="./src/julep/resources/docs.py">create</a>(\*\*<a href="src/julep/types/doc_create_params.py">params</a>) -> <a href="./src/julep/types/embed_query_response.py">EmbedQueryResponse</a></code>
- <code title="get /docs/{doc_id}">client.docs.<a href="./src/julep/resources/docs.py">retrieve</a>(doc_id) -> <a href="./src/julep/types/doc.py">Doc</a></code>

# Tasks

Types:

```python
from julep.types import Task
```

Methods:

- <code title="get /tasks/{task_id}">client.tasks.<a href="./src/julep/resources/tasks/tasks.py">retrieve</a>(task_id) -> <a href="./src/julep/types/task.py">Task</a></code>

## Executions

Types:

```python
from julep.types.tasks import (
    ExecutionCreateResponse,
    ExecutionUpdateResponse,
    ExecutionListResponse,
)
```

Methods:

- <code title="post /tasks/{task_id}/executions">client.tasks.executions.<a href="./src/julep/resources/tasks/executions.py">create</a>(task_id, \*\*<a href="src/julep/types/tasks/execution_create_params.py">params</a>) -> <a href="./src/julep/types/tasks/execution_create_response.py">ExecutionCreateResponse</a></code>
- <code title="patch /tasks/{task_id}/executions/{execution_id}">client.tasks.executions.<a href="./src/julep/resources/tasks/executions.py">update</a>(execution_id, \*, task_id, \*\*<a href="src/julep/types/tasks/execution_update_params.py">params</a>) -> <a href="./src/julep/types/tasks/execution_update_response.py">ExecutionUpdateResponse</a></code>
- <code title="get /tasks/{task_id}/executions">client.tasks.executions.<a href="./src/julep/resources/tasks/executions.py">list</a>(task_id, \*\*<a href="src/julep/types/tasks/execution_list_params.py">params</a>) -> <a href="./src/julep/types/tasks/execution_list_response.py">ExecutionListResponse</a></code>

# Executions

Types:

```python
from julep.types import Execution, ExecutionUpdateResponse
```

Methods:

- <code title="get /executions/{execution_id}">client.executions.<a href="./src/julep/resources/executions/executions.py">retrieve</a>(execution_id) -> <a href="./src/julep/types/execution.py">Execution</a></code>
- <code title="put /executions/{execution_id}">client.executions.<a href="./src/julep/resources/executions/executions.py">update</a>(execution_id, \*\*<a href="src/julep/types/execution_update_params.py">params</a>) -> <a href="./src/julep/types/execution_update_response.py">object</a></code>

## Transitions

Types:

```python
from julep.types.executions import TransitionListResponse, TransitionListStreamResponse
```

Methods:

- <code title="get /executions/{execution_id}/transitions">client.executions.transitions.<a href="./src/julep/resources/executions/transitions.py">list</a>(execution_id, \*\*<a href="src/julep/types/executions/transition_list_params.py">params</a>) -> <a href="./src/julep/types/executions/transition_list_response.py">TransitionListResponse</a></code>
- <code title="get /executions/{execution_id}/transitions.stream">client.executions.transitions.<a href="./src/julep/resources/executions/transitions.py">list_stream</a>(execution_id, \*\*<a href="src/julep/types/executions/transition_list_stream_params.py">params</a>) -> <a href="./src/julep/types/executions/transition_list_stream_response.py">object</a></code>
