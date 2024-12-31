# PropertiesService

A list of all methods in the `PropertiesService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                                 |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------------- |
| [New](#new)         | Create new build (default or specified settings)                                                                            |
| [Get](#get)         | Obtain the lastest value for formula with specified 'name'                                                                  |
| [Set](#set)         | Remove all previous values for specified 'name' and add a new value                                                         |
| [Add](#add)         | Add a new value for specified 'name'                                                                                        |
| [All](#all)         | Obtain a list of all properties with specified 'name'                                                                       |
| [Update](#update)   | Remove previously set and add new properties with specified 'name' fileds with values from 'values' fileds of provided list |
| [Remove](#remove)   | Remove all values for specified 'name'                                                                                      |
| [Display](#display) | Display a list of all properties with specified 'name'                                                                      |

## New

Create new build (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/properties/revision/new`

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
  "github.com/swagger-api/swagger-petstore/pkg/properties"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := properties.NewRequestParams{}


response, err := client.Properties.New(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Get

Obtain the lastest value for formula with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/properties/actual/get`

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
  "github.com/swagger-api/swagger-petstore/pkg/properties"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := properties.GetRequestParams{}
params.SetName("string")

response, err := client.Properties.Get(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Set

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/properties/actual/set`

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
  "github.com/swagger-api/swagger-petstore/pkg/properties"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := properties.SetRequestParams{}
params.SetName("string")

response, err := client.Properties.Set(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Add

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/properties/actual/add`

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
  "github.com/swagger-api/swagger-petstore/pkg/properties"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := properties.AddRequestParams{}
params.SetName("string")

response, err := client.Properties.Add(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## All

Obtain a list of all properties with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/properties/all/get`

**Parameters**

| Name   | Type             | Required | Description                   |
| :----- | :--------------- | :------- | :---------------------------- |
| ctx    | Context          | ✅       | Default go language context   |
| params | AllRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]Property`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/properties"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := properties.AllRequestParams{}


response, err := client.Properties.All(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Update

Remove previously set and add new properties with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/properties/all/update`

**Parameters**

| Name     | Type                | Required | Description                   |
| :------- | :------------------ | :------- | :---------------------------- |
| ctx      | Context             | ✅       | Default go language context   |
| property | []Property          | ✅       |                               |
| params   | UpdateRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webotodevsdk"
  "github.com/swagger-api/swagger-petstore/pkg/properties"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := properties.UpdateRequestParams{}


response, err := client.Properties.Update(context.Background(), request, params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Remove

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/properties/all/remove`

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
  "github.com/swagger-api/swagger-petstore/pkg/properties"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := properties.RemoveRequestParams{}


response, err := client.Properties.Remove(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Display

Display a list of all properties with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/properties/all/display`

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
  "github.com/swagger-api/swagger-petstore/pkg/properties"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := properties.DisplayRequestParams{}


response, err := client.Properties.Display(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
