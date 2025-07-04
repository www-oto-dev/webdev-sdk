# LayoutsService

A list of all methods in the `LayoutsService` service. Click on the method name to view detailed information about that method.

| Methods                     | Description                                                                                                                |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| [new](#new)                 | Create new version (default or specified settings)                                                                         |
| [get](#get)                 | Obtain the lastest layout for page with specified 'name'                                                                   |
| [set](#set)                 | Remove all previous layouts for specified page with 'name' and add a new value                                             |
| [add](#add)                 | Add a new value for specified page by 'name'                                                                               |
| [all](#all)                 | Obtain a list of all layouts with specified 'name'                                                                         |
| [update](#update)           | Remove previously set and add new layouts with specified 'name' fileds with layouts from 'layouts' fileds of provided list |
| [remove](#remove)           | Remove all layouts for specified 'name'                                                                                    |
| [display](#display)         | Display a list of all layouts with specified 'name'                                                                        |
| [revisions](#revisions)     | List of all avaliable revisions (aka 'versions')                                                                           |
| [new_1](#new_1)             | Create new version (default or specified settings)                                                                         |
| [get_1](#get_1)             | Obtain the lastest layout for page with specified 'name'                                                                   |
| [set_1](#set_1)             | Remove all previous layouts for specified page with 'name' and add a new value                                             |
| [add_1](#add_1)             | Add a new value for specified page by 'name'                                                                               |
| [all_1](#all_1)             | Obtain a list of all layouts with specified 'name'                                                                         |
| [update_1](#update_1)       | Remove previously set and add new layouts with specified 'name' fileds with layouts from 'layouts' fileds of provided list |
| [remove_1](#remove_1)       | Remove all layouts for specified 'name'                                                                                    |
| [display_1](#display_1)     | Display a list of all layouts with specified 'name'                                                                        |
| [revisions_1](#revisions_1) | List of all avaliable revisions (aka 'versions')                                                                           |

## new

Create new version (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/api/v1/layouts/revision/new`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| init    | str  | ❌       |             |
| version | str  | ❌       |             |

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

result = sdk.layouts.new(
    init="init",
    version="version"
)

print(result)
```

## get

Obtain the lastest layout for page with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/layouts/actual/get`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ✅       |             |
| version | str  | ❌       |             |

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

result = sdk.layouts.get(
    name="name",
    version="version"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## set

Remove all previous layouts for specified page with 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/api/v1/layouts/actual/set`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ✅       |             |
| value   | str  | ❌       |             |
| version | str  | ❌       |             |

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

result = sdk.layouts.set(
    name="name",
    value="value",
    version="version"
)

print(result)
```

## add

Add a new value for specified page by 'name'

- HTTP Method: `PUT`
- Endpoint: `/api/v1/layouts/actual/add`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ✅       |             |
| value   | str  | ❌       |             |
| version | str  | ❌       |             |

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

result = sdk.layouts.add(
    name="name",
    value="value",
    version="version"
)

print(result)
```

## all

Obtain a list of all layouts with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/layouts/all/get`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ❌       |             |
| version | str  | ❌       |             |

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

result = sdk.layouts.all(
    name="name",
    version="version"
)

print(result)
```

## update

Remove previously set and add new layouts with specified 'name' fileds with layouts from 'layouts' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/api/v1/layouts/all/update`

**Parameters**

| Name         | Type                              | Required | Description       |
| :----------- | :-------------------------------- | :------- | :---------------- |
| request_body | [List[Value]](../models/Value.md) | ✅       | The request body. |
| version      | str                               | ❌       |                   |

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

result = sdk.layouts.update(
    request_body=request_body,
    version="version"
)

print(result)
```

## remove

Remove all layouts for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/layouts/all/remove`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ❌       |             |
| value   | str  | ❌       |             |
| version | str  | ❌       |             |

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

result = sdk.layouts.remove(
    name="name",
    value="value",
    version="version"
)

print(result)
```

## display

Display a list of all layouts with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/layouts/all/display`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ❌       |             |
| version | str  | ❌       |             |
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

result = sdk.layouts.display(
    name="name",
    version="version",
    format="format"
)

print(result)
```

## revisions

List of all avaliable revisions (aka 'versions')

- HTTP Method: `GET`
- Endpoint: `/api/v1/layouts/rev/list`

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

result = sdk.layouts.revisions()

print(result)
```

## new_1

Create new version (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/layouts/revision/new`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| init    | str  | ❌       |             |
| version | str  | ❌       |             |

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

result = sdk.layouts.new_1(
    init="init",
    version="version"
)

print(result)
```

## get_1

Obtain the lastest layout for page with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/layouts/actual/get`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ✅       |             |
| version | str  | ❌       |             |

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

result = sdk.layouts.get_1(
    name="name",
    version="version"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## set_1

Remove all previous layouts for specified page with 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/layouts/actual/set`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ✅       |             |
| value   | str  | ❌       |             |
| version | str  | ❌       |             |

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

result = sdk.layouts.set_1(
    name="name",
    value="value",
    version="version"
)

print(result)
```

## add_1

Add a new value for specified page by 'name'

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/layouts/actual/add`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ✅       |             |
| value   | str  | ❌       |             |
| version | str  | ❌       |             |

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

result = sdk.layouts.add_1(
    name="name",
    value="value",
    version="version"
)

print(result)
```

## all_1

Obtain a list of all layouts with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/layouts/all/get`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ❌       |             |
| version | str  | ❌       |             |

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

result = sdk.layouts.all_1(
    name="name",
    version="version"
)

print(result)
```

## update_1

Remove previously set and add new layouts with specified 'name' fileds with layouts from 'layouts' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/layouts/all/update`

**Parameters**

| Name         | Type                              | Required | Description       |
| :----------- | :-------------------------------- | :------- | :---------------- |
| request_body | [List[Value]](../models/Value.md) | ✅       | The request body. |
| version      | str                               | ❌       |                   |

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

result = sdk.layouts.update_1(
    request_body=request_body,
    version="version"
)

print(result)
```

## remove_1

Remove all layouts for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/api/v1/layouts/all/remove`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ❌       |             |
| value   | str  | ❌       |             |
| version | str  | ❌       |             |

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

result = sdk.layouts.remove_1(
    name="name",
    value="value",
    version="version"
)

print(result)
```

## display_1

Display a list of all layouts with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/layouts/all/display`

**Parameters**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| name    | str  | ❌       |             |
| version | str  | ❌       |             |
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

result = sdk.layouts.display_1(
    name="name",
    version="version",
    format="format"
)

print(result)
```

## revisions_1

List of all avaliable revisions (aka 'versions')

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/layouts/rev/list`

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

result = sdk.layouts.revisions_1()

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
