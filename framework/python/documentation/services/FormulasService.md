# FormulasService

A list of all methods in the `FormulasService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                              |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------- |
| [new](#new)         | Create new set (default or specified settings) and return set's hex string ID                                            |
| [get](#get)         | Obtain the lastest value for meaning with specified 'key'                                                                |
| [set](#set)         | Remove all previous values for specified 'key' and add a new value                                                       |
| [add](#add)         | Add a new value for specified 'key'                                                                                      |
| [all](#all)         | Obtain a list of all formulas with specified 'key'                                                                       |
| [update](#update)   | Remove previously set and add new formulas with specified 'key' fileds with values from 'values' fileds of provided list |
| [remove](#remove)   | Remove all values for specified 'key'                                                                                    |
| [display](#display) | Display a list of all formulas with specified 'key'                                                                      |

## new

Create new set (default or specified settings) and return set's hex string ID

- HTTP Method: `PUT`
- Endpoint: `/formulas/set/new`

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

result = sdk.formulas.new(init="init")

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get

Obtain the lastest value for meaning with specified 'key'

- HTTP Method: `GET`
- Endpoint: `/formulas/actual/get`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| key  | str  | ✅       |             |
| set  | str  | ❌       |             |

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

result = sdk.formulas.get(
    key="key",
    set="set"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## set

Remove all previous values for specified 'key' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/formulas/actual/set`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| key   | str  | ✅       |             |
| value | str  | ❌       |             |
| set   | str  | ❌       |             |

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

result = sdk.formulas.set(
    key="key",
    value="value",
    set="set"
)

print(result)
```

## add

Add a new value for specified 'key'

- HTTP Method: `PUT`
- Endpoint: `/formulas/actual/add`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| key   | str  | ✅       |             |
| value | str  | ❌       |             |
| set   | str  | ❌       |             |

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

result = sdk.formulas.add(
    key="key",
    value="value",
    set="set"
)

print(result)
```

## all

Obtain a list of all formulas with specified 'key'

- HTTP Method: `GET`
- Endpoint: `/formulas/all/get`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| key  | str  | ❌       |             |
| set  | str  | ❌       |             |

**Return Type**

`List[Formula]`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.formulas.all(
    key="key",
    set="set"
)

print(result)
```

## update

Remove previously set and add new formulas with specified 'key' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/formulas/all/update`

**Parameters**

| Name         | Type                                  | Required | Description       |
| :----------- | :------------------------------------ | :------- | :---------------- |
| request_body | [List[Formula]](../models/Formula.md) | ✅       | The request body. |
| set          | str                                   | ❌       |                   |

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

result = sdk.formulas.update(
    request_body=request_body,
    set="set"
)

print(result)
```

## remove

Remove all values for specified 'key'

- HTTP Method: `DELETE`
- Endpoint: `/formulas/all/remove`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| key   | str  | ✅       |             |
| value | str  | ❌       |             |
| set   | str  | ❌       |             |

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

result = sdk.formulas.remove(
    key="key",
    value="value",
    set="set"
)

print(result)
```

## display

Display a list of all formulas with specified 'key'

- HTTP Method: `GET`
- Endpoint: `/formulas/all/display`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| key    | str  | ❌       |             |
| set    | str  | ❌       |             |
| format | str  | ❌       |             |

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

result = sdk.formulas.display(
    key="key",
    set="set",
    format="format"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
