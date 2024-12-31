# LayoutsService

A list of all methods in the `LayoutsService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                                |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------- |
| [New](#new)         | Create new version (default or specified settings)                                                                         |
| [Get](#get)         | Obtain the lastest layout for page with specified 'name'                                                                   |
| [Set](#set)         | Remove all previous layouts for specified page with 'name' and add a new value                                             |
| [Add](#add)         | Add a new value for specified page by 'name'                                                                               |
| [All](#all)         | Obtain a list of all layouts with specified 'name'                                                                         |
| [Update](#update)   | Remove previously set and add new layouts with specified 'name' fileds with layouts from 'layouts' fileds of provided list |
| [Remove](#remove)   | Remove all layouts for specified 'name'                                                                                    |
| [Display](#display) | Display a list of all layouts with specified 'name'                                                                        |

## New

Create new version (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/layouts/revision/new`

**Parameters**

| Name   | Type             | Required | Description                   |
| :----- | :--------------- | :------- | :---------------------------- |
| ctx    | Context          | ✅       | Default go language context   |
| params | NewRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/layouts"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := layouts.NewRequestParams{}


response, err := client.Layouts.New(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Get

Obtain the lastest layout for page with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/layouts/actual/get`

**Parameters**

| Name   | Type             | Required | Description                   |
| :----- | :--------------- | :------- | :---------------------------- |
| ctx    | Context          | ✅       | Default go language context   |
| params | GetRequestParams | ✅       | Additional request parameters |

**Return Type**

`string`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/layouts"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := layouts.GetRequestParams{}
params.SetName("string")

response, err := client.Layouts.Get(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Set

Remove all previous layouts for specified page with 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/layouts/actual/set`

**Parameters**

| Name   | Type             | Required | Description                   |
| :----- | :--------------- | :------- | :---------------------------- |
| ctx    | Context          | ✅       | Default go language context   |
| params | SetRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/layouts"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := layouts.SetRequestParams{}
params.SetName("string")

response, err := client.Layouts.Set(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Add

Add a new value for specified page by 'name'

- HTTP Method: `PUT`
- Endpoint: `/layouts/actual/add`

**Parameters**

| Name   | Type             | Required | Description                   |
| :----- | :--------------- | :------- | :---------------------------- |
| ctx    | Context          | ✅       | Default go language context   |
| params | AddRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/layouts"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := layouts.AddRequestParams{}
params.SetName("string")

response, err := client.Layouts.Add(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## All

Obtain a list of all layouts with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/layouts/all/get`

**Parameters**

| Name   | Type             | Required | Description                   |
| :----- | :--------------- | :------- | :---------------------------- |
| ctx    | Context          | ✅       | Default go language context   |
| params | AllRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]shared.Value`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/layouts"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := layouts.AllRequestParams{}


response, err := client.Layouts.All(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Update

Remove previously set and add new layouts with specified 'name' fileds with layouts from 'layouts' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/layouts/all/update`

**Parameters**

| Name   | Type                | Required | Description                   |
| :----- | :------------------ | :------- | :---------------------------- |
| ctx    | Context             | ✅       | Default go language context   |
| value  | []shared.Value      | ✅       |                               |
| params | UpdateRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/layouts"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := layouts.UpdateRequestParams{}


response, err := client.Layouts.Update(context.Background(), request, params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Remove

Remove all layouts for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/layouts/all/remove`

**Parameters**

| Name   | Type                | Required | Description                   |
| :----- | :------------------ | :------- | :---------------------------- |
| ctx    | Context             | ✅       | Default go language context   |
| params | RemoveRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/layouts"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := layouts.RemoveRequestParams{}


response, err := client.Layouts.Remove(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Display

Display a list of all layouts with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/layouts/all/display`

**Parameters**

| Name   | Type                 | Required | Description                   |
| :----- | :------------------- | :------- | :---------------------------- |
| ctx    | Context              | ✅       | Default go language context   |
| params | DisplayRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/layouts"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := layouts.DisplayRequestParams{}


response, err := client.Layouts.Display(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
