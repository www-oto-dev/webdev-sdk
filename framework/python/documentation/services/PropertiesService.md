# PropertiesService

A list of all methods in the `PropertiesService` service. Click on the method name to view detailed information about that method.

| Methods                     | Description                                                                                                                 |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| [new](#new)                 | Create new build (default or specified settings)                                                                            |
| [get](#get)                 | Obtain the lastest value for formula with specified 'name'                                                                  |
| [set](#set)                 | Remove all previous values for specified 'name' and add a new value                                                         |
| [add](#add)                 | Add a new value for specified 'name'                                                                                        |
| [all](#all)                 | Obtain a list of all properties with specified 'name'                                                                       |
| [update](#update)           | Remove previously set and add new properties with specified 'name' fileds with values from 'values' fileds of provided list |
| [remove](#remove)           | Remove all values for specified 'name'                                                                                      |
| [display](#display)         | Display a list of all properties with specified 'name'                                                                      |
| [revisions](#revisions)     | List of all avaliable revisions (aka 'build')                                                                               |
| [new_1](#new_1)             | Create new build (default or specified settings)                                                                            |
| [get_1](#get_1)             | Obtain the lastest value for formula with specified 'name'                                                                  |
| [set_1](#set_1)             | Remove all previous values for specified 'name' and add a new value                                                         |
| [add_1](#add_1)             | Add a new value for specified 'name'                                                                                        |
| [all_1](#all_1)             | Obtain a list of all properties with specified 'name'                                                                       |
| [update_1](#update_1)       | Remove previously set and add new properties with specified 'name' fileds with values from 'values' fileds of provided list |
| [remove_1](#remove_1)       | Remove all values for specified 'name'                                                                                      |
| [display_1](#display_1)     | Display a list of all properties with specified 'name'                                                                      |
| [revisions_1](#revisions_1) | List of all avaliable revisions (aka 'build')                                                                               |

## new

Create new build (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/api/v1/properties/revision/new`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| init  | str  | ❌       |             |
| build | str  | ❌       |             |

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

result = sdk.properties.new(
    init="init",
    build="build"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get

Obtain the lastest value for formula with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/properties/actual/get`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ✅       |             |
| build | str  | ❌       |             |

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

result = sdk.properties.get(
    name="name",
    build="build"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## set

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/api/v1/properties/actual/set`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ✅       |             |
| value | str  | ❌       |             |
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

result = sdk.properties.set(
    name="name",
    value="value",
    build="build"
)

print(result)
```

## add

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/api/v1/properties/actual/add`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ✅       |             |
| value | str  | ❌       |             |
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

result = sdk.properties.add(
    name="name",
    value="value",
    build="build"
)

print(result)
```

## all

Obtain a list of all properties with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/properties/all/get`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ❌       |             |
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
    name="name",
    build="build"
)

print(result)
```

## update

Remove previously set and add new properties with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/api/v1/properties/all/update`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [List[Property]](../models/Property.md) | ✅       | The request body. |
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
        "name": "name",
        "value": "value"
    }
]

result = sdk.properties.update(
    request_body=request_body,
    build="build"
)

print(result)
```

## remove

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/properties/all/remove`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ❌       |             |
| value | str  | ❌       |             |
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
    name="name",
    value="value",
    build="build"
)

print(result)
```

## display

Display a list of all properties with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/properties/all/display`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| name   | str  | ❌       |             |
| build  | str  | ❌       |             |
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

result = sdk.properties.display(
    name="name",
    build="build",
    format="format"
)

print(result)
```

## revisions

List of all avaliable revisions (aka 'build')

- HTTP Method: `GET`
- Endpoint: `/api/v1/properties/rev/list`

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

result = sdk.properties.revisions()

print(result)
```

## new_1

Create new build (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/properties/revision/new`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| init  | str  | ❌       |             |
| build | str  | ❌       |             |

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

result = sdk.properties.new_1(
    init="init",
    build="build"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_1

Obtain the lastest value for formula with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/properties/actual/get`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ✅       |             |
| build | str  | ❌       |             |

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

result = sdk.properties.get_1(
    name="name",
    build="build"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## set_1

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/properties/actual/set`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ✅       |             |
| value | str  | ❌       |             |
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

result = sdk.properties.set_1(
    name="name",
    value="value",
    build="build"
)

print(result)
```

## add_1

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/properties/actual/add`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ✅       |             |
| value | str  | ❌       |             |
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

result = sdk.properties.add_1(
    name="name",
    value="value",
    build="build"
)

print(result)
```

## all_1

Obtain a list of all properties with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/properties/all/get`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ❌       |             |
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

result = sdk.properties.all_1(
    name="name",
    build="build"
)

print(result)
```

## update_1

Remove previously set and add new properties with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/properties/all/update`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [List[Property]](../models/Property.md) | ✅       | The request body. |
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
        "name": "name",
        "value": "value"
    }
]

result = sdk.properties.update_1(
    request_body=request_body,
    build="build"
)

print(result)
```

## remove_1

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/api/v1/properties/all/remove`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| name  | str  | ❌       |             |
| value | str  | ❌       |             |
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

result = sdk.properties.remove_1(
    name="name",
    value="value",
    build="build"
)

print(result)
```

## display_1

Display a list of all properties with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/properties/all/display`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| name   | str  | ❌       |             |
| build  | str  | ❌       |             |
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

result = sdk.properties.display_1(
    name="name",
    build="build",
    format="format"
)

print(result)
```

## revisions_1

List of all avaliable revisions (aka 'build')

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/properties/rev/list`

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

result = sdk.properties.revisions_1()

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
