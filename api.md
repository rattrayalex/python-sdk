# Shared Types

```python
from julep.types import ResourceCreated, ResourceDeleted, ResourceUpdated
```

# Agents

Types:

```python
from julep.types import Agent
```

Methods:

- <code title="post /agents">client.agents.<a href="./src/julep/resources/agents/agents.py">create</a>(\*\*<a href="src/julep/types/agent_create_params.py">params</a>) -> <a href="./src/julep/types/shared/resource_created.py">ResourceCreated</a></code>
- <code title="get /agents">client.agents.<a href="./src/julep/resources/agents/agents.py">list</a>(\*\*<a href="src/julep/types/agent_list_params.py">params</a>) -> <a href="./src/julep/types/agent.py">SyncOffsetPagination[Agent]</a></code>

## Tools

Types:

```python
from julep.types.agents import ToolListResponse
```

Methods:

- <code title="post /agents/{agent_id}/tools">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">create</a>(agent_id, \*\*<a href="src/julep/types/agents/tool_create_params.py">params</a>) -> <a href="./src/julep/types/shared/resource_created.py">ResourceCreated</a></code>
- <code title="get /agents/{agent_id}/tools">client.agents.tools.<a href="./src/julep/resources/agents/tools.py">list</a>(agent_id, \*\*<a href="src/julep/types/agents/tool_list_params.py">params</a>) -> <a href="./src/julep/types/agents/tool_list_response.py">SyncOffsetPagination[ToolListResponse]</a></code>

## Docs

Types:

```python
from julep.types.agents import DocSearchResponse
```

Methods:

- <code title="post /agents/{agent_id}/docs">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">create</a>(agent_id, \*\*<a href="src/julep/types/agents/doc_create_params.py">params</a>) -> <a href="./src/julep/types/shared/resource_created.py">ResourceCreated</a></code>
- <code title="get /agents/{agent_id}/docs">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">list</a>(agent_id, \*\*<a href="src/julep/types/agents/doc_list_params.py">params</a>) -> <a href="./src/julep/types/doc.py">SyncOffsetPagination[Doc]</a></code>
- <code title="post /agents/{agent_id}/search">client.agents.docs.<a href="./src/julep/resources/agents/docs.py">search</a>(agent_id, \*\*<a href="src/julep/types/agents/doc_search_params.py">params</a>) -> <a href="./src/julep/types/agents/doc_search_response.py">DocSearchResponse</a></code>

## Tasks

Methods:

- <code title="post /agents/{agent_id}/tasks">client.agents.tasks.<a href="./src/julep/resources/agents/tasks.py">create</a>(agent_id, \*\*<a href="src/julep/types/agents/task_create_params.py">params</a>) -> <a href="./src/julep/types/shared/resource_created.py">ResourceCreated</a></code>
- <code title="get /agents/{agent_id}/tasks">client.agents.tasks.<a href="./src/julep/resources/agents/tasks.py">list</a>(agent_id, \*\*<a href="src/julep/types/agents/task_list_params.py">params</a>) -> <a href="./src/julep/types/task.py">SyncOffsetPagination[Task]</a></code>

# Sessions

Types:

```python
from julep.types import ChatInput, ChatResponse, ChatSettings, Entry, History, Message, Session
```

Methods:

- <code title="post /sessions">client.sessions.<a href="./src/julep/resources/sessions.py">create</a>(\*\*<a href="src/julep/types/session_create_params.py">params</a>) -> <a href="./src/julep/types/shared/resource_created.py">ResourceCreated</a></code>
- <code title="get /sessions">client.sessions.<a href="./src/julep/resources/sessions.py">list</a>(\*\*<a href="src/julep/types/session_list_params.py">params</a>) -> <a href="./src/julep/types/session.py">SyncOffsetPagination[Session]</a></code>

# Users

Types:

```python
from julep.types import User
```

Methods:

- <code title="post /users">client.users.<a href="./src/julep/resources/users/users.py">create</a>(\*\*<a href="src/julep/types/user_create_params.py">params</a>) -> <a href="./src/julep/types/shared/resource_created.py">ResourceCreated</a></code>
- <code title="get /users">client.users.<a href="./src/julep/resources/users/users.py">list</a>(\*\*<a href="src/julep/types/user_list_params.py">params</a>) -> <a href="./src/julep/types/user.py">SyncOffsetPagination[User]</a></code>

## Docs

Types:

```python
from julep.types.users import DocSearchResponse
```

Methods:

- <code title="post /users/{user_id}/docs">client.users.docs.<a href="./src/julep/resources/users/docs.py">create</a>(user_id, \*\*<a href="src/julep/types/users/doc_create_params.py">params</a>) -> <a href="./src/julep/types/shared/resource_created.py">ResourceCreated</a></code>
- <code title="get /users/{user_id}/docs">client.users.docs.<a href="./src/julep/resources/users/docs.py">list</a>(user_id, \*\*<a href="src/julep/types/users/doc_list_params.py">params</a>) -> <a href="./src/julep/types/doc.py">SyncOffsetPagination[Doc]</a></code>
- <code title="post /users/{user_id}/search">client.users.docs.<a href="./src/julep/resources/users/docs.py">search</a>(user_id, \*\*<a href="src/julep/types/users/doc_search_params.py">params</a>) -> <a href="./src/julep/types/users/doc_search_response.py">DocSearchResponse</a></code>

# Jobs

Types:

```python
from julep.types import JobStatus
```

# Docs

Types:

```python
from julep.types import Doc, EmbedQueryResponse, Snippet
```

Methods:

- <code title="post /embed">client.docs.<a href="./src/julep/resources/docs.py">embed</a>(\*\*<a href="src/julep/types/doc_embed_params.py">params</a>) -> <a href="./src/julep/types/embed_query_response.py">EmbedQueryResponse</a></code>

# Tasks

Types:

```python
from julep.types import Task, Tool
```

## Executions

Methods:

- <code title="post /tasks/{task_id}/executions">client.tasks.executions.<a href="./src/julep/resources/tasks/executions.py">create</a>(task_id, \*\*<a href="src/julep/types/tasks/execution_create_params.py">params</a>) -> <a href="./src/julep/types/shared/resource_created.py">ResourceCreated</a></code>
- <code title="get /tasks/{task_id}/executions">client.tasks.executions.<a href="./src/julep/resources/tasks/executions.py">list</a>(task_id, \*\*<a href="src/julep/types/tasks/execution_list_params.py">params</a>) -> <a href="./src/julep/types/execution.py">SyncOffsetPagination[Execution]</a></code>

# Executions

Types:

```python
from julep.types import Execution, Transition
```

## Transitions

Types:

```python
from julep.types.executions import TransitionStreamResponse
```

Methods:

- <code title="get /executions/{execution_id}/transitions">client.executions.transitions.<a href="./src/julep/resources/executions/transitions.py">list</a>(execution_id, \*\*<a href="src/julep/types/executions/transition_list_params.py">params</a>) -> <a href="./src/julep/types/transition.py">SyncOffsetPagination[Transition]</a></code>
- <code title="get /executions/{execution_id}/transitions.stream">client.executions.transitions.<a href="./src/julep/resources/executions/transitions.py">stream</a>(execution_id, \*\*<a href="src/julep/types/executions/transition_stream_params.py">params</a>) -> <a href="./src/julep/types/executions/transition_stream_response.py">object</a></code>
