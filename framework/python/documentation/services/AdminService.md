# AdminService

A list of all methods in the `AdminService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                              |
| :-------------------------------------------- | :------------------------------------------------------- |
| [projects](#projects)                         | Obtain a list of all projects [ADMIN RIGHTS REQUIRED]    |
| [new_project](#new_project)                   | Create project [ADMIN RIGHTS REQUIRED]                   |
| [remove_project](#remove_project)             | Remove project with specified ID [ADMIN RIGHTS REQUIRED] |
| [change_project](#change_project)             | Change options [ADMIN RIGHTS REQUIRED]                   |
| [change_project_slug](#change_project_slug)   | Change project slug [ADMIN RIGHTS REQUIRED]              |
| [change_project_title](#change_project_title) | Change project title [ADMIN RIGHTS REQUIRED]             |

## projects

Obtain a list of all projects [ADMIN RIGHTS REQUIRED]

- HTTP Method: `GET`
- Endpoint: `/api/v1/admin/projects/all`

**Return Type**

`List[Project]`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.admin.projects()

print(result)
```

## new_project

Create project [ADMIN RIGHTS REQUIRED]

- HTTP Method: `PUT`
- Endpoint: `/api/v1/admin/projects/new`

**Parameters**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| title    | str  | ❌       |             |
| slug     | str  | ❌       |             |
| init     | str  | ❌       |             |
| internal | bool | ❌       |             |

**Return Type**

`bool`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.admin.new_project(
    title="title",
    slug="slug",
    init="init",
    internal=False
)

print(result)
```

## remove_project

Remove project with specified ID [ADMIN RIGHTS REQUIRED]

- HTTP Method: `DELETE`
- Endpoint: `/api/v1/admin/projects/remove`

**Parameters**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| slug     | str  | ❌       |             |
| uid      | str  | ❌       |             |
| internal | bool | ❌       |             |

**Return Type**

`bool`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.admin.remove_project(
    slug="slug",
    uid="uid",
    internal=True
)

print(result)
```

## change_project

Change options [ADMIN RIGHTS REQUIRED]

- HTTP Method: `PUT`
- Endpoint: `/api/v1/admin/projects/change`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| slug      | str  | ❌       |             |
| uid       | str  | ❌       |             |
| new_slug  | str  | ❌       |             |
| new_title | str  | ❌       |             |
| internal  | bool | ❌       |             |

**Return Type**

`bool`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.admin.change_project(
    slug="slug",
    uid="uid",
    new_slug="new_slug",
    new_title="new_title",
    internal=True
)

print(result)
```

## change_project_slug

Change project slug [ADMIN RIGHTS REQUIRED]

- HTTP Method: `PUT`
- Endpoint: `/api/v1/admin/projects/change/slug`

**Parameters**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| slug     | str  | ❌       |             |
| uid      | str  | ❌       |             |
| new_slug | str  | ❌       |             |
| internal | bool | ❌       |             |

**Return Type**

`bool`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.admin.change_project_slug(
    slug="slug",
    uid="uid",
    new_slug="new_slug",
    internal=False
)

print(result)
```

## change_project_title

Change project title [ADMIN RIGHTS REQUIRED]

- HTTP Method: `PUT`
- Endpoint: `/api/v1/admin/projects/change/title`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| slug      | str  | ❌       |             |
| uid       | str  | ❌       |             |
| new_title | str  | ❌       |             |
| internal  | bool | ❌       |             |

**Return Type**

`bool`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    project_id="my-project-slug-or-uid",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.admin.change_project_title(
    slug="slug",
    uid="uid",
    new_title="new_title",
    internal=False
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
