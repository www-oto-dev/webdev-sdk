# ProjectService

A list of all methods in the `ProjectService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                                       | Description |
| :-------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| [read_project_properties_project_project_slug_properties_get](#read_project_properties_project_project_slug_properties_get)                   |             |
| [create_project_property_project_project_slug_properties_post](#create_project_property_project_project_slug_properties_post)                 |             |
| [get_property_project_project_slug_properties_property_slug_get](#get_property_project_project_slug_properties_property_slug_get)             |             |
| [update_property_project_project_slug_properties_property_slug_put](#update_property_project_project_slug_properties_property_slug_put)       |             |
| [delete_property_project_project_slug_properties_property_slug_delete](#delete_property_project_project_slug_properties_property_slug_delete) |             |

## read_project_properties_project_project_slug_properties_get

- HTTP Method: `GET`
- Endpoint: `/project/{project_slug}/properties/`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| project_slug | str  | ✅       |             |

**Return Type**

`List[Property]`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.read_project_properties_project_project_slug_properties_get(project_slug="project_slug")

print(result)
```

## create_project_property_project_project_slug_properties_post

- HTTP Method: `POST`
- Endpoint: `/project/{project_slug}/properties/`

**Parameters**

| Name         | Type                                          | Required | Description       |
| :----------- | :-------------------------------------------- | :------- | :---------------- |
| request_body | [PropertyCreate](../models/PropertyCreate.md) | ✅       | The request body. |
| project_slug | str                                           | ✅       |                   |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk
from web_oto_dev_sdk.models import PropertyCreate

sdk = WebOtoDevSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = PropertyCreate(
    key="key",
    value="value"
)

result = sdk.project.create_project_property_project_project_slug_properties_post(
    request_body=request_body,
    project_slug="project_slug"
)

print(result)
```

## get_property_project_project_slug_properties_property_slug_get

- HTTP Method: `GET`
- Endpoint: `/project/{project_slug}/properties/{property_slug}`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| project_slug | str  | ✅       |             |

**Return Type**

`List[Property]`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.get_property_project_project_slug_properties_property_slug_get(project_slug="project_slug")

print(result)
```

## update_property_project_project_slug_properties_property_slug_put

- HTTP Method: `PUT`
- Endpoint: `/project/{project_slug}/properties/{property_slug}`

**Parameters**

| Name          | Type                                          | Required | Description       |
| :------------ | :-------------------------------------------- | :------- | :---------------- |
| request_body  | [PropertyUpdate](../models/PropertyUpdate.md) | ✅       | The request body. |
| project_slug  | str                                           | ✅       |                   |
| property_slug | str                                           | ✅       |                   |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk
from web_oto_dev_sdk.models import PropertyUpdate

sdk = WebOtoDevSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

request_body = PropertyUpdate(
    key="key",
    value="value"
)

result = sdk.project.update_property_project_project_slug_properties_property_slug_put(
    request_body=request_body,
    project_slug="project_slug",
    property_slug="property_slug"
)

print(result)
```

## delete_property_project_project_slug_properties_property_slug_delete

- HTTP Method: `DELETE`
- Endpoint: `/project/{project_slug}/properties/{property_slug}`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| project_slug  | str  | ✅       |             |
| property_slug | str  | ✅       |             |

**Return Type**

`Property`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.project.delete_property_project_project_slug_properties_property_slug_delete(
    project_slug="project_slug",
    property_slug="property_slug"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
