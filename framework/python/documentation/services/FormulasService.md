# FormulasService

A list of all methods in the `FormulasService` service. Click on the method name to view detailed information about that method.

| Methods                     | Description                                                                                                               |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| [new](#new)                 | Create new set (default or specified settings)                                                                            |
| [get](#get)                 | Obtain the lastest value for formula with specified 'name'                                                                |
| [set](#set)                 | Remove all previous values for specified 'name' and add a new value                                                       |
| [add](#add)                 | Add a new value for specified 'name'                                                                                      |
| [all](#all)                 | Obtain a list of all formulas with specified 'name'                                                                       |
| [update](#update)           | Remove previously set and add new formulas with specified 'name' fileds with values from 'values' fileds of provided list |
| [remove](#remove)           | Remove all values for specified 'name'                                                                                    |
| [display](#display)         | Display a list of all formulas with specified 'name'                                                                      |
| [revisions](#revisions)     | List of all avaliable revisions (aka 'set')                                                                               |
| [new_1](#new_1)             | Create new set (default or specified settings)                                                                            |
| [get_1](#get_1)             | Obtain the lastest value for formula with specified 'name'                                                                |
| [set_1](#set_1)             | Remove all previous values for specified 'name' and add a new value                                                       |
| [add_1](#add_1)             | Add a new value for specified 'name'                                                                                      |
| [all_1](#all_1)             | Obtain a list of all formulas with specified 'name'                                                                       |
| [update_1](#update_1)       | Remove previously set and add new formulas with specified 'name' fileds with values from 'values' fileds of provided list |
| [remove_1](#remove_1)       | Remove all values for specified 'name'                                                                                    |
| [display_1](#display_1)     | Display a list of all formulas with specified 'name'                                                                      |
| [revisions_1](#revisions_1) | List of all avaliable revisions (aka 'set')                                                                               |

## new

Create new set (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/api/v1/formulas/revision/new`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| init | str  | ❌       |             |
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

result = sdk.formulas.new(
    init="init",
    set="set"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get

Obtain the lastest value for formula with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/formulas/actual/get`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| name | str  | ✅       |             |
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
    name="name",
    set="set"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## set

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/api/v1/formulas/actual/set`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| name   | str  | ✅       |             |
| value  | str  | ❌       |             |
| form   | str  | ❌       |             |
| engine | str  | ❌       |             |
| set    | str  | ❌       |             |

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
    name="name",
    value="value",
    form="form",
    engine="engine",
    set="set"
)

print(result)
```

## add

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/api/v1/formulas/actual/add`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| name   | str  | ✅       |             |
| value  | str  | ❌       |             |
| form   | str  | ❌       |             |
| engine | str  | ❌       |             |
| set    | str  | ❌       |             |

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
    name="name",
    value="value",
    form="form",
    engine="engine",
    set="set"
)

print(result)
```

## all

Obtain a list of all formulas with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/formulas/all/get`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| name | str  | ❌       |             |
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
    name="name",
    set="set"
)

print(result)
```

## update

Remove previously set and add new formulas with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/api/v1/formulas/all/update`

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
        "name": "name",
        "value": "value",
        "form": "form",
        "engine": "engine"
    }
]

result = sdk.formulas.update(
    request_body=request_body,
    set="set"
)

print(result)
```

## remove

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/formulas/all/remove`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ❌       |             |
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
    name="name",
    value="value",
    set="set"
)

print(result)
```

## display

Display a list of all formulas with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/formulas/all/display`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| name   | str  | ❌       |             |
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
    name="name",
    set="set",
    format="format"
)

print(result)
```

## revisions

List of all avaliable revisions (aka 'set')

- HTTP Method: `GET`
- Endpoint: `/api/v1/formulas/rev/list`

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

result = sdk.formulas.revisions()

print(result)
```

## new_1

Create new set (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/formulas/revision/new`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| init | str  | ❌       |             |
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

result = sdk.formulas.new_1(
    init="init",
    set="set"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_1

Obtain the lastest value for formula with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/formulas/actual/get`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| name | str  | ✅       |             |
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

result = sdk.formulas.get_1(
    name="name",
    set="set"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## set_1

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/formulas/actual/set`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| name   | str  | ✅       |             |
| value  | str  | ❌       |             |
| form   | str  | ❌       |             |
| engine | str  | ❌       |             |
| set    | str  | ❌       |             |

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

result = sdk.formulas.set_1(
    name="name",
    value="value",
    form="form",
    engine="engine",
    set="set"
)

print(result)
```

## add_1

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/formulas/actual/add`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| name   | str  | ✅       |             |
| value  | str  | ❌       |             |
| form   | str  | ❌       |             |
| engine | str  | ❌       |             |
| set    | str  | ❌       |             |

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

result = sdk.formulas.add_1(
    name="name",
    value="value",
    form="form",
    engine="engine",
    set="set"
)

print(result)
```

## all_1

Obtain a list of all formulas with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/formulas/all/get`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| name | str  | ❌       |             |
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

result = sdk.formulas.all_1(
    name="name",
    set="set"
)

print(result)
```

## update_1

Remove previously set and add new formulas with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/formulas/all/update`

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
        "name": "name",
        "value": "value",
        "form": "form",
        "engine": "engine"
    }
]

result = sdk.formulas.update_1(
    request_body=request_body,
    set="set"
)

print(result)
```

## remove_1

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/api/v1/formulas/all/remove`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ❌       |             |
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

result = sdk.formulas.remove_1(
    name="name",
    value="value",
    set="set"
)

print(result)
```

## display_1

Display a list of all formulas with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/formulas/all/display`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| name   | str  | ❌       |             |
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

result = sdk.formulas.display_1(
    name="name",
    set="set",
    format="format"
)

print(result)
```

## revisions_1

List of all avaliable revisions (aka 'set')

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/formulas/rev/list`

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

result = sdk.formulas.revisions_1()

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
