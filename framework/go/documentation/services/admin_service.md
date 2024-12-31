# AdminService

A list of all methods in the `AdminService` service. Click on the method name to view detailed information about that method.

| Methods                                   | Description                                              |
| :---------------------------------------- | :------------------------------------------------------- |
| [Projects](#projects)                     | Obtain a list of all projects [ADMIN RIGHTS REQUIRED]    |
| [NewProject](#newproject)                 | Create project [ADMIN RIGHTS REQUIRED]                   |
| [RemoveProject](#removeproject)           | Remove project with specified ID [ADMIN RIGHTS REQUIRED] |
| [ChangeProject](#changeproject)           | Change options [ADMIN RIGHTS REQUIRED]                   |
| [ChangeProjectSlug](#changeprojectslug)   | Change project slug [ADMIN RIGHTS REQUIRED]              |
| [ChangeProjectTitle](#changeprojecttitle) | Change project title [ADMIN RIGHTS REQUIRED]             |

## Projects

Obtain a list of all projects [ADMIN RIGHTS REQUIRED]

- HTTP Method: `GET`
- Endpoint: `/admin/projects/all`

**Parameters**

| Name | Type    | Required | Description                 |
| :--- | :------ | :------- | :-------------------------- |
| ctx  | Context | ✅       | Default go language context |

**Return Type**

`[]shared.Project`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)

response, err := client.Admin.Projects(context.Background())
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## NewProject

Create project [ADMIN RIGHTS REQUIRED]

- HTTP Method: `PUT`
- Endpoint: `/admin/projects/new`

**Parameters**

| Name   | Type                    | Required | Description                   |
| :----- | :---------------------- | :------- | :---------------------------- |
| ctx    | Context                 | ✅       | Default go language context   |
| params | NewProjectRequestParams | ✅       | Additional request parameters |

**Return Type**

`bool`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/admin"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := admin.NewProjectRequestParams{}


response, err := client.Admin.NewProject(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## RemoveProject

Remove project with specified ID [ADMIN RIGHTS REQUIRED]

- HTTP Method: `DELETE`
- Endpoint: `/admin/projects/remove`

**Parameters**

| Name   | Type                       | Required | Description                   |
| :----- | :------------------------- | :------- | :---------------------------- |
| ctx    | Context                    | ✅       | Default go language context   |
| params | RemoveProjectRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/admin"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := admin.RemoveProjectRequestParams{}


response, err := client.Admin.RemoveProject(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## ChangeProject

Change options [ADMIN RIGHTS REQUIRED]

- HTTP Method: `PUT`
- Endpoint: `/admin/projects/change`

**Parameters**

| Name   | Type                       | Required | Description                   |
| :----- | :------------------------- | :------- | :---------------------------- |
| ctx    | Context                    | ✅       | Default go language context   |
| params | ChangeProjectRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/admin"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := admin.ChangeProjectRequestParams{}


response, err := client.Admin.ChangeProject(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## ChangeProjectSlug

Change project slug [ADMIN RIGHTS REQUIRED]

- HTTP Method: `PUT`
- Endpoint: `/admin/projects/change/slug`

**Parameters**

| Name   | Type                           | Required | Description                   |
| :----- | :----------------------------- | :------- | :---------------------------- |
| ctx    | Context                        | ✅       | Default go language context   |
| params | ChangeProjectSlugRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/admin"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := admin.ChangeProjectSlugRequestParams{}


response, err := client.Admin.ChangeProjectSlug(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## ChangeProjectTitle

Change project title [ADMIN RIGHTS REQUIRED]

- HTTP Method: `PUT`
- Endpoint: `/admin/projects/change/title`

**Parameters**

| Name   | Type                            | Required | Description                   |
| :----- | :------------------------------ | :------- | :---------------------------- |
| ctx    | Context                         | ✅       | Default go language context   |
| params | ChangeProjectTitleRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/admin"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := admin.ChangeProjectTitleRequestParams{}


response, err := client.Admin.ChangeProjectTitle(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
