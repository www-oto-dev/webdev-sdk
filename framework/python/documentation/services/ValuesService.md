# ValuesService

A list of all methods in the `ValuesService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                                |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------- |
| [new](#new)         | Create new dataset (default or specified datasettings) and return dataset's hex string ID                                  |
| [get](#get)         | Obtain the lastest value for meaning with specified 'key'                                                                  |
| [dataset](#dataset) | Remove all previous values for specified 'key' and add a new value                                                         |
| [add](#add)         | Add a new value for specified 'key'                                                                                        |
| [all](#all)         | Obtain a list of all values with specified 'key'                                                                           |
| [update](#update)   | Remove previously dataset and add new values with specified 'key' fileds with values from 'values' fileds of provided list |
| [remove](#remove)   | Remove all values for specified 'key'                                                                                      |
| [display](#display) | Display a list of all values with specified 'key'                                                                          |

## new

Create new dataset (default or specified datasettings) and return dataset's hex string ID

- HTTP Method: `PUT`
- Endpoint: `/values/dataset/new`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| init | str  | ❌       |             |

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

result = sdk.values.new(init="init")

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get

Obtain the lastest value for meaning with specified 'key'

- HTTP Method: `GET`
- Endpoint: `/values/actual/get`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| key     | str  | ✅       |             |
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
    key="key",
    dataset="dataset"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## dataset

Remove all previous values for specified 'key' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/values/actual/dataset`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| key     | str  | ✅       |             |
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

result = sdk.values.dataset(
    key="key",
    value="value",
    dataset="dataset"
)

print(result)
```

## add

Add a new value for specified 'key'

- HTTP Method: `PUT`
- Endpoint: `/values/actual/add`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| key     | str  | ✅       |             |
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
    key="key",
    value="value",
    dataset="dataset"
)

print(result)
```

## all

Obtain a list of all values with specified 'key'

- HTTP Method: `GET`
- Endpoint: `/values/all/get`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| key     | str  | ❌       |             |
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
    key="key",
    dataset="dataset"
)

print(result)
```

## update

Remove previously dataset and add new values with specified 'key' fileds with values from 'values' fileds of provided list

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
        "key": "key",
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

Remove all values for specified 'key'

- HTTP Method: `DELETE`
- Endpoint: `/values/all/remove`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| key     | str  | ✅       |             |
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
    key="key",
    value="value",
    dataset="dataset"
)

print(result)
```

## display

Display a list of all values with specified 'key'

- HTTP Method: `GET`
- Endpoint: `/values/all/display`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| key     | str  | ❌       |             |
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
    key="key",
    dataset="dataset",
    format="format"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
