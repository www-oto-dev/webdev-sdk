// This file was generated by liblab | https://liblab.com/

package hooks

type Hook interface {
	BeforeRequest(req Request, params map[string]string) Request
	AfterResponse(req Request, resp Response, params map[string]string) Response
	OnError(req Request, resp ErrorResponse, params map[string]string) ErrorResponse
}

type Request interface {
	GetMethod() string
	SetMethod(method string)
	GetBaseUrl() string
	SetBaseUrl(baseUrl string)
	GetPath() string
	SetPath(path string)
	GetPathParam(param string) string
	SetPathParam(param string, value any)
	GetHeader(header string) string
	SetHeader(header string, value string)
	GetQueryParam(header string) string
	SetQueryParam(header string, value string)
	GetOptions() any
	SetOptions(options any)
	GetBody() any
	SetBody(body any)
}

type Response interface {
	GetStatusCode() int
	SetStatusCode(statusCode int)
	GetHeader(header string) string
	SetHeader(header string, value string)
	GetBody() []byte
	SetBody(body []byte)
}

type ErrorResponse interface {
	Error() string
	GetError() error
	GetStatusCode() int
	SetStatusCode(statusCode int)
	GetHeader(header string) string
	SetHeader(header string, value string)
	GetBody() []byte
	SetBody(body []byte)
}
