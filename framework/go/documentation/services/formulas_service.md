# FormulasService

A list of all methods in the `FormulasService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                               |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------ |
| [New](#new)         | Create new set (default or specified settings)                                                                            |
| [Get](#get)         | Obtain the lastest value for formula with specified 'name'                                                                |
| [Set](#set)         | Remove all previous values for specified 'name' and add a new value                                                       |
| [Add](#add)         | Add a new value for specified 'name'                                                                                      |
| [All](#all)         | Obtain a list of all formulas with specified 'name'                                                                       |
| [Update](#update)   | Remove previously set and add new formulas with specified 'name' fileds with values from 'values' fileds of provided list |
| [Remove](#remove)   | Remove all values for specified 'name'                                                                                    |
| [Display](#display) | Display a list of all formulas with specified 'name'                                                                      |

## New

Create new set (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/formulas/revision/new`

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
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/formulas"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := formulas.NewRequestParams{}


response, err := client.Formulas.New(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Get

Obtain the lastest value for formula with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/formulas/actual/get`

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
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/formulas"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := formulas.GetRequestParams{}
params.SetName("string")

response, err := client.Formulas.Get(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Set

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/formulas/actual/set`

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
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/formulas"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := formulas.SetRequestParams{}
params.SetName("string")

response, err := client.Formulas.Set(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Add

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/formulas/actual/add`

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
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/formulas"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := formulas.AddRequestParams{}
params.SetName("string")

response, err := client.Formulas.Add(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## All

Obtain a list of all formulas with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/formulas/all/get`

**Parameters**

| Name   | Type             | Required | Description                   |
| :----- | :--------------- | :------- | :---------------------------- |
| ctx    | Context          | ✅       | Default go language context   |
| params | AllRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]Formula`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/formulas"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := formulas.AllRequestParams{}


response, err := client.Formulas.All(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Update

Remove previously set and add new formulas with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/formulas/all/update`

**Parameters**

| Name    | Type                | Required | Description                   |
| :------ | :------------------ | :------- | :---------------------------- |
| ctx     | Context             | ✅       | Default go language context   |
| formula | []Formula           | ✅       |                               |
| params  | UpdateRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/formulas"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := formulas.UpdateRequestParams{}


response, err := client.Formulas.Update(context.Background(), request, params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Remove

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/formulas/all/remove`

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
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/formulas"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := formulas.RemoveRequestParams{}


response, err := client.Formulas.Remove(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Display

Display a list of all formulas with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/formulas/all/display`

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
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/formulas"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := formulas.DisplayRequestParams{}


response, err := client.Formulas.Display(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
