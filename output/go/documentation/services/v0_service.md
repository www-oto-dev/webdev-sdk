# V0Service

A list of all methods in the `V0Service` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description |
| :-------------------------------------------------------------------- | :---------- |
| [ReadRootV0AdminGet](#readrootv0adminget)                             |             |
| [ReadRootV0AdminProjectsGet](#readrootv0adminprojectsget)             |             |
| [ReadRootV0ControlGet](#readrootv0controlget)                         |             |
| [ReadRootV0ControlProjectsGet](#readrootv0controlprojectsget)         |             |
| [ReadRootV0ProjectGet](#readrootv0projectget)                         |             |
| [ReadRootV0ProjectproperiesSetPut](#readrootv0projectproperiessetput) |             |

## ReadRootV0AdminGet

- HTTP Method: `GET`
- Endpoint: `/v0/admin/`

**Parameters**

| Name | Type    | Required | Description                 |
| :--- | :------ | :------- | :-------------------------- |
| ctx  | Context | ✅       | Default go language context |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webdevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webdevsdk"
)

config := webdevsdkconfig.NewConfig()
client := webdevsdk.NewWebdevSdk(config)

response, err := client.V0.ReadRootV0AdminGet(context.Background())
if err != nil {
  panic(err)
}

fmt.Print(response)
```

## ReadRootV0AdminProjectsGet

- HTTP Method: `GET`
- Endpoint: `/v0/admin/projects`

**Parameters**

| Name | Type    | Required | Description                 |
| :--- | :------ | :------- | :-------------------------- |
| ctx  | Context | ✅       | Default go language context |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webdevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webdevsdk"
)

config := webdevsdkconfig.NewConfig()
client := webdevsdk.NewWebdevSdk(config)

response, err := client.V0.ReadRootV0AdminProjectsGet(context.Background())
if err != nil {
  panic(err)
}

fmt.Print(response)
```

## ReadRootV0ControlGet

- HTTP Method: `GET`
- Endpoint: `/v0/control/`

**Parameters**

| Name | Type    | Required | Description                 |
| :--- | :------ | :------- | :-------------------------- |
| ctx  | Context | ✅       | Default go language context |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webdevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webdevsdk"
)

config := webdevsdkconfig.NewConfig()
client := webdevsdk.NewWebdevSdk(config)

response, err := client.V0.ReadRootV0ControlGet(context.Background())
if err != nil {
  panic(err)
}

fmt.Print(response)
```

## ReadRootV0ControlProjectsGet

- HTTP Method: `GET`
- Endpoint: `/v0/control/projects`

**Parameters**

| Name | Type    | Required | Description                 |
| :--- | :------ | :------- | :-------------------------- |
| ctx  | Context | ✅       | Default go language context |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webdevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webdevsdk"
)

config := webdevsdkconfig.NewConfig()
client := webdevsdk.NewWebdevSdk(config)

response, err := client.V0.ReadRootV0ControlProjectsGet(context.Background())
if err != nil {
  panic(err)
}

fmt.Print(response)
```

## ReadRootV0ProjectGet

- HTTP Method: `GET`
- Endpoint: `/v0/project/`

**Parameters**

| Name | Type    | Required | Description                 |
| :--- | :------ | :------- | :-------------------------- |
| ctx  | Context | ✅       | Default go language context |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webdevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webdevsdk"
)

config := webdevsdkconfig.NewConfig()
client := webdevsdk.NewWebdevSdk(config)

response, err := client.V0.ReadRootV0ProjectGet(context.Background())
if err != nil {
  panic(err)
}

fmt.Print(response)
```

## ReadRootV0ProjectproperiesSetPut

- HTTP Method: `PUT`
- Endpoint: `/v0/projectproperies/set`

**Parameters**

| Name | Type    | Required | Description                 |
| :--- | :------ | :------- | :-------------------------- |
| ctx  | Context | ✅       | Default go language context |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "github.com/swagger-api/swagger-petstore/pkg/webdevsdkconfig"
  "github.com/swagger-api/swagger-petstore/pkg/webdevsdk"
)

config := webdevsdkconfig.NewConfig()
client := webdevsdk.NewWebdevSdk(config)

response, err := client.V0.ReadRootV0ProjectproperiesSetPut(context.Background())
if err != nil {
  panic(err)
}

fmt.Print(response)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
