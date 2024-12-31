# ValuesService

A list of all methods in the `ValuesService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                             |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------- |
| [new\_](#new_)      | Create new dataset (default or specified settings)                                                                      |
| [get\_](#get_)      | Obtain the lastest value for variable with specified 'name'                                                             |
| [set\_](#set_)      | Remove all previous values for specified 'name' and add a new value                                                     |
| [add](#add)         | Add a new value for specified 'name'                                                                                    |
| [all](#all)         | Obtain a list of all values with specified 'name'                                                                       |
| [update](#update)   | Remove previously set and add new values with specified 'name' fileds with values from 'values' fileds of provided list |
| [remove](#remove)   | Remove all values for specified 'name'                                                                                  |
| [display](#display) | Display a list of all values with specified 'name'                                                                      |

## new\_

Create new dataset (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/values/revision/new`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| init    | string | ❌       |             |
| dataset | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.values.new_({
    init: 'init',
    dataset: 'dataset',
  });

  console.log(data);
})();
```

## get\_

Obtain the lastest value for variable with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/values/actual/get`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| name    | string | ✅       |             |
| dataset | string | ❌       |             |

**Return Type**

`string`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.values.get_({
    name: 'name',
    dataset: 'dataset',
  });

  console.log(data);
})();
```

## set\_

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/values/actual/set`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| name    | string | ✅       |             |
| value   | string | ❌       |             |
| dataset | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.values.set_({
    name: 'name',
    value: 'value',
    dataset: 'dataset',
  });

  console.log(data);
})();
```

## add

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/values/actual/add`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| name    | string | ✅       |             |
| value   | string | ❌       |             |
| dataset | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.values.add({
    name: 'name',
    value: 'value',
    dataset: 'dataset',
  });

  console.log(data);
})();
```

## all

Obtain a list of all values with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/values/all/get`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| name    | string | ❌       |             |
| dataset | string | ❌       |             |

**Return Type**

`Value[]`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.values.all({
    name: 'name',
    dataset: 'dataset',
  });

  console.log(data);
})();
```

## update

Remove previously set and add new values with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/values/all/update`

**Parameters**

| Name    | Type                          | Required | Description       |
| :------ | :---------------------------- | :------- | :---------------- |
| body    | [Value[]](../models/Value.md) | ✅       | The request body. |
| dataset | string                        | ❌       |                   |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.values.update({
    dataset: 'dataset',
  });

  console.log(data);
})();
```

## remove

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/values/all/remove`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| name    | string | ❌       |             |
| value   | string | ❌       |             |
| dataset | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.values.remove({
    name: 'name',
    value: 'value',
    dataset: 'dataset',
  });

  console.log(data);
})();
```

## display

Display a list of all values with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/values/all/display`

**Parameters**

| Name    | Type   | Required | Description |
| :------ | :----- | :------- | :---------- |
| name    | string | ❌       |             |
| dataset | string | ❌       |             |
| format  | string | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.values.display({
    name: 'name',
    dataset: 'dataset',
    format: 'format',
  });

  console.log(data);
})();
```

<!-- This file was generated by liblab | https://liblab.com/ -->
