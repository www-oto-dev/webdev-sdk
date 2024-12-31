// This file was generated by liblab | https://liblab.com/

package formulas

type NewRequestParams struct {
	Init *string `queryParam:"init"`
	Set  *string `queryParam:"set"`
}

func (params *NewRequestParams) SetInit(init string) {
	params.Init = &init
}
func (params *NewRequestParams) SetSet(set string) {
	params.Set = &set
}

type GetRequestParams struct {
	Name *string `queryParam:"name" required:"true"`
	Set  *string `queryParam:"set"`
}

func (params *GetRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *GetRequestParams) SetSet(set string) {
	params.Set = &set
}

type SetRequestParams struct {
	Name   *string `queryParam:"name" required:"true"`
	Value  *string `queryParam:"value"`
	Form   *string `queryParam:"form"`
	Engine *string `queryParam:"engine"`
	Set    *string `queryParam:"set"`
}

func (params *SetRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *SetRequestParams) SetValue(value string) {
	params.Value = &value
}
func (params *SetRequestParams) SetForm(form string) {
	params.Form = &form
}
func (params *SetRequestParams) SetEngine(engine string) {
	params.Engine = &engine
}
func (params *SetRequestParams) SetSet(set string) {
	params.Set = &set
}

type AddRequestParams struct {
	Name   *string `queryParam:"name" required:"true"`
	Value  *string `queryParam:"value"`
	Form   *string `queryParam:"form"`
	Engine *string `queryParam:"engine"`
	Set    *string `queryParam:"set"`
}

func (params *AddRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *AddRequestParams) SetValue(value string) {
	params.Value = &value
}
func (params *AddRequestParams) SetForm(form string) {
	params.Form = &form
}
func (params *AddRequestParams) SetEngine(engine string) {
	params.Engine = &engine
}
func (params *AddRequestParams) SetSet(set string) {
	params.Set = &set
}

type AllRequestParams struct {
	Name *string `queryParam:"name"`
	Set  *string `queryParam:"set"`
}

func (params *AllRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *AllRequestParams) SetSet(set string) {
	params.Set = &set
}

type UpdateRequestParams struct {
	Set *string `queryParam:"set"`
}

func (params *UpdateRequestParams) SetSet(set string) {
	params.Set = &set
}

type RemoveRequestParams struct {
	Name  *string `queryParam:"name"`
	Value *string `queryParam:"value"`
	Set   *string `queryParam:"set"`
}

func (params *RemoveRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *RemoveRequestParams) SetValue(value string) {
	params.Value = &value
}
func (params *RemoveRequestParams) SetSet(set string) {
	params.Set = &set
}

type DisplayRequestParams struct {
	Name   *string `queryParam:"name"`
	Set    *string `queryParam:"set"`
	Format *string `queryParam:"format"`
}

func (params *DisplayRequestParams) SetName(name string) {
	params.Name = &name
}
func (params *DisplayRequestParams) SetSet(set string) {
	params.Set = &set
}
func (params *DisplayRequestParams) SetFormat(format string) {
	params.Format = &format
}
