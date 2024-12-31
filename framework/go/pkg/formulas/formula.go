// This file was generated by liblab | https://liblab.com/

package formulas

import (
	"encoding/json"
)

type Formula struct {
	Name    *string `json:"name,omitempty" required:"true"`
	Value   *string `json:"value,omitempty"`
	Form    *string `json:"form,omitempty"`
	Engine  *string `json:"engine,omitempty"`
	touched map[string]bool
}

func (f *Formula) GetName() *string {
	if f == nil {
		return nil
	}
	return f.Name
}

func (f *Formula) SetName(name string) {
	if f.touched == nil {
		f.touched = map[string]bool{}
	}
	f.touched["Name"] = true
	f.Name = &name
}

func (f *Formula) SetNameNil() {
	if f.touched == nil {
		f.touched = map[string]bool{}
	}
	f.touched["Name"] = true
	f.Name = nil
}

func (f *Formula) GetValue() *string {
	if f == nil {
		return nil
	}
	return f.Value
}

func (f *Formula) SetValue(value string) {
	if f.touched == nil {
		f.touched = map[string]bool{}
	}
	f.touched["Value"] = true
	f.Value = &value
}

func (f *Formula) SetValueNil() {
	if f.touched == nil {
		f.touched = map[string]bool{}
	}
	f.touched["Value"] = true
	f.Value = nil
}

func (f *Formula) GetForm() *string {
	if f == nil {
		return nil
	}
	return f.Form
}

func (f *Formula) SetForm(form string) {
	if f.touched == nil {
		f.touched = map[string]bool{}
	}
	f.touched["Form"] = true
	f.Form = &form
}

func (f *Formula) SetFormNil() {
	if f.touched == nil {
		f.touched = map[string]bool{}
	}
	f.touched["Form"] = true
	f.Form = nil
}

func (f *Formula) GetEngine() *string {
	if f == nil {
		return nil
	}
	return f.Engine
}

func (f *Formula) SetEngine(engine string) {
	if f.touched == nil {
		f.touched = map[string]bool{}
	}
	f.touched["Engine"] = true
	f.Engine = &engine
}

func (f *Formula) SetEngineNil() {
	if f.touched == nil {
		f.touched = map[string]bool{}
	}
	f.touched["Engine"] = true
	f.Engine = nil
}
func (f Formula) MarshalJSON() ([]byte, error) {
	data := make(map[string]any)

	if f.touched["Name"] && f.Name == nil {
		data["name"] = nil
	} else if f.Name != nil {
		data["name"] = f.Name
	}

	if f.touched["Value"] && f.Value == nil {
		data["value"] = nil
	} else if f.Value != nil {
		data["value"] = f.Value
	}

	if f.touched["Form"] && f.Form == nil {
		data["form"] = nil
	} else if f.Form != nil {
		data["form"] = f.Form
	}

	if f.touched["Engine"] && f.Engine == nil {
		data["engine"] = nil
	} else if f.Engine != nil {
		data["engine"] = f.Engine
	}

	return json.Marshal(data)
}
