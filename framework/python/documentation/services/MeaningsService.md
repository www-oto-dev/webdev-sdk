# MeaningsService

A list of all methods in the `MeaningsService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                              |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------- |
| [new](#new)         | Create new collection (default or specified settings) and return collections's hex string ID                             |
| [get](#get)         | Obtain the lastest value for meaning with specified 'key'                                                                |
| [set](#set)         | Remove all previous values for specified 'key' and add a new value                                                       |
| [add](#add)         | Add a new value for specified 'key'                                                                                      |
| [all](#all)         | Obtain a list of all meanings with specified 'key'                                                                       |
| [update](#update)   | Remove previously set and add new meanings with specified 'key' fileds with values from 'values' fileds of provided list |
| [remove](#remove)   | Remove all values for specified 'key'                                                                                    |
| [display](#display) | Display a list of all meanings with specified 'key'                                                                      |

## new

Create new collection (default or specified settings) and return collections's hex string ID

- HTTP Method: `PUT`
- Endpoint: `/meanings/collection/new`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| init | str  | ❌       |             |

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

result = sdk.meanings.new(init="init")

print(result)
```

## get

Obtain the lastest value for meaning with specified 'key'

- HTTP Method: `GET`
- Endpoint: `/meanings/actual/get`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| key        | str  | ✅       |             |
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
    key="key",
    collection="collection"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## set

Remove all previous values for specified 'key' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/meanings/actual/set`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| key        | str  | ✅       |             |
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
    key="key",
    value="value",
    collection="collection"
)

print(result)
```

## add

Add a new value for specified 'key'

- HTTP Method: `PUT`
- Endpoint: `/meanings/actual/add`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| key        | str  | ✅       |             |
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
    key="key",
    value="value",
    collection="collection"
)

print(result)
```

## all

Obtain a list of all meanings with specified 'key'

- HTTP Method: `GET`
- Endpoint: `/meanings/all/get`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| key        | str  | ❌       |             |
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
    key="key",
    collection="collection"
)

print(result)
```

## update

Remove previously set and add new meanings with specified 'key' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/meanings/all/update`

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
        "key": "key",
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

Remove all values for specified 'key'

- HTTP Method: `DELETE`
- Endpoint: `/meanings/all/remove`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| key        | str  | ❌       |             |
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
    key="key",
    value="value",
    collection="collection"
)

print(result)
```

## display

Display a list of all meanings with specified 'key'

- HTTP Method: `GET`
- Endpoint: `/meanings/all/display`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| key        | str  | ❌       |             |
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
    key="key",
    collection="collection",
    format="format"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->