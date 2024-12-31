# ValuesService

A list of all methods in the `ValuesService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                             |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------- |
| [New](#new)         | Create new dataset (default or specified settings)                                                                      |
| [Get](#get)         | Obtain the lastest value for variable with specified 'name'                                                             |
| [Set](#set)         | Remove all previous values for specified 'name' and add a new value                                                     |
| [Add](#add)         | Add a new value for specified 'name'                                                                                    |
| [All](#all)         | Obtain a list of all values with specified 'name'                                                                       |
| [Update](#update)   | Remove previously set and add new values with specified 'name' fileds with values from 'values' fileds of provided list |
| [Remove](#remove)   | Remove all values for specified 'name'                                                                                  |
| [Display](#display) | Display a list of all values with specified 'name'                                                                      |

## New

Create new dataset (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/values/revision/new`

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
  "web-dev-sdk/pkg/values"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := values.NewRequestParams{}


response, err := client.Values.New(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Get

Obtain the lastest value for variable with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/values/actual/get`

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
  "web-dev-sdk/pkg/values"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := values.GetRequestParams{}
params.SetName("string")

response, err := client.Values.Get(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Set

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/values/actual/set`

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
  "web-dev-sdk/pkg/values"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := values.SetRequestParams{}
params.SetName("string")

response, err := client.Values.Set(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Add

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/values/actual/add`

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
  "web-dev-sdk/pkg/values"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := values.AddRequestParams{}
params.SetName("string")

response, err := client.Values.Add(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## All

Obtain a list of all values with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/values/all/get`

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
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/values"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := values.AllRequestParams{}


response, err := client.Values.All(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Update

Remove previously set and add new values with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/values/all/update`

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
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/values"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := values.UpdateRequestParams{}


response, err := client.Values.Update(context.Background(), request, params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Remove

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/values/all/remove`

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
  "web-dev-sdk/pkg/values"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := values.RemoveRequestParams{}


response, err := client.Values.Remove(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Display

Display a list of all values with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/values/all/display`

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
  "web-dev-sdk/pkg/values"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := values.DisplayRequestParams{}


response, err := client.Values.Display(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
