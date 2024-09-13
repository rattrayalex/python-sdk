# Agents

Types:

```python
from julep.types import (
    Agent,
    AgentCreateResponse,
    AgentUpdateResponse,
    AgentDeleteResponse,
    AgentCreateOrUpdateResponse,
    AgentPatchResponse,
)
```

Methods:

- <code title="post /agents">client.agents.<a href="./src/julep/resources/agents/agents.py">create</a>(\*\*<a href="src/julep/types/agent_create_params.py">params</a>) -> <a href="./src/julep/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="put /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/julep/types/agent_update_params.py">params</a>) -> <a href="./src/julep/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /agents">client.agents.<a href="./src/julep/resources/agents/agents.py">list</a>(\*\*<a href="src/julep/types/agent_list_params.py">params</a>) -> <a href="./src/julep/types/agent.py">SyncOffsetPagination[Agent]</a></code>
- <code title="delete /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">delete</a>(agent_id) -> <a href="./src/julep/types/agent_delete_response.py">AgentDeleteResponse</a></code>
- <code title="post /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">create_or_update</a>(agent_id, \*\*<a href="src/julep/types/agent_create_or_update_params.py">params</a>) -> <a href="./src/julep/types/agent_create_or_update_response.py">AgentCreateOrUpdateResponse</a></code>
- <code title="get /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">get</a>(agent_id) -> <a href="./src/julep/types/agent.py">Agent</a></code>
- <code title="patch /agents/{agent_id}">client.agents.<a href="./src/julep/resources/agents/agents.py">patch</a>(agent_id, \*\*<a href="src/julep/types/agent_patch_params.py">params</a>) -> <a href="./src/julep/types/agent_patch_response.py">AgentPatchResponse</a></code>

## Tools

Types:

```python
from julep.types.agents import (
    ToolCreateResponse,
    ToolUpdateResponse,
    ToolListResponse,
    ToolDeleteResponse,
    ToolPatchResponse,
)
```

Methods:

- <code title="post /agents/{agent_id}/tools">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">create</a>(agent_id, \*\*<a href="src/julep/types/agents/tool_create_params.py">params</a>) -> <a href="./src/julep/types/agents/tool_create_response.py">ToolCreateResponse</a></code>
- <code title="put /agents/{agent_id}/tools/{tool_id}">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">update</a>(tool_id, \*, agent_id, \*\*<a href="src/julep/types/agents/tool_update_params.py">params</a>) -> <a href="./src/julep/types/agents/tool_update_response.py">ToolUpdateResponse</a></code>
- <code title="get /agents/{agent_id}/tools">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">list</a>(agent_id, \*\*<a href="src/julep/types/agents/tool_list_params.py">params</a>) -> <a href="./src/julep/types/agents/tool_list_response.py">SyncOffsetPagination[ToolListResponse]</a></code>
- <code title="delete /agents/{agent_id}/tools/{tool_id}">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">delete</a>(tool_id, \*, agent_id) -> <a href="./src/julep/types/agents/tool_delete_response.py">ToolDeleteResponse</a></code>
- <code title="patch /agents/{agent_id}/tools/{tool_id}">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">patch</a>(tool_id, \*, agent_id, \*\*<a href="src/julep/types/agents/tool_patch_params.py">params</a>) -> <a href="./src/julep/types/agents/tool_patch_response.py">ToolPatchResponse</a></code>

## Docs

Types:

```python
from julep.types.agents import DocCreateResponse, DocDeleteResponse, DocSearchResponse
```

Methods:

- <code title="post /agents/{agent_id}/docs">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">create</a>(agent_id, \*\*<a href="src/julep/types/agents/doc_create_params.py">params</a>) -> <a href="./src/julep/types/agents/doc_create_response.py">DocCreateResponse</a></code>
- <code title="get /agents/{agent_id}/docs">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">list</a>(agent_id, \*\*<a href="src/julep/types/agents/doc_list_params.py">params</a>) -> <a href="./src/julep/types/doc.py">SyncOffsetPagination[Doc]</a></code>
- <code title="delete /agents/{agent_id}/docs/{doc_id}">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">delete</a>(doc_id, \*, agent_id) -> <a href="./src/julep/types/agents/doc_delete_response.py">DocDeleteResponse</a></code>
- <code title="post /agents/{agent_id}/search">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">search</a>(agent_id, \*\*<a href="src/julep/types/agents/doc_search_params.py">params</a>) -> <a href="./src/julep/types/agents/doc_search_response.py">DocSearchResponse</a></code>

## Tasks

Types:

```python
from julep.types.agents import TaskCreateResponse, TaskCreateOrUpdateResponse
```

Methods:

- <code title="post /agents/{agent_id}/tasks">client.agents.tasks.<a href="./src/julep/resources/agents/tasks.py">create</a>(agent_id, \*\*<a href="src/julep/types/agents/task_create_params.py">params</a>) -> <a href="./src/julep/types/agents/task_create_response.py">TaskCreateResponse</a></code>
- <code title="get /agents/{agent_id}/tasks">client.agents.tasks.<a href="./src/julep/resources/agents/tasks.py">list</a>(agent_id, \*\*<a href="src/julep/types/agents/task_list_params.py">params</a>) -> <a href="./src/julep/types/task.py">SyncOffsetPagination[Task]</a></code>
- <code title="post /agents/{agent_id}/tasks/{task_id}">client.agents.tasks.<a href="./src/julep/resources/agents/tasks.py">create_or_update</a>(task_id, \*, agent_id, \*\*<a href="src/julep/types/agents/task_create_or_update_params.py">params</a>) -> <a href="./src/julep/types/agents/task_create_or_update_response.py">TaskCreateOrUpdateResponse</a></code>

# Sessions

Types:

```python
from julep.types import (
    ChatInput,
    ChatResponse,
    History,
    Session,
    SessionCreateResponse,
    SessionUpdateResponse,
    SessionDeleteResponse,
    SessionChatResponse,
    SessionCreateOrUpdateResponse,
    SessionPatchResponse,
)
```

Methods:

- <code title="post /sessions">client.sessions.<a href="./src/julep/resources/sessions.py">create</a>(\*\*<a href="src/julep/types/session_create_params.py">params</a>) -> <a href="./src/julep/types/session_create_response.py">SessionCreateResponse</a></code>
- <code title="put /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions.py">update</a>(session_id, \*\*<a href="src/julep/types/session_update_params.py">params</a>) -> <a href="./src/julep/types/session_update_response.py">SessionUpdateResponse</a></code>
- <code title="get /sessions">client.sessions.<a href="./src/julep/resources/sessions.py">list</a>(\*\*<a href="src/julep/types/session_list_params.py">params</a>) -> <a href="./src/julep/types/session.py">SyncOffsetPagination[Session]</a></code>
- <code title="delete /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions.py">delete</a>(session_id) -> <a href="./src/julep/types/session_delete_response.py">SessionDeleteResponse</a></code>
- <code title="post /sessions/{session_id}/chat">client.sessions.<a href="./src/julep/resources/sessions.py">chat</a>(session_id, \*\*<a href="src/julep/types/session_chat_params.py">params</a>) -> <a href="./src/julep/types/session_chat_response.py">SessionChatResponse</a></code>
- <code title="post /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions.py">create_or_update</a>(session_id, \*\*<a href="src/julep/types/session_create_or_update_params.py">params</a>) -> <a href="./src/julep/types/session_create_or_update_response.py">SessionCreateOrUpdateResponse</a></code>
- <code title="get /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions.py">get</a>(session_id) -> <a href="./src/julep/types/session.py">Session</a></code>
- <code title="get /sessions/{session_id}/history">client.sessions.<a href="./src/julep/resources/sessions.py">history</a>(session_id) -> <a href="./src/julep/types/history.py">History</a></code>
- <code title="patch /sessions/{session_id}">client.sessions.<a href="./src/julep/resources/sessions.py">patch</a>(session_id, \*\*<a href="src/julep/types/session_patch_params.py">params</a>) -> <a href="./src/julep/types/session_patch_response.py">SessionPatchResponse</a></code>

# Users

Types:

```python
from julep.types import (
    User,
    UserCreateResponse,
    UserUpdateResponse,
    UserDeleteResponse,
    UserCreateOrUpdateResponse,
    UserPatchResponse,
)
```

Methods:

- <code title="post /users">client.users.<a href="./src/julep/resources/users/users.py">create</a>(\*\*<a href="src/julep/types/user_create_params.py">params</a>) -> <a href="./src/julep/types/user_create_response.py">UserCreateResponse</a></code>
- <code title="put /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">update</a>(user_id, \*\*<a href="src/julep/types/user_update_params.py">params</a>) -> <a href="./src/julep/types/user_update_response.py">UserUpdateResponse</a></code>
- <code title="get /users">client.users.<a href="./src/julep/resources/users/users.py">list</a>(\*\*<a href="src/julep/types/user_list_params.py">params</a>) -> <a href="./src/julep/types/user.py">SyncOffsetPagination[User]</a></code>
- <code title="delete /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">delete</a>(user_id) -> <a href="./src/julep/types/user_delete_response.py">UserDeleteResponse</a></code>
- <code title="post /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">create_or_update</a>(user_id, \*\*<a href="src/julep/types/user_create_or_update_params.py">params</a>) -> <a href="./src/julep/types/user_create_or_update_response.py">UserCreateOrUpdateResponse</a></code>
- <code title="get /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">get</a>(user_id) -> <a href="./src/julep/types/user.py">User</a></code>
- <code title="patch /users/{user_id}">client.users.<a href="./src/julep/resources/users/users.py">patch</a>(user_id, \*\*<a href="src/julep/types/user_patch_params.py">params</a>) -> <a href="./src/julep/types/user_patch_response.py">UserPatchResponse</a></code>

## Docs

Types:

```python
from julep.types.users import DocCreateResponse, DocDeleteResponse, DocSearchResponse
```

Methods:

- <code title="post /users/{user_id}/docs">client.users.docs.<a href="./src/julep/resources/users/docs.py">create</a>(user_id, \*\*<a href="src/julep/types/users/doc_create_params.py">params</a>) -> <a href="./src/julep/types/users/doc_create_response.py">DocCreateResponse</a></code>
- <code title="get /users/{user_id}/docs">client.users.docs.<a href="./src/julep/resources/users/docs.py">list</a>(user_id, \*\*<a href="src/julep/types/users/doc_list_params.py">params</a>) -> <a href="./src/julep/types/doc.py">SyncOffsetPagination[Doc]</a></code>
- <code title="delete /users/{user_id}/docs/{doc_id}">client.users.docs.<a href="./src/julep/resources/users/docs.py">delete</a>(doc_id, \*, user_id) -> <a href="./src/julep/types/users/doc_delete_response.py">DocDeleteResponse</a></code>
- <code title="post /users/{user_id}/search">client.users.docs.<a href="./src/julep/resources/users/docs.py">search</a>(user_id, \*\*<a href="src/julep/types/users/doc_search_params.py">params</a>) -> <a href="./src/julep/types/users/doc_search_response.py">DocSearchResponse</a></code>

# Jobs

Types:

```python
from julep.types import JobStatus
```

Methods:

- <code title="get /jobs/{job_id}">client.jobs.<a href="./src/julep/resources/jobs.py">get</a>(job_id) -> <a href="./src/julep/types/job_status.py">JobStatus</a></code>

# Docs

Types:

```python
from julep.types import Doc, EmbedQueryResponse
```

Methods:

- <code title="post /embed">client.docs.<a href="./src/julep/resources/docs.py">create</a>(\*\*<a href="src/julep/types/doc_create_params.py">params</a>) -> <a href="./src/julep/types/embed_query_response.py">EmbedQueryResponse</a></code>
- <code title="get /docs/{doc_id}">client.docs.<a href="./src/julep/resources/docs.py">get</a>(doc_id) -> <a href="./src/julep/types/doc.py">Doc</a></code>

# Tasks

Types:

```python
from julep.types import Task
```

Methods:

- <code title="get /tasks/{task_id}">client.tasks.<a href="./src/julep/resources/tasks/tasks.py">get</a>(task_id) -> <a href="./src/julep/types/task.py">Task</a></code>

## Executions

Types:

```python
from julep.types.tasks import ExecutionCreateResponse, ExecutionUpdateResponse
```

Methods:

- <code title="post /tasks/{task_id}/executions">client.tasks.executions.<a href="./src/julep/resources/tasks/executions.py">create</a>(task_id, \*\*<a href="src/julep/types/tasks/execution_create_params.py">params</a>) -> <a href="./src/julep/types/tasks/execution_create_response.py">ExecutionCreateResponse</a></code>
- <code title="patch /tasks/{task_id}/executions/{execution_id}">client.tasks.executions.<a href="./src/julep/resources/tasks/executions.py">update</a>(execution_id, \*, task_id, \*\*<a href="src/julep/types/tasks/execution_update_params.py">params</a>) -> <a href="./src/julep/types/tasks/execution_update_response.py">ExecutionUpdateResponse</a></code>
- <code title="get /tasks/{task_id}/executions">client.tasks.executions.<a href="./src/julep/resources/tasks/executions.py">list</a>(task_id, \*\*<a href="src/julep/types/tasks/execution_list_params.py">params</a>) -> <a href="./src/julep/types/execution.py">SyncOffsetPagination[Execution]</a></code>

# Executions

Types:

```python
from julep.types import Execution, Transition, ExecutionUpdateResponse
```

Methods:

- <code title="put /executions/{execution_id}">client.executions.<a href="./src/julep/resources/executions/executions.py">update</a>(execution_id, \*\*<a href="src/julep/types/execution_update_params.py">params</a>) -> <a href="./src/julep/types/execution_update_response.py">object</a></code>
- <code title="get /executions/{execution_id}">client.executions.<a href="./src/julep/resources/executions/executions.py">get</a>(execution_id) -> <a href="./src/julep/types/execution.py">Execution</a></code>

## Transitions

Types:

```python
from julep.types.executions import TransitionStreamResponse
```

Methods:

- <code title="get /executions/{execution_id}/transitions">client.executions.transitions.<a href="./src/julep/resources/executions/transitions.py">list</a>(execution_id, \*\*<a href="src/julep/types/executions/transition_list_params.py">params</a>) -> <a href="./src/julep/types/transition.py">SyncOffsetPagination[Transition]</a></code>
- <code title="get /executions/{execution_id}/transitions.stream">client.executions.transitions.<a href="./src/julep/resources/executions/transitions.py">stream</a>(execution_id, \*\*<a href="src/julep/types/executions/transition_stream_params.py">params</a>) -> <a href="./src/julep/types/executions/transition_stream_response.py">object</a></code>
