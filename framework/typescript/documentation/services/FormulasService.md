# FormulasService

A list of all methods in the `FormulasService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                               |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------ |
| [new\_](#new_)      | Create new set (default or specified settings)                                                                            |
| [get\_](#get_)      | Obtain the lastest value for formula with specified 'name'                                                                |
| [set\_](#set_)      | Remove all previous values for specified 'name' and add a new value                                                       |
| [add](#add)         | Add a new value for specified 'name'                                                                                      |
| [all](#all)         | Obtain a list of all formulas with specified 'name'                                                                       |
| [update](#update)   | Remove previously set and add new formulas with specified 'name' fileds with values from 'values' fileds of provided list |
| [remove](#remove)   | Remove all values for specified 'name'                                                                                    |
| [display](#display) | Display a list of all formulas with specified 'name'                                                                      |

## new\_

Create new set (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/formulas/revision/new`

**Parameters**

| Name | Type   | Required | Description |
| :--- | :----- | :------- | :---------- |
| init | string | ❌       |             |
| set  | string | ❌       |             |

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

  const { data } = await webOtoDevSdk.formulas.new_({
    init: 'init',
    set: 'set',
  });

  console.log(data);
})();
```

## get\_

Obtain the lastest value for formula with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/formulas/actual/get`

**Parameters**

| Name | Type   | Required | Description |
| :--- | :----- | :------- | :---------- |
| name | string | ✅       |             |
| set  | string | ❌       |             |

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

  const { data } = await webOtoDevSdk.formulas.get_({
    name: 'name',
    set: 'set',
  });

  console.log(data);
})();
```

## set\_

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/formulas/actual/set`

**Parameters**

| Name   | Type   | Required | Description |
| :----- | :----- | :------- | :---------- |
| name   | string | ✅       |             |
| value  | string | ❌       |             |
| form   | string | ❌       |             |
| engine | string | ❌       |             |
| set    | string | ❌       |             |

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

  const { data } = await webOtoDevSdk.formulas.set_({
    name: 'name',
    value: 'value',
    form: 'form',
    engine: 'engine',
    set: 'set',
  });

  console.log(data);
})();
```

## add

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/formulas/actual/add`

**Parameters**

| Name   | Type   | Required | Description |
| :----- | :----- | :------- | :---------- |
| name   | string | ✅       |             |
| value  | string | ❌       |             |
| form   | string | ❌       |             |
| engine | string | ❌       |             |
| set    | string | ❌       |             |

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

  const { data } = await webOtoDevSdk.formulas.add({
    name: 'name',
    value: 'value',
    form: 'form',
    engine: 'engine',
    set: 'set',
  });

  console.log(data);
})();
```

## all

Obtain a list of all formulas with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/formulas/all/get`

**Parameters**

| Name | Type   | Required | Description |
| :--- | :----- | :------- | :---------- |
| name | string | ❌       |             |
| set  | string | ❌       |             |

**Return Type**

`Formula[]`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
    projectId: 'my-project-slug-or-uid',
  });

  const { data } = await webOtoDevSdk.formulas.all({
    name: 'name',
    set: 'set',
  });

  console.log(data);
})();
```

## update

Remove previously set and add new formulas with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/formulas/all/update`

**Parameters**

| Name | Type                              | Required | Description       |
| :--- | :-------------------------------- | :------- | :---------------- |
| body | [Formula[]](../models/Formula.md) | ✅       | The request body. |
| set  | string                            | ❌       |                   |

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

  const { data } = await webOtoDevSdk.formulas.update({
    set: 'set',
  });

  console.log(data);
})();
```

## remove

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/formulas/all/remove`

**Parameters**

| Name  | Type   | Required | Description |
| :---- | :----- | :------- | :---------- |
| name  | string | ❌       |             |
| value | string | ❌       |             |
| set   | string | ❌       |             |

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

  const { data } = await webOtoDevSdk.formulas.remove({
    name: 'name',
    value: 'value',
    set: 'set',
  });

  console.log(data);
})();
```

## display

Display a list of all formulas with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/formulas/all/display`

**Parameters**

| Name   | Type   | Required | Description |
| :----- | :----- | :------- | :---------- |
| name   | string | ❌       |             |
| set    | string | ❌       |             |
| format | string | ❌       |             |

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

  const { data } = await webOtoDevSdk.formulas.display({
    name: 'name',
    set: 'set',
    format: 'format',
  });

  console.log(data);
})();
```

<!-- This file was generated by liblab | https://liblab.com/ -->
