// This file was generated by liblab | https://liblab.com/

package properties

type NewRequestParams struct {
	Init  *string `queryParam:"init"`
	Build *string `queryParam:"build"`
}

func (params *NewRequestParams) SetInit(init string) {
	params.Init = &init
}
func (params *NewRequestParams) SetBuild(build string) {
	params.Build = &build
}

type GetRequestParams struct {
	Name  *string `queryParam:"name" required:"true"`
	Build *string `queryParam:"build"`
}

func (params *GetRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *GetRequestParams) SetBuild(build string) {
	params.Build = &build
}

type SetRequestParams struct {
	Name  *string `queryParam:"name" required:"true"`
	Value *string `queryParam:"value"`
	Build *string `queryParam:"build"`
}

func (params *SetRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *SetRequestParams) SetValue(value string) {
	params.Value = &value
}
func (params *SetRequestParams) SetBuild(build string) {
	params.Build = &build
}

type AddRequestParams struct {
	Name  *string `queryParam:"name" required:"true"`
	Value *string `queryParam:"value"`
	Build *string `queryParam:"build"`
}

func (params *AddRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *AddRequestParams) SetValue(value string) {
	params.Value = &value
}
func (params *AddRequestParams) SetBuild(build string) {
	params.Build = &build
}

type AllRequestParams struct {
	Name  *string `queryParam:"name"`
	Build *string `queryParam:"build"`
}

func (params *AllRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *AllRequestParams) SetBuild(build string) {
	params.Build = &build
}

type UpdateRequestParams struct {
	Build *string `queryParam:"build"`
}

func (params *UpdateRequestParams) SetBuild(build string) {
	params.Build = &build
}

type RemoveRequestParams struct {
	Name  *string `queryParam:"name"`
	Value *string `queryParam:"value"`
	Build *string `queryParam:"build"`
}

func (params *RemoveRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *RemoveRequestParams) SetValue(value string) {
	params.Value = &value
}
func (params *RemoveRequestParams) SetBuild(build string) {
	params.Build = &build
}

type DisplayRequestParams struct {
	Name   *string `queryParam:"name"`
	Build  *string `queryParam:"build"`
	Format *string `queryParam:"format"`
}

func (params *DisplayRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *DisplayRequestParams) SetBuild(build string) {
	params.Build = &build
}
func (params *DisplayRequestParams) SetFormat(format string) {
	params.Format = &format
}
