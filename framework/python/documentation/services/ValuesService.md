# ValuesService

A list of all methods in the `ValuesService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                             |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------- |
| [new](#new)         | Create new dataset (default or specified settings)                                                                      |
| [get](#get)         | Obtain the lastest value for variable with specified 'name'                                                             |
| [set](#set)         | Remove all previous values for specified 'name' and add a new value                                                     |
| [add](#add)         | Add a new value for specified 'name'                                                                                    |
| [all](#all)         | Obtain a list of all values with specified 'name'                                                                       |
| [update](#update)   | Remove previously set and add new values with specified 'name' fileds with values from 'values' fileds of provided list |
| [remove](#remove)   | Remove all values for specified 'name'                                                                                  |
| [display](#display) | Display a list of all values with specified 'name'                                                                      |

## new

Create new dataset (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/values/revision/new`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| init    | str  | ❌       |             |
| dataset | str  | ❌       |             |

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

result = sdk.values.new(
    init="init",
    dataset="dataset"
)

print(result)
```

## get

Obtain the lastest value for variable with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/values/actual/get`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ✅       |             |
| dataset | str  | ❌       |             |

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

result = sdk.values.get(
    name="name",
    dataset="dataset"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## set

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/values/actual/set`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ✅       |             |
| value   | str  | ❌       |             |
| dataset | str  | ❌       |             |

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

result = sdk.values.set(
    name="name",
    value="value",
    dataset="dataset"
)

print(result)
```

## add

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/values/actual/add`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ✅       |             |
| value   | str  | ❌       |             |
| dataset | str  | ❌       |             |

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

result = sdk.values.add(
    name="name",
    value="value",
    dataset="dataset"
)

print(result)
```

## all

Obtain a list of all values with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/values/all/get`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ❌       |             |
| dataset | str  | ❌       |             |

**Return Type**

`List[Value]`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.values.all(
    name="name",
    dataset="dataset"
)

print(result)
```

## update

Remove previously set and add new values with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/values/all/update`

**Parameters**

| Name         | Type                              | Required | Description       |
| :----------- | :-------------------------------- | :------- | :---------------- |
| request_body | [List[Value]](../models/Value.md) | ✅       | The request body. |
| dataset      | str                               | ❌       |                   |

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

result = sdk.values.update(
    request_body=request_body,
    dataset="dataset"
)

print(result)
```

## remove

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/values/all/remove`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ❌       |             |
| value   | str  | ❌       |             |
| dataset | str  | ❌       |             |

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

result = sdk.values.remove(
    name="name",
    value="value",
    dataset="dataset"
)

print(result)
```

## display

Display a list of all values with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/values/all/display`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ❌       |             |
| dataset | str  | ❌       |             |
| format  | str  | ❌       |             |

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

result = sdk.values.display(
    name="name",
    dataset="dataset",
    format="format"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
