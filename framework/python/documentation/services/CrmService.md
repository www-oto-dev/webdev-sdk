# CrmService

A list of all methods in the `CrmService` service. Click on the method name to view detailed information about that method.

| Methods               | Description                            |
| :-------------------- | :------------------------------------- |
| [active](#active)     | Returns True if internal CRM is active |
| [active_1](#active_1) | Returns True if internal CRM is active |

## active

Returns True if internal CRM is active

- HTTP Method: `PUT`
- Endpoint: `/api/v1/crm/active`

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

result = sdk.crm.active()

print(result)
```

## active_1

Returns True if internal CRM is active

- HTTP Method: `PUT`
- Endpoint: `/api/v1/api/v1/crm/active`

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

result = sdk.crm.active_1()

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
