# ContextService

A list of all methods in the `ContextService` service. Click on the method name to view detailed information about that method.

| Methods                     | Description                                                      |
| :-------------------------- | :--------------------------------------------------------------- |
| [add](#add)                 | Add a new cpntext with specified options                         |
| [context](#context)         | Obtain a context using text                                      |
| [all](#all)                 | Obtain a list of all context with specified options              |
| [update](#update)           | Remove previously set and add new context with specified options |
| [remove](#remove)           | Remove all values for specified options                          |
| [display](#display)         | Display a list of all context with specified options             |
| [revisions](#revisions)     | List of all avaliable revisions (aka 'collection')               |
| [add_1](#add_1)             | Add a new cpntext with specified options                         |
| [context_1](#context_1)     | Obtain a context using text                                      |
| [all_1](#all_1)             | Obtain a list of all context with specified options              |
| [update_1](#update_1)       | Remove previously set and add new context with specified options |
| [remove_1](#remove_1)       | Remove all values for specified options                          |
| [display_1](#display_1)     | Display a list of all context with specified options             |
| [revisions_1](#revisions_1) | List of all avaliable revisions (aka 'collection')               |

## add

Add a new cpntext with specified options

- HTTP Method: `PUT`
- Endpoint: `/api/v1/context/actual/add`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| text       | str  | ✅       |             |
| role       | str  | ❌       |             |
| origin     | str  | ❌       |             |
| source     | str  | ❌       |             |
| page       | str  | ❌       |             |
| timestamp  | str  | ❌       |             |
| collection | str  | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.context.add(
    text="text",
    role="role",
    origin="origin",
    source="source",
    page="page",
    timestamp="timestamp",
    collection="collection"
)

print(result)
```

## context

Obtain a context using text

- HTTP Method: `GET`
- Endpoint: `/api/v1/context/actual/context`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| role       | str  | ❌       |             |
| origin     | str  | ❌       |             |
| source     | str  | ❌       |             |
| page       | str  | ❌       |             |
| timestamp  | str  | ❌       |             |
| collection | str  | ❌       |             |

**Return Type**

`List[MenuItem]`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.context.context(
    role="role",
    origin="origin",
    source="source",
    page="page",
    timestamp="timestamp",
    collection="collection"
)

print(result)
```

## all

Obtain a list of all context with specified options

- HTTP Method: `GET`
- Endpoint: `/api/v1/context/all/get`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| role       | str  | ❌       |             |
| origin     | str  | ❌       |             |
| source     | str  | ❌       |             |
| page       | str  | ❌       |             |
| timestamp  | str  | ❌       |             |
| collection | str  | ❌       |             |

**Return Type**

`List[MenuItem]`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.context.all(
    role="role",
    origin="origin",
    source="source",
    page="page",
    timestamp="timestamp",
    collection="collection"
)

print(result)
```

## update

Remove previously set and add new context with specified options

- HTTP Method: `PUT`
- Endpoint: `/api/v1/context/all/update`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [List[MenuItem]](../models/MenuItem.md) | ✅       | The request body. |
| collection   | str                                     | ❌       |                   |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = [
    {
        "name": "name",
        "value": "value",
        "type_": "type",
        "target": "target"
    }
]

result = sdk.context.update(
    request_body=request_body,
    collection="collection"
)

print(result)
```

## remove

Remove all values for specified options

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/context/all/remove`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| text       | str  | ❌       |             |
| role       | str  | ❌       |             |
| origin     | str  | ❌       |             |
| source     | str  | ❌       |             |
| page       | str  | ❌       |             |
| timestamp  | str  | ❌       |             |
| collection | str  | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.context.remove(
    text="text",
    role="role",
    origin="origin",
    source="source",
    page="page",
    timestamp="timestamp",
    collection="collection"
)

print(result)
```

## display

Display a list of all context with specified options

- HTTP Method: `GET`
- Endpoint: `/api/v1/context/all/display`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| role       | str  | ❌       |             |
| origin     | str  | ❌       |             |
| source     | str  | ❌       |             |
| page       | str  | ❌       |             |
| timestamp  | str  | ❌       |             |
| collection | str  | ❌       |             |
| format     | str  | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.context.display(
    role="role",
    origin="origin",
    source="source",
    page="page",
    timestamp="timestamp",
    collection="collection",
    format="format"
)

print(result)
```

## revisions

List of all avaliable revisions (aka 'collection')

- HTTP Method: `GET`
- Endpoint: `/api/v1/context/rev/list`

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.context.revisions()

print(result)
```

## add_1

Add a new cpntext with specified options

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/context/actual/add`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| text       | str  | ✅       |             |
| role       | str  | ❌       |             |
| origin     | str  | ❌       |             |
| source     | str  | ❌       |             |
| page       | str  | ❌       |             |
| timestamp  | str  | ❌       |             |
| collection | str  | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.context.add_1(
    text="text",
    role="role",
    origin="origin",
    source="source",
    page="page",
    timestamp="timestamp",
    collection="collection"
)

print(result)
```

## context_1

Obtain a context using text

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/context/actual/context`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| role       | str  | ❌       |             |
| origin     | str  | ❌       |             |
| source     | str  | ❌       |             |
| page       | str  | ❌       |             |
| timestamp  | str  | ❌       |             |
| collection | str  | ❌       |             |

**Return Type**

`List[MenuItem]`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.context.context_1(
    role="role",
    origin="origin",
    source="source",
    page="page",
    timestamp="timestamp",
    collection="collection"
)

print(result)
```

## all_1

Obtain a list of all context with specified options

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/context/all/get`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| role       | str  | ❌       |             |
| origin     | str  | ❌       |             |
| source     | str  | ❌       |             |
| page       | str  | ❌       |             |
| timestamp  | str  | ❌       |             |
| collection | str  | ❌       |             |

**Return Type**

`List[MenuItem]`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.context.all_1(
    role="role",
    origin="origin",
    source="source",
    page="page",
    timestamp="timestamp",
    collection="collection"
)

print(result)
```

## update_1

Remove previously set and add new context with specified options

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/context/all/update`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [List[MenuItem]](../models/MenuItem.md) | ✅       | The request body. |
| collection   | str                                     | ❌       |                   |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = [
    {
        "name": "name",
        "value": "value",
        "type_": "type",
        "target": "target"
    }
]

result = sdk.context.update_1(
    request_body=request_body,
    collection="collection"
)

print(result)
```

## remove_1

Remove all values for specified options

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/api/v1/context/all/remove`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| text       | str  | ❌       |             |
| role       | str  | ❌       |             |
| origin     | str  | ❌       |             |
| source     | str  | ❌       |             |
| page       | str  | ❌       |             |
| timestamp  | str  | ❌       |             |
| collection | str  | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.context.remove_1(
    text="text",
    role="role",
    origin="origin",
    source="source",
    page="page",
    timestamp="timestamp",
    collection="collection"
)

print(result)
```

## display_1

Display a list of all context with specified options

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/context/all/display`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| role       | str  | ❌       |             |
| origin     | str  | ❌       |             |
| source     | str  | ❌       |             |
| page       | str  | ❌       |             |
| timestamp  | str  | ❌       |             |
| collection | str  | ❌       |             |
| format     | str  | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.context.display_1(
    role="role",
    origin="origin",
    source="source",
    page="page",
    timestamp="timestamp",
    collection="collection",
    format="format"
)

print(result)
```

## revisions_1

List of all avaliable revisions (aka 'collection')

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/context/rev/list`

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.context.revisions_1()

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
