// This file was generated by liblab | https://liblab.com/

package layouts

type NewRequestParams struct {
	Init    *string `queryParam:"init"`
	Version *string `queryParam:"version"`
}

func (params *NewRequestParams) SetInit(init string) {
	params.Init = &init
}
func (params *NewRequestParams) SetVersion(version string) {
	params.Version = &version
}

type GetRequestParams struct {
	Name    *string `queryParam:"name" required:"true"`
	Version *string `queryParam:"version"`
}

func (params *GetRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *GetRequestParams) SetVersion(version string) {
	params.Version = &version
}

type SetRequestParams struct {
	Name    *string `queryParam:"name" required:"true"`
	Value   *string `queryParam:"value"`
	Version *string `queryParam:"version"`
}

func (params *SetRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *SetRequestParams) SetValue(value string) {
	params.Value = &value
}
func (params *SetRequestParams) SetVersion(version string) {
	params.Version = &version
}

type AddRequestParams struct {
	Name    *string `queryParam:"name" required:"true"`
	Value   *string `queryParam:"value"`
	Version *string `queryParam:"version"`
}

func (params *AddRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *AddRequestParams) SetValue(value string) {
	params.Value = &value
}
func (params *AddRequestParams) SetVersion(version string) {
	params.Version = &version
}

type AllRequestParams struct {
	Name    *string `queryParam:"name"`
	Version *string `queryParam:"version"`
}

func (params *AllRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *AllRequestParams) SetVersion(version string) {
	params.Version = &version
}

type UpdateRequestParams struct {
	Version *string `queryParam:"version"`
}

func (params *UpdateRequestParams) SetVersion(version string) {
	params.Version = &version
}

type RemoveRequestParams struct {
	Name    *string `queryParam:"name"`
	Value   *string `queryParam:"value"`
	Version *string `queryParam:"version"`
}

func (params *RemoveRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *RemoveRequestParams) SetValue(value string) {
	params.Value = &value
}
func (params *RemoveRequestParams) SetVersion(version string) {
	params.Version = &version
}

type DisplayRequestParams struct {
	Name    *string `queryParam:"name"`
	Version *string `queryParam:"version"`
	Format  *string `queryParam:"format"`
}

func (params *DisplayRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *DisplayRequestParams) SetVersion(version string) {
	params.Version = &version
}
func (params *DisplayRequestParams) SetFormat(format string) {
	params.Format = &format
}
