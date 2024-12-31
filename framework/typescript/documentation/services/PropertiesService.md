# PropertiesService

A list of all methods in the `PropertiesService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                                 |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------------- |
| [new\_](#new_)      | Create new build (default or specified settings)                                                                            |
| [get\_](#get_)      | Obtain the lastest value for formula with specified 'name'                                                                  |
| [set\_](#set_)      | Remove all previous values for specified 'name' and add a new value                                                         |
| [add](#add)         | Add a new value for specified 'name'                                                                                        |
| [all](#all)         | Obtain a list of all properties with specified 'name'                                                                       |
| [update](#update)   | Remove previously set and add new properties with specified 'name' fileds with values from 'values' fileds of provided list |
| [remove](#remove)   | Remove all values for specified 'name'                                                                                      |
| [display](#display) | Display a list of all properties with specified 'name'                                                                      |

## new\_

Create new build (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/properties/revision/new`

**Parameters**

| Name  | Type   | Required | Description |
| :---- | :----- | :------- | :---------- |
| init  | string | ❌       |             |
| build | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.properties.new_({
    init: 'init',
    build: 'build',
  });

  console.log(data);
})();
```

## get\_

Obtain the lastest value for formula with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/properties/actual/get`

**Parameters**

| Name  | Type   | Required | Description |
| :---- | :----- | :------- | :---------- |
| name  | string | ✅       |             |
| build | string | ❌       |             |

**Return Type**

`string`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.properties.get_({
    name: 'name',
    build: 'build',
  });

  console.log(data);
})();
```

## set\_

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/properties/actual/set`

**Parameters**

| Name  | Type   | Required | Description |
| :---- | :----- | :------- | :---------- |
| name  | string | ✅       |             |
| value | string | ❌       |             |
| build | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.properties.set_({
    name: 'name',
    value: 'value',
    build: 'build',
  });

  console.log(data);
})();
```

## add

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/properties/actual/add`

**Parameters**

| Name  | Type   | Required | Description |
| :---- | :----- | :------- | :---------- |
| name  | string | ✅       |             |
| value | string | ❌       |             |
| build | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.properties.add({
    name: 'name',
    value: 'value',
    build: 'build',
  });

  console.log(data);
})();
```

## all

Obtain a list of all properties with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/properties/all/get`

**Parameters**

| Name  | Type   | Required | Description |
| :---- | :----- | :------- | :---------- |
| name  | string | ❌       |             |
| build | string | ❌       |             |

**Return Type**

`Property[]`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.properties.all({
    name: 'name',
    build: 'build',
  });

  console.log(data);
})();
```

## update

Remove previously set and add new properties with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/properties/all/update`

**Parameters**

| Name  | Type                                | Required | Description       |
| :---- | :---------------------------------- | :------- | :---------------- |
| body  | [Property[]](../models/Property.md) | ✅       | The request body. |
| build | string                              | ❌       |                   |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.properties.update({
    build: 'build',
  });

  console.log(data);
})();
```

## remove

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/properties/all/remove`

**Parameters**

| Name  | Type   | Required | Description |
| :---- | :----- | :------- | :---------- |
| name  | string | ❌       |             |
| value | string | ❌       |             |
| build | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.properties.remove({
    name: 'name',
    value: 'value',
    build: 'build',
  });

  console.log(data);
})();
```

## display

Display a list of all properties with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/properties/all/display`

**Parameters**

| Name   | Type   | Required | Description |
| :----- | :----- | :------- | :---------- |
| name   | string | ❌       |             |
| build  | string | ❌       |             |
| format | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.properties.display({
    name: 'name',
    build: 'build',
    format: 'format',
  });

  console.log(data);
})();
```

<!-- This file was generated by liblab | https://liblab.com/ -->
