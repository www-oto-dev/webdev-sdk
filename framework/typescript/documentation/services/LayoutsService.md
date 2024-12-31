# LayoutsService

A list of all methods in the `LayoutsService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                                |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------- |
| [new\_](#new_)      | Create new version (default or specified settings)                                                                         |
| [get\_](#get_)      | Obtain the lastest layout for page with specified 'name'                                                                   |
| [set\_](#set_)      | Remove all previous layouts for specified page with 'name' and add a new value                                             |
| [add](#add)         | Add a new value for specified page by 'name'                                                                               |
| [all](#all)         | Obtain a list of all layouts with specified 'name'                                                                         |
| [update](#update)   | Remove previously set and add new layouts with specified 'name' fileds with layouts from 'layouts' fileds of provided list |
| [remove](#remove)   | Remove all layouts for specified 'name'                                                                                    |
| [display](#display) | Display a list of all layouts with specified 'name'                                                                        |

## new\_

Create new version (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/layouts/revision/new`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| init    | string | ❌       |             |
| version | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
    projectId: 'my-project-slug-or-uid',
  });

  const { data } = await webOtoDevSdk.layouts.new_({
    init: 'init',
    version: 'version',
  });

  console.log(data);
})();
```

## get\_

Obtain the lastest layout for page with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/layouts/actual/get`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| name    | string | ✅       |             |
| version | string | ❌       |             |

**Return Type**

`string`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
    projectId: 'my-project-slug-or-uid',
  });

  const { data } = await webOtoDevSdk.layouts.get_({
    name: 'name',
    version: 'version',
  });

  console.log(data);
})();
```

## set\_

Remove all previous layouts for specified page with 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/layouts/actual/set`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| name    | string | ✅       |             |
| value   | string | ❌       |             |
| version | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
    projectId: 'my-project-slug-or-uid',
  });

  const { data } = await webOtoDevSdk.layouts.set_({
    name: 'name',
    value: 'value',
    version: 'version',
  });

  console.log(data);
})();
```

## add

Add a new value for specified page by 'name'

- HTTP Method: `PUT`
- Endpoint: `/layouts/actual/add`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| name    | string | ✅       |             |
| value   | string | ❌       |             |
| version | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
    projectId: 'my-project-slug-or-uid',
  });

  const { data } = await webOtoDevSdk.layouts.add({
    name: 'name',
    value: 'value',
    version: 'version',
  });

  console.log(data);
})();
```

## all

Obtain a list of all layouts with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/layouts/all/get`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| name    | string | ❌       |             |
| version | string | ❌       |             |

**Return Type**

`Value[]`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
    projectId: 'my-project-slug-or-uid',
  });

  const { data } = await webOtoDevSdk.layouts.all({
    name: 'name',
    version: 'version',
  });

  console.log(data);
})();
```

## update

Remove previously set and add new layouts with specified 'name' fileds with layouts from 'layouts' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/layouts/all/update`

**Parameters**

| Name    | Type                          | Required | Description       |
| :------ | :---------------------------- | :------- | :---------------- |
| body    | [Value[]](../models/Value.md) | ✅       | The request body. |
| version | string                        | ❌       |                   |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
    projectId: 'my-project-slug-or-uid',
  });

  const { data } = await webOtoDevSdk.layouts.update({
    version: 'version',
  });

  console.log(data);
})();
```

## remove

Remove all layouts for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/layouts/all/remove`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| name    | string | ❌       |             |
| value   | string | ❌       |             |
| version | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
    projectId: 'my-project-slug-or-uid',
  });

  const { data } = await webOtoDevSdk.layouts.remove({
    name: 'name',
    value: 'value',
    version: 'version',
  });

  console.log(data);
})();
```

## display

Display a list of all layouts with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/layouts/all/display`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| name    | string | ❌       |             |
| version | string | ❌       |             |
| format  | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
    projectId: 'my-project-slug-or-uid',
  });

  const { data } = await webOtoDevSdk.layouts.display({
    name: 'name',
    version: 'version',
    format: 'format',
  });

  console.log(data);
})();
```

<!-- This file was generated by liblab | https://liblab.com/ -->
