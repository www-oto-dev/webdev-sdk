# ProjectService

A list of all methods in the `ProjectService` service. Click on the method name to view detailed information about that method.

| Methods                   | Description                |
| :------------------------ | :------------------------- |
| [info](#info)             | Obtain project information |
| [collect](#collect)       | collect                    |
| [generate](#generate)     | generate                   |
| [build](#build)           | build                      |
| [view](#view)             | view                       |
| [imagine](#imagine)       | imagine                    |
| [info_1](#info_1)         | Obtain project information |
| [collect_1](#collect_1)   | collect                    |
| [generate_1](#generate_1) | generate                   |
| [build_1](#build_1)       | build                      |
| [view_1](#view_1)         | view                       |
| [imagine_1](#imagine_1)   | imagine                    |

## info

Obtain project information

- HTTP Method: `GET`
- Endpoint: `/api/v1/project/info`

**Return Type**

`ProjectInfo`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.info()

print(result)
```

## collect

collect

- HTTP Method: `POST`
- Endpoint: `/api/v1/project/collect`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.collect()

print(result)
```

## generate

generate

- HTTP Method: `POST`
- Endpoint: `/api/v1/project/generate`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.generate()

print(result)
```

## build

build

- HTTP Method: `POST`
- Endpoint: `/api/v1/project/build`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.build()

print(result)
```

## view

view

- HTTP Method: `POST`
- Endpoint: `/api/v1/project/view`

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

result = sdk.project.view()

with open("output-file.ext", "w") as f:
    f.write(result)
```

## imagine

imagine

- HTTP Method: `POST`
- Endpoint: `/api/v1/project/imagine`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| target | str  | ❌       |             |

**Return Type**

`HttpValidationError`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.imagine(target="target")

print(result)
```

## info_1

Obtain project information

- HTTP Method: `GET`
- Endpoint: `/api/v1/api/v1/project/info`

**Return Type**

`ProjectInfo`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.info_1()

print(result)
```

## collect_1

collect

- HTTP Method: `POST`
- Endpoint: `/api/v1/api/v1/project/collect`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.collect_1()

print(result)
```

## generate_1

generate

- HTTP Method: `POST`
- Endpoint: `/api/v1/api/v1/project/generate`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.generate_1()

print(result)
```

## build_1

build

- HTTP Method: `POST`
- Endpoint: `/api/v1/api/v1/project/build`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.build_1()

print(result)
```

## view_1

view

- HTTP Method: `POST`
- Endpoint: `/api/v1/api/v1/project/view`

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

result = sdk.project.view_1()

with open("output-file.ext", "w") as f:
    f.write(result)
```

## imagine_1

imagine

- HTTP Method: `POST`
- Endpoint: `/api/v1/api/v1/project/imagine`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| target | str  | ❌       |             |

**Return Type**

`HttpValidationError`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.imagine_1(target="target")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
