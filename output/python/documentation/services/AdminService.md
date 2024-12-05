# AdminService

A list of all methods in the `AdminService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description |
| :------------------------------------------------------------------ | :---------- |
| [get_projects_admin_projects_get](#get_projects_admin_projects_get) |             |

## get_projects_admin_projects_get

- HTTP Method: `GET`
- Endpoint: `/admin/projects`

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from web_oto_dev_sdk import WebOtoDevSdk

sdk = WebOtoDevSdk(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)

result = sdk.admin.get_projects_admin_projects_get()

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->