# MeaningsService

A list of all methods in the `MeaningsService` service. Click on the method name to view detailed information about that method.

| Methods                     | Description                                                                                                               |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| [new](#new)                 | Create new collection (default or specified settings)                                                                     |
| [get](#get)                 | Obtain the lastest value for meaning with specified 'name'                                                                |
| [set](#set)                 | Remove all previous values for specified 'name' and add a new value                                                       |
| [add](#add)                 | Add a new value for specified 'name'                                                                                      |
| [all](#all)                 | Obtain a list of all meanings with specified 'name'                                                                       |
| [update](#update)           | Remove previously set and add new meanings with specified 'name' fileds with values from 'values' fileds of provided list |
| [remove](#remove)           | Remove all values for specified 'name'                                                                                    |
| [display](#display)         | Display a list of all meanings with specified 'name'                                                                      |
| [revisions](#revisions)     | List of all avaliable revisions (aka 'collection')                                                                        |
| [new_1](#new_1)             | Create new collection (default or specified settings)                                                                     |
| [get_1](#get_1)             | Obtain the lastest value for meaning with specified 'name'                                                                |
| [set_1](#set_1)             | Remove all previous values for specified 'name' and add a new value                                                       |
| [add_1](#add_1)             | Add a new value for specified 'name'                                                                                      |
| [all_1](#all_1)             | Obtain a list of all meanings with specified 'name'                                                                       |
| [update_1](#update_1)       | Remove previously set and add new meanings with specified 'name' fileds with values from 'values' fileds of provided list |
| [remove_1](#remove_1)       | Remove all values for specified 'name'                                                                                    |
| [display_1](#display_1)     | Display a list of all meanings with specified 'name'                                                                      |
| [revisions_1](#revisions_1) | List of all avaliable revisions (aka 'collection')                                                                        |

## new

Create new collection (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/api/v1/meanings/revision/new`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| init       | str  | ❌       |             |
| collection | str  | ❌       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.meanings.new(
    init="init",
    collection="collection"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get

Obtain the lastest value for meaning with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/meanings/actual/get`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| name       | str  | ✅       |             |
| collection | str  | ❌       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.meanings.get(
    name="name",
    collection="collection"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## set

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/api/v1/meanings/actual/set`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| name       | str  | ✅       |             |
| value      | str  | ❌       |             |
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

result = sdk.meanings.set(
    name="name",
    value="value",
    collection="collection"
)

print(result)
```

## add

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/api/v1/meanings/actual/add`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| name       | str  | ✅       |             |
| value      | str  | ❌       |             |
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

result = sdk.meanings.add(
    name="name",
    value="value",
    collection="collection"
)

print(result)
```

## all

Obtain a list of all meanings with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/meanings/all/get`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| name       | str  | ❌       |             |
| collection | str  | ❌       |             |

**Return Type**

`List[Meaning]`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.meanings.all(
    name="name",
    collection="collection"
)

print(result)
```

## update

Remove previously set and add new meanings with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/api/v1/meanings/all/update`

**Parameters**

| Name         | Type                                  | Required | Description       |
| :----------- | :------------------------------------ | :------- | :---------------- |
| request_body | [List[Meaning]](../models/Meaning.md) | ✅       | The request body. |
| collection   | str                                   | ❌       |                   |

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
        "value": "value"
    }
]

result = sdk.meanings.update(
    request_body=request_body,
    collection="collection"
)

print(result)
```

## remove

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/meanings/all/remove`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| name       | str  | ❌       |             |
| value      | str  | ❌       |             |
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

result = sdk.meanings.remove(
    name="name",
    value="value",
    collection="collection"
)

print(result)
```

## display

Display a list of all meanings with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/meanings/all/display`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| name       | str  | ❌       |             |
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

result = sdk.meanings.display(
    name="name",
    collection="collection",
    format="format"
)

print(result)
```

## revisions

List of all avaliable revisions (aka 'collection')

- HTTP Method: `GET`
- Endpoint: `/api/v1/meanings/rev/list`

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

result = sdk.meanings.revisions()

print(result)
```

## new_1

Create new collection (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/meanings/revision/new`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| init       | str  | ❌       |             |
| collection | str  | ❌       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.meanings.new_1(
    init="init",
    collection="collection"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_1

Obtain the lastest value for meaning with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/meanings/actual/get`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| name       | str  | ✅       |             |
| collection | str  | ❌       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.meanings.get_1(
    name="name",
    collection="collection"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## set_1

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/meanings/actual/set`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| name       | str  | ✅       |             |
| value      | str  | ❌       |             |
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

result = sdk.meanings.set_1(
    name="name",
    value="value",
    collection="collection"
)

print(result)
```

## add_1

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/meanings/actual/add`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| name       | str  | ✅       |             |
| value      | str  | ❌       |             |
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

result = sdk.meanings.add_1(
    name="name",
    value="value",
    collection="collection"
)

print(result)
```

## all_1

Obtain a list of all meanings with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/meanings/all/get`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| name       | str  | ❌       |             |
| collection | str  | ❌       |             |

**Return Type**

`List[Meaning]`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.meanings.all_1(
    name="name",
    collection="collection"
)

print(result)
```

## update_1

Remove previously set and add new meanings with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/meanings/all/update`

**Parameters**

| Name         | Type                                  | Required | Description       |
| :----------- | :------------------------------------ | :------- | :---------------- |
| request_body | [List[Meaning]](../models/Meaning.md) | ✅       | The request body. |
| collection   | str                                   | ❌       |                   |

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
        "value": "value"
    }
]

result = sdk.meanings.update_1(
    request_body=request_body,
    collection="collection"
)

print(result)
```

## remove_1

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/api/v1/meanings/all/remove`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| name       | str  | ❌       |             |
| value      | str  | ❌       |             |
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

result = sdk.meanings.remove_1(
    name="name",
    value="value",
    collection="collection"
)

print(result)
```

## display_1

Display a list of all meanings with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/meanings/all/display`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| name       | str  | ❌       |             |
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

result = sdk.meanings.display_1(
    name="name",
    collection="collection",
    format="format"
)

print(result)
```

## revisions_1

List of all avaliable revisions (aka 'collection')

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/meanings/rev/list`

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

result = sdk.meanings.revisions_1()

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
