# PropertiesService

A list of all methods in the `PropertiesService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                                 |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------------- |
| [get](#get)         | Obtain the lastest value for preference with specified 'key'                                                                |
| [set](#set)         | Remove all previous values for specified 'key' and add a new value                                                          |
| [all](#all)         | Obtain a list of all preferences with specified 'key'                                                                       |
| [replace](#replace) | Remove previously set and add new preferences with specified 'key' fileds with values from 'values' fileds of provided list |
| [remove](#remove)   | Remove all values for specified 'key'                                                                                       |

## get

Obtain the lastest value for preference with specified 'key'

- HTTP Method: `GET`
- Endpoint: `/properties/actual/{key}`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| key   | str  | ✅       |             |
| pid   | str  | ❌       |             |
| build | str  | ❌       |             |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.properties.get(
    key="key",
    pid="pid",
    build="build"
)

print(result)
```

## set

Remove all previous values for specified 'key' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/properties/actual/{key}`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| key   | str  | ✅       |             |
| value | str  | ❌       |             |
| pid   | str  | ❌       |             |
| build | str  | ❌       |             |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.properties.set(
    key="key",
    value="value",
    pid="pid",
    build="build"
)

print(result)
```

## all

Obtain a list of all preferences with specified 'key'

- HTTP Method: `GET`
- Endpoint: `/properties/all`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| key   | str  | ❌       |             |
| pid   | str  | ❌       |             |
| build | str  | ❌       |             |

**Return Type**

`List[Property]`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.properties.all(
    key="key",
    pid="pid",
    build="build"
)

print(result)
```

## replace

Remove previously set and add new preferences with specified 'key' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/properties/all`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [List[Property]](../models/Property.md) | ✅       | The request body. |
| pid          | str                                     | ❌       |                   |
| build        | str                                     | ❌       |                   |

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

result = sdk.properties.replace(
    request_body=request_body,
    pid="pid",
    build="build"
)

print(result)
```

## remove

Remove all values for specified 'key'

- HTTP Method: `DELETE`
- Endpoint: `/properties/all/{key}`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| key   | str  | ✅       |             |
| value | str  | ❌       |             |
| pid   | str  | ❌       |             |
| build | str  | ❌       |             |

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

result = sdk.properties.remove(
    key="key",
    value="value",
    pid="pid",
    build="build"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
