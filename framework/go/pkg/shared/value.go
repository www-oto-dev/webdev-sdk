// This file was generated by liblab | https://liblab.com/

package shared

import (
	"encoding/json"
)

type Value struct {
	Name    *string `json:"name,omitempty" required:"true"`
	Value   *string `json:"value,omitempty"`
	touched map[string]bool
}

func (v *Value) GetName() *string {
	if v == nil {
		return nil
	}
	return v.Name
}

func (v *Value) SetName(name string) {
	if v.touched == nil {
		v.touched = map[string]bool{}
	}
	v.touched["Name"] = true
	v.Name = &name
}

func (v *Value) SetNameNil() {
	if v.touched == nil {
		v.touched = map[string]bool{}
	}
	v.touched["Name"] = true
	v.Name = nil
}

func (v *Value) GetValue() *string {
	if v == nil {
		return nil
	}
	return v.Value
}

func (v *Value) SetValue(value string) {
	if v.touched == nil {
		v.touched = map[string]bool{}
	}
	v.touched["Value"] = true
	v.Value = &value
}

func (v *Value) SetValueNil() {
	if v.touched == nil {
		v.touched = map[string]bool{}
	}
	v.touched["Value"] = true
	v.Value = nil
}
func (v Value) MarshalJSON() ([]byte, error) {
	data := make(map[string]any)

	if v.touched["Name"] && v.Name == nil {
		data["name"] = nil
	} else if v.Name != nil {
		data["name"] = v.Name
	}

	if v.touched["Value"] && v.Value == nil {
		data["value"] = nil
	} else if v.Value != nil {
		data["value"] = v.Value
	}

	return json.Marshal(data)
}
