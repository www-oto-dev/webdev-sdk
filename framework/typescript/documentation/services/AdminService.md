# AdminService

A list of all methods in the `AdminService` service. Click on the method name to view detailed information about that method.

| Methods                                   | Description                                              |
| :---------------------------------------- | :------------------------------------------------------- |
| [projects](#projects)                     | Obtain a list of all projects [ADMIN RIGHTS REQUIRED]    |
| [newProject](#newproject)                 | Create project [ADMIN RIGHTS REQUIRED]                   |
| [removeProject](#removeproject)           | Remove project with specified ID [ADMIN RIGHTS REQUIRED] |
| [changeProject](#changeproject)           | Change options [ADMIN RIGHTS REQUIRED]                   |
| [changeProjectSlug](#changeprojectslug)   | Change project slug [ADMIN RIGHTS REQUIRED]              |
| [changeProjectTitle](#changeprojecttitle) | Change project title [ADMIN RIGHTS REQUIRED]             |

## projects

Obtain a list of all projects [ADMIN RIGHTS REQUIRED]

- HTTP Method: `GET`
- Endpoint: `/admin/projects/all`

**Return Type**

`Project[]`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.admin.projects();

  console.log(data);
})();
```

## newProject

Create project [ADMIN RIGHTS REQUIRED]

- HTTP Method: `PUT`
- Endpoint: `/admin/projects/new`

**Parameters**

| Name     | Type    | Required | Description |
| :------- | :------ | :------- | :---------- |
| title    | string  | ❌       |             |
| slug     | string  | ❌       |             |
| init     | string  | ❌       |             |
| internal | boolean | ❌       |             |

**Return Type**

`boolean`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.admin.newProject({
    title: 'title',
    slug: 'slug',
    init: 'init',
    internal: true,
  });

  console.log(data);
})();
```

## removeProject

Remove project with specified ID [ADMIN RIGHTS REQUIRED]

- HTTP Method: `DELETE`
- Endpoint: `/admin/projects/remove`

**Parameters**

| Name     | Type    | Required | Description |
| :------- | :------ | :------- | :---------- |
| slug     | string  | ❌       |             |
| uid      | string  | ❌       |             |
| internal | boolean | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.admin.removeProject({
    slug: 'slug',
    uid: 'uid',
    internal: true,
  });

  console.log(data);
})();
```

## changeProject

Change options [ADMIN RIGHTS REQUIRED]

- HTTP Method: `PUT`
- Endpoint: `/admin/projects/change`

**Parameters**

| Name     | Type    | Required | Description |
| :------- | :------ | :------- | :---------- |
| slug     | string  | ❌       |             |
| uid      | string  | ❌       |             |
| newSlug  | string  | ❌       |             |
| newTitle | string  | ❌       |             |
| internal | boolean | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.admin.changeProject({
    slug: 'slug',
    uid: 'uid',
    newSlug: 'new_slug',
    newTitle: 'new_title',
    internal: true,
  });

  console.log(data);
})();
```

## changeProjectSlug

Change project slug [ADMIN RIGHTS REQUIRED]

- HTTP Method: `PUT`
- Endpoint: `/admin/projects/change/slug`

**Parameters**

| Name     | Type    | Required | Description |
| :------- | :------ | :------- | :---------- |
| slug     | string  | ❌       |             |
| uid      | string  | ❌       |             |
| newSlug  | string  | ❌       |             |
| internal | boolean | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.admin.changeProjectSlug({
    slug: 'slug',
    uid: 'uid',
    newSlug: 'new_slug',
    internal: true,
  });

  console.log(data);
})();
```

## changeProjectTitle

Change project title [ADMIN RIGHTS REQUIRED]

- HTTP Method: `PUT`
- Endpoint: `/admin/projects/change/title`

**Parameters**

| Name     | Type    | Required | Description |
| :------- | :------ | :------- | :---------- |
| slug     | string  | ❌       |             |
| uid      | string  | ❌       |             |
| newTitle | string  | ❌       |             |
| internal | boolean | ❌       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```typescript
import { WebOtoDevSdk } from 'web-oto-dev-sdk';

(async () => {
  const webOtoDevSdk = new WebOtoDevSdk({
    apiKey: 'YOUR_API_KEY',
  });

  const { data } = await webOtoDevSdk.admin.changeProjectTitle({
    slug: 'slug',
    uid: 'uid',
    newTitle: 'new_title',
    internal: true,
  });

  console.log(data);
})();
```

<!-- This file was generated by liblab | https://liblab.com/ -->
