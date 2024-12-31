# MeaningsService

A list of all methods in the `MeaningsService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                               |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------ |
| [new\_](#new_)      | Create new collection (default or specified settings)                                                                     |
| [get\_](#get_)      | Obtain the lastest value for meaning with specified 'name'                                                                |
| [set\_](#set_)      | Remove all previous values for specified 'name' and add a new value                                                       |
| [add](#add)         | Add a new value for specified 'name'                                                                                      |
| [all](#all)         | Obtain a list of all meanings with specified 'name'                                                                       |
| [update](#update)   | Remove previously set and add new meanings with specified 'name' fileds with values from 'values' fileds of provided list |
| [remove](#remove)   | Remove all values for specified 'name'                                                                                    |
| [display](#display) | Display a list of all meanings with specified 'name'                                                                      |

## new\_

Create new collection (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/meanings/revision/new`

**Parameters**

| Name       | Type   | Required | Description |
| :--------- | :----- | :------- | :---------- |
| init       | string | ❌       |             |
| collection | string | ❌       |             |

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

  const { data } = await webOtoDevSdk.meanings.new_({
    init: 'init',
    collection: 'collection',
  });

  console.log(data);
})();
```

## get\_

Obtain the lastest value for meaning with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/meanings/actual/get`

**Parameters**

| Name       | Type   | Required | Description |
| :--------- | :----- | :------- | :---------- |
| name       | string | ✅       |             |
| collection | string | ❌       |             |

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

  const { data } = await webOtoDevSdk.meanings.get_({
    name: 'name',
    collection: 'collection',
  });

  console.log(data);
})();
```

## set\_

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/meanings/actual/set`

**Parameters**

| Name       | Type   | Required | Description |
| :--------- | :----- | :------- | :---------- |
| name       | string | ✅       |             |
| value      | string | ❌       |             |
| collection | string | ❌       |             |

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

  const { data } = await webOtoDevSdk.meanings.set_({
    name: 'name',
    value: 'value',
    collection: 'collection',
  });

  console.log(data);
})();
```

## add

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/meanings/actual/add`

**Parameters**

| Name       | Type   | Required | Description |
| :--------- | :----- | :------- | :---------- |
| name       | string | ✅       |             |
| value      | string | ❌       |             |
| collection | string | ❌       |             |

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

  const { data } = await webOtoDevSdk.meanings.add({
    name: 'name',
    value: 'value',
    collection: 'collection',
  });

  console.log(data);
})();
```

## all

Obtain a list of all meanings with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/meanings/all/get`

**Parameters**

| Name       | Type   | Required | Description |
| :--------- | :----- | :------- | :---------- |
| name       | string | ❌       |             |
| collection | string | ❌       |             |

**Return Type**

`Meaning[]`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
    projectId: 'my-project-slug-or-uid',
  });

  const { data } = await webOtoDevSdk.meanings.all({
    name: 'name',
    collection: 'collection',
  });

  console.log(data);
})();
```

## update

Remove previously set and add new meanings with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/meanings/all/update`

**Parameters**

| Name       | Type                              | Required | Description       |
| :--------- | :-------------------------------- | :------- | :---------------- |
| body       | [Meaning[]](../models/Meaning.md) | ✅       | The request body. |
| collection | string                            | ❌       |                   |

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

  const { data } = await webOtoDevSdk.meanings.update({
    collection: 'collection',
  });

  console.log(data);
})();
```

## remove

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/meanings/all/remove`

**Parameters**

| Name       | Type   | Required | Description |
| :--------- | :----- | :------- | :---------- |
| name       | string | ❌       |             |
| value      | string | ❌       |             |
| collection | string | ❌       |             |

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

  const { data } = await webOtoDevSdk.meanings.remove({
    name: 'name',
    value: 'value',
    collection: 'collection',
  });

  console.log(data);
})();
```

## display

Display a list of all meanings with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/meanings/all/display`

**Parameters**

| Name       | Type   | Required | Description |
| :--------- | :----- | :------- | :---------- |
| name       | string | ❌       |             |
| collection | string | ❌       |             |
| format     | string | ❌       |             |

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

  const { data } = await webOtoDevSdk.meanings.display({
    name: 'name',
    collection: 'collection',
    format: 'format',
  });

  console.log(data);
})();
```

<!-- This file was generated by liblab | https://liblab.com/ -->
